"""Input validation helpers."""
import re

_USERNAME_RE = re.compile(r"^[A-Za-z0-9_.-]{1,39}$")
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate_username(value: str) -> tuple[bool, str]:
    username = value.strip()
    if not username:
        return False, "Username cannot be empty."
    if not _USERNAME_RE.fullmatch(username):
        return False, "Use 1-39 letters, digits, dots, underscores, or hyphens."
    return True, username


def analyze_email_syntax(value: str) -> dict:
    """Check syntax only; this does not verify ownership or mailbox existence."""
    email = value.strip()
    if not email:
        return {"valid_syntax": False, "normalized": "", "message": "Email cannot be empty."}

    valid = bool(_EMAIL_RE.fullmatch(email))
    domain = email.rsplit("@", 1)[1].lower() if valid else None
    return {
        "valid_syntax": valid,
        "normalized": email,
        "domain": domain,
        "message": (
            "Syntax looks plausible; mailbox ownership/existence is not verified."
            if valid else "Email syntax is not valid."
        ),
    }
