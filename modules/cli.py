"""Interactive command-line interface."""
from datetime import datetime, timezone
from modules.config import APP_NAME, VERSION, PLATFORMS
from modules.profile_checker import check_profile
from modules.reporting import save_csv, save_json
from modules.validators import validate_username, analyze_email_syntax


def _header():
    print("\n" + "=" * 48)
    print(f"             {APP_NAME}  v{VERSION}")
    print("       Public-source footprint helper")
    print("=" * 48)


def _username_investigation():
    username = input("\nEnter a username: ").strip()
    valid, message = validate_username(username)
    if not valid:
        print(f"[!] {message}")
        return

    print("\nChecking selected public profile pages...")
    results = []
    for platform in PLATFORMS:
        result = check_profile(platform, message)
        results.append(result.to_dict())
        print(f"\n{result.platform}: {result.status}")
        print(f"  URL: {result.url}")
        if result.http_status is not None:
            print(f"  HTTP: {result.http_status}")
        print(f"  Note: {result.detail}")

    report = {
        "tool": APP_NAME,
        "version": VERSION,
        "created_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "query_type": "username",
        "username": message,
        "results": results,
        "limitations": [
            "Only ordinary public profile URLs were requested.",
            "A reachable page does not prove an account exists.",
            "A 404 response does not definitively prove an account is absent.",
            "No authentication, access-control bypass, CAPTCHA solving, or private-data collection.",
        ],
    }
    print("\nReport export:")
    print(f"  JSON: {save_json(report)}")
    print(f"  CSV:  {save_csv(results)}")


def _email_analysis():
    email = input("\nEnter an email address to analyze: ")
    result = analyze_email_syntax(email)
    print("\nEmail syntax analysis")
    print(f"  Valid syntax: {result['valid_syntax']}")
    if result.get("domain"):
        print(f"  Domain: {result['domain']}")
    print(f"  Note: {result['message']}")
    print("  Privacy: No message is sent and no mailbox lookup is performed.")


def main():
    _header()
    while True:
        print("\n[1] Public username profile checks")
        print("[2] Email syntax analysis")
        print("[3] About and safety limitations")
        print("[4] Exit")
        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            _username_investigation()
        elif choice == "2":
            _email_analysis()
        elif choice == "3":
            print("\nShadowRecon checks only public profile URLs and email syntax.")
            print("It does not identify private accounts, verify mailbox ownership,")
            print("bypass restrictions, or guarantee account existence.")
            print("Use only for lawful, authorized research.")
        elif choice == "4":
            print("\nExiting ShadowRecon. Stay ethical.")
            break
        else:
            print("\n[!] Invalid option. Choose 1, 2, 3, or 4.")
