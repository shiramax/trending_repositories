import shelve
import os

DB_FILE = 'repos.db'
def store_repo(repo):
    with shelve.open(DB_FILE, 'c') as shelf:
        shelf[repo["name"]] = repo


def store_repo_security_score(repo_name, security_score):
    with shelve.open(DB_FILE, 'c',  writeback=True) as shelf:
        nested_dict = shelf[repo_name]
        nested_dict['security_score'] = security_score
        shelf[repo_name] = nested_dict


def get_stored_repo(repo_name):
    with shelve.open(DB_FILE, 'r') as shelf:
        repo = shelf[repo_name]
    return repo


def stored_repos_names():
    with shelve.open(DB_FILE, 'r') as shelf:
        repos_names = list(shelf.keys())
    return repos_names


def repo_is_stored(repo):
    if repo["name"] in stored_repos_names():
        return True
    return False


def db_file_exists():
    return True if os.path.isfile(DB_FILE) else False

def store_repos(repos):
    for repo in repos:
        if db_file_exists():
            if repo_is_stored(repo):
                continue
        store_repo(repo)