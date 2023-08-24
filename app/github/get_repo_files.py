import requests
import base64
import os
import sys


token = os.getenv("GLOBAL_CICD_GIT_TOKEN")
headers = {
    # "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

def parse_dir():


def create_tree(json_res):
    pass


def get_file_from_github(repo: str) -> None:
    api_url = f"https://api.github.com/repos/{repo}/contents"
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        tree = create_tree(response.json())

    else:
        print("Error fetching the files:", response.status_code, response.text)


if __name__ == '__main__':
    tree = {}
    REPO = "AmosElitzur1/skygen"
    path = ""
    get_file_from_github(REPO)