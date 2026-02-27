import requests

# 🔐 Replace this with your GitHub Personal Access Token
GITHUB_TOKEN = "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"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def get_github_data(username):
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos"

    user_response = requests.get(user_url, headers=headers)

    if user_response.status_code == 404:
        return "not_found", None

    if user_response.status_code == 403:
        return "rate_limited", None

    repos_response = requests.get(repos_url, headers=headers)

    user_data = user_response.json()
    repos_data = repos_response.json()

    return user_data, repos_data