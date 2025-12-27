import os
import requests

GITHUB_PAT = os.getenv("GITHUB_PAT")
REPO = "gtpw689-commits/reimagry"
WORKFLOW = "gpt4all.yml"
PROMPT = "Hello GPT4All"

url = f"https://api.github.com/repos/{REPO}/actions/workflows/{WORKFLOW}/dispatches"
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {GITHUB_PAT}"
}
data = {"ref": "main", "inputs": {"prompt": PROMPT}}

r = requests.post(url, json=data, headers=headers)
print(r.status_code, r.text)
