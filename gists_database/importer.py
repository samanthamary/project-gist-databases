import requests

BASE_URL = 'https://api.github.com/users/{username}/gists'

def import_gists_to_database(db, username, commit=True):
    url = BASE_URL.format(username=username)
    resp = requests.get(url, params={'per_page': 100})
    if not resp.ok:
        raise requests.exceptions.HTTPError
    gists = resp.json()
    for gist in gists:
        params = (gist["id"],
                  gist["html_url"],
                  gist["git_pull_url"],
                  gist["git_push_url"],
                  gist["commits_url"],
                  gist["forks_url"],
                  gist["public"],
                  gist["created_at"],
                  gist["updated_at"],
                  gist["comments"],
                  gist["comments_url"])
        cursor = db.execute("""insert into gists (github_id, html_url, git_pull_url, 
        git_push_url, commits_url, forks_url, public, created_at, updated_at, comments, comments_url) VALUES 
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", params)
    if commit:
        db.commit()