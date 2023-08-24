import requests

def search_public_repositories(owner):
    url = f"https://api.github.com/users/{owner}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        repositories = response.json()
        clone_urls = [repository["clone_url"] for repository in repositories]
        return clone_urls
    else:
        print(f"Failed to retrieve repositories. Error: {response.status_code}")
        return []

# Example usage
# clone_urls = search_public_repositories("Aransh")
# print(clone_urls)