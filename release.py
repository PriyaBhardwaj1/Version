import subprocess
import os
from datetime import datetime
from github import Github

def bump_version():
    """ Bump the version using bumpversion tool. """
    try:
        # Use bumpversion to bump the version (could be patch, minor, major)
        subprocess.run(["bumpversion", "patch"], check=True)  # Change 'patch' to 'minor' or 'major'
        print("Version bumped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error bumping version: {e}")

def generate_changelog():
    """ Generate a changelog from git commits. """
    try:
        subprocess.run(["python", "generate_changelog.py"], check=True)
        print("Changelog generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating changelog: {e}")

def create_github_release():
    """ Create a GitHub release using the current version. """
    try:
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token:
            raise ValueError("GitHub token not set. Please set the GITHUB_TOKEN environment variable.")

        # Authenticate to GitHub
        g = Github(github_token)
        repo = g.get_repo("your_username/your_repo_name")

        # Get the current version from the latest Git tag
        version = subprocess.check_output(["git", "describe", "--tags"]).decode("utf-8").strip()

        # Create the release
        release = repo.create_git_release(
            tag=version,
            name=f"Release {version}",
            message=f"Release {version} - Changelog included.",
            draft=False,
            prerelease=False
        )
        print(f"Release {version} created successfully on GitHub.")
    except ValueError as e:
        print(f"ValueError: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Error in Git command: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    """ Main function to execute the release process. """
    bump_version()  # Bump the version
    generate_changelog()  # Generate the changelog
    create_github_release()  # Create the GitHub release

if __name__ == "__main__":
    main()
