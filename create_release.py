import os
from github import Github
import subprocess
from dotenv import load_dotenv

def create_github_release():
    """
    Create a GitHub release using the latest git tag.
    """
    try:
        # Load environment variables from .env file
        load_dotenv()

        # Get GitHub token, username, and repo name from environment variables
        github_token = os.getenv("GITHUB_TOKEN")
        github_username = os.getenv("GITHUB_USERNAME")
        github_repo_name = os.getenv("GITHUB_REPO_NAME")

        if not github_token or not github_username or not github_repo_name:
            raise ValueError("GitHub token, username, or repo name not set. Please set them in the .env file.")

        # Authenticate to GitHub
        g = Github(github_token)

        # Get the repo object using the username and repo name from the .env file
        repo = g.get_repo(f"{github_username}/{github_repo_name}")

        # Get the current version from the latest Git tag
        version = subprocess.check_output(["git", "describe", "--tags"]).decode("utf-8").strip()

        # Create a GitHub release
        release = repo.create_git_release(
            tag=version,
            name=f"Release {version}",
            message=f"Release {version} - Detailed changelog here.",
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

if __name__ == "__main__":
    create_github_release()