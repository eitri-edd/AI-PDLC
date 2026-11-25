#!/usr/bin/env python3
"""Patch only artifact discovery in actions/deploy-pages v5.0.1 (MIT license).

The official action metadata and bundled code are verified before modification.
"""
import hashlib
from pathlib import Path
import sys

BUNDLE_SHA256 = "63fd34d89cd23d8848618a019f978f2225880a38afe2328e6e7d72f20fc44e89"
ACTION_SHA256 = "64c44539fba53559a157b5de16c01d3ab91dbc999c1b98b5c0b2fc3528d5d059"
ORIGINAL = b"""    let response
    try {
      const twirpResponse = await artifactClient.listArtifacts()
      response = wrapTwirpResponseLikeOctokit(twirpResponse, requestOptions)
    } catch (twirpError) {
      core.error('Listing artifact metadata failed', twirpError)
      const octokitError = wrapTwirpErrorLikeOctokit(twirpError, requestOptions)
      throw octokitError
    }

    const filteredArtifacts = response.data.artifacts.filter(artifact => artifact.name === artifactName)
"""
REPLACEMENT = b"""    let filteredArtifacts
    for (let attempt = 1; attempt <= 12; attempt++) {
      let response
      try {
        const twirpResponse = await artifactClient.listArtifacts()
        response = wrapTwirpResponseLikeOctokit(twirpResponse, requestOptions)
      } catch (twirpError) {
        core.error('Listing artifact metadata failed', twirpError)
        const octokitError = wrapTwirpErrorLikeOctokit(twirpError, requestOptions)
        throw octokitError
      }
      filteredArtifacts = response.data.artifacts.filter(artifact => artifact.name === artifactName)
      // Retry zero matches only. Duplicates and errors fail through unchanged.
      if (filteredArtifacts.length !== 0 || attempt === 12) break
      core.info(`No matching Pages artifact on attempt ${attempt}; retrying lookup`)
      await new Promise(resolve => setTimeout(resolve, 5000))
    }
"""


def patch_bundle(data, expected_sha256):
    if hashlib.sha256(data).hexdigest() != expected_sha256:
        raise ValueError("deploy-pages bundle SHA-256 mismatch")
    if data.count(ORIGINAL) != 1:
        raise ValueError("expected exactly one original artifact lookup")
    return data.replace(ORIGINAL, REPLACEMENT, 1)


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: patch_deploy_pages.py ACTION_DIRECTORY")
    directory = Path(sys.argv[1])
    metadata = (directory / "action.yml").read_bytes()
    if hashlib.sha256(metadata).hexdigest() != ACTION_SHA256:
        raise ValueError("deploy-pages action.yml SHA-256 mismatch")
    bundle = directory / "dist/index.js"
    modified = patch_bundle(bundle.read_bytes(), BUNDLE_SHA256)
    bundle.write_bytes(modified)


if __name__ == "__main__":
    main()
