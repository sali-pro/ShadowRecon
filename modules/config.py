"""Project configuration and supported public profile templates."""

APP_NAME = "ShadowRecon"
VERSION = "1.0.0"
USER_AGENT = "ShadowRecon/1.0 (+public-profile-check; educational use)"

# These checks only request ordinary public profile pages. They do not log in,
# bypass access controls, solve CAPTCHAs, or inspect private information.
PLATFORMS = {
    "GitHub": "https://github.com/{username}",
    "GitLab": "https://gitlab.com/{username}",
    "Reddit": "https://www.reddit.com/user/{username}/",
}
