import requests
import time
import os

GITHUB_PAT = os.getenv("GITHUB_PAT")

class GPT4AllBackend:
    def __init__(self, repo="gtpw689-commits/reimagry", workflow="gpt4all.yml", token=None):
        self.repo = repo
        self.workflow = workflow
        self.token = token
        self.api_url = f"https://api.github.com/repos/{self.repo}/actions/workflows/{self.workflow}/dispatches"

    def chat(self, prompt):
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"token {self.token}"
        }
        payload = {
            "ref": "main",
            "inputs": {"prompt": prompt}
        }

        # Trigger workflow
        r = requests.post(self.api_url, json=payload, headers=headers)
        if r.status_code != 204:
            return f"Error triggering workflow: {r.status_code} {r.text}"

        # Wait and fetch the last workflow run
        time.sleep(5)  # small delay
        runs_url = f"https://api.github.com/repos/{self.repo}/actions/workflows/{self.workflow}/runs"
        runs = requests.get(runs_url, headers=headers).json()
        if "workflow_runs" not in runs or len(runs["workflow_runs"]) == 0:
            return "No workflow runs found"

        latest_run_id = runs["workflow_runs"][0]["id"]
        jobs_url = f"https://api.github.com/repos/{self.repo}/actions/runs/{latest_run_id}/jobs"
        jobs = requests.get(jobs_url, headers=headers).json()

        # Get output from the first step
        try:
            output_url = jobs["jobs"][0]["steps"][-1]["outputs"].get("response", "")
            return output_url
        except Exception as e:
            return f"Error fetching workflow output: {str(e)}"
