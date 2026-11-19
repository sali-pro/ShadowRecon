"""Conservative checks of ordinary, publicly accessible profile URLs."""
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from modules.config import PLATFORMS, USER_AGENT
from modules.validators import validate_username


@dataclass
class ProfileResult:
    platform: str
    url: str
    status: str
    http_status: int | None
    checked_at_utc: str
    detail: str

    def to_dict(self):
        return asdict(self)


def check_profile(platform: str, username: str, timeout: float = 8.0) -> ProfileResult:
    valid, message = validate_username(username)
    if not valid:
        raise ValueError(message)
    if platform not in PLATFORMS:
        raise ValueError(f"Unsupported platform: {platform}")

    url = PLATFORMS[platform].format(username=username)
    checked_at = datetime.now(timezone.utc).isoformat(timespec="seconds")

    request = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        # A single ordinary GET request to the public profile URL.
        with urlopen(request, timeout=timeout) as response:
            code = response.status
        if code == 200:
            status, detail = "page_reachable", (
                "The public page responded successfully. This does not prove "
                "the account exists; sites may show generic or soft-404 pages."
            )
        else:
            status, detail = "uncertain", f"Received HTTP {code}; interpret cautiously."
        return ProfileResult(platform, url, status, code, checked_at, detail)

    except HTTPError as exc:
        if exc.code == 404:
            status, detail = "not_found_response", (
                "The site returned 404. This is not definitive proof that no account exists."
            )
        elif exc.code in (401, 403, 429):
            status, detail = "restricted_or_rate_limited", (
                f"The site returned HTTP {exc.code}. No attempt was made to bypass restrictions."
            )
        else:
            status, detail = "http_error", f"The site returned HTTP {exc.code}."
        return ProfileResult(platform, url, status, exc.code, checked_at, detail)

    except (URLError, TimeoutError, OSError) as exc:
        reason = getattr(exc, "reason", exc)
        return ProfileResult(
            platform, url, "network_error", None, checked_at,
            f"Could not complete the request: {reason}"
        )
