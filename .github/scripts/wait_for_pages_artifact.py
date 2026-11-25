"""Wait until the Pages artifact is visible to deploy-pages's artifact API."""

import base64
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request


ARTIFACT_NAME = "github-pages"
LIST_ARTIFACTS_PATH = "/twirp/github.actions.results.api.v1.ArtifactService/ListArtifacts"
ATTEMPTS = 12
DELAY_SECONDS = 5


def backend_ids(runtime_token):
    """Read the workflow and job backend IDs from the Actions runtime JWT."""
    try:
        payload = runtime_token.split(".")[1]
        payload += "=" * (-len(payload) % 4)
        claims = json.loads(base64.urlsafe_b64decode(payload))
    except (IndexError, ValueError, json.JSONDecodeError) as error:
        raise ValueError("ACTIONS_RUNTIME_TOKEN is not a valid JWT") from error
    for scope in claims.get("scp", "").split():
        parts = scope.split(":")
        if len(parts) == 3 and parts[0] == "Actions.Results":
            return parts[1], parts[2]
    raise ValueError("ACTIONS_RUNTIME_TOKEN has no Actions.Results scope")


def list_artifacts(runtime_token, results_url):
    run_id, job_id = backend_ids(runtime_token)
    origin_parts = urllib.parse.urlsplit(results_url)
    origin = f"{origin_parts.scheme}://{origin_parts.netloc}"
    request = urllib.request.Request(
        origin + LIST_ARTIFACTS_PATH,
        data=json.dumps({
            "workflowRunBackendId": run_id,
            "workflowJobRunBackendId": job_id,
        }).encode(),
        headers={
            "Authorization": f"Bearer {runtime_token}",
            "Content-Type": "application/json",
            "User-Agent": "AI-PDLC-Pages-artifact-check",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.load(response).get("artifacts", [])


def main():
    runtime_token = os.environ["ACTIONS_RUNTIME_TOKEN"]
    results_url = os.environ["ACTIONS_RESULTS_URL"]
    for attempt in range(1, ATTEMPTS + 1):
        try:
            artifacts = list_artifacts(runtime_token, results_url)
        except (OSError, ValueError, urllib.error.URLError) as error:
            print(f"Artifact API attempt {attempt} failed with {type(error).__name__}; retrying.")
        else:
            count = sum(artifact.get("name") == ARTIFACT_NAME for artifact in artifacts)
            if count == 1:
                print(f"{ARTIFACT_NAME} is visible to the deployment artifact API.")
                return
            print(f"Artifact API attempt {attempt} found {count} {ARTIFACT_NAME} artifact(s); retrying.")
        if attempt < ATTEMPTS:
            time.sleep(DELAY_SECONDS)
    raise TimeoutError(f"{ARTIFACT_NAME} was not visible to the deployment artifact API after {ATTEMPTS * DELAY_SECONDS} seconds")


if __name__ == "__main__":
    main()
