import opts
from git import Repo
import logging
import os
from pip_check_reqs import find_extra_reqs
import glob

GIT_REPO_SUFFIX = ".git"
REPO_DIR = "repos"
REQUIREMENTS_FILE = "requirements.txt"
CURRENT_DIR = os.getcwd()
PYTHON_SUFFIX = ".py"


def get_repo_path(repo):
    """
    Get full repo path
    :param repo: repo
    :return: repo path
    """
    repo_path = os.path.join(REPO_DIR, repo["name"])
    return repo_path


def git_pull(git_dir):
    """
    Perform git pull on git dir.
    :param git_dir: git dir
    :return: True if repo was changed, False otherwise
    """
    repo = Repo(git_dir)
    current = repo.head.commit
    repo.remotes.origin.pull()
    if current != repo.head.commit:
        return True
    else:
        return False


def clone_repo(repo):
    """
    Clone repo, if the repo already clone, git pull
    :param repo: repo to clone
    :return:
    """
    url = repo["url"] + GIT_REPO_SUFFIX
    path = get_repo_path(repo)
    if os.path.isdir(path):
        logging.warning(f"Git repo {repo['name']} exists, running git pull")
        is_changed = git_pull(path)
        return is_changed
    else:
        logging.info(f"Cloning {url} to {path}")
        Repo.clone_from(url, path)
        return True


def requirements_file_in_repo(path):
    """
    Get the requirements file
    :return: requirements file
    """
    if os.path.isdir(path):
        repo_path = path
    else:
        repo_path = os.path.dirname(path)

    path = repo_path +  r'/**/*' + REQUIREMENTS_FILE
    files = glob.glob(path, recursive=True)
    if len(files) >= 1:
        return files
    elif len(files) == 0:
        raise Exception("No requirements file found")

def run_find_extra_reqs(paths, req_filename):
    """
    run_find_extra_reqs
    :param path: list of files to run on or repo folder
    :return: results
    """
    try:
        result = find_extra_reqs.find_extra_reqs(
            options=opts.options(paths, req_filename),
            requirements_filename=req_filename
        )
        logging.info(f"Result: {result} for : {paths}, req file: {req_filename}")
        return result
    except Exception as e:
        logging.warning(f"Failed to get security score from {paths} , req file: {req_filename} due to: {e}")
        return []

def run_find_missing_reqs(repo):
    """
    Calculate security score by summing the count of
    missing requirements in the repo.
    :param repo: repo
    :return: security_score, if for some reason
    (requirements file is missing or Exception) the security score will be 0
    """
    repo_path = get_repo_path(repo)
    result = []
    try:
        req_filenames = requirements_file_in_repo(repo_path)
        for file in req_filenames:
            path = os.path.dirname(file)
            packages = run_find_extra_reqs([path], file)
            for package in packages:
                if package not in result:
                    result.append(package)
    except Exception as e:
        logging.error(e)
    return len(result)


