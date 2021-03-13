# TODO:
# README file
# Requirments file

import repo_security_score
import repo_store
from gtrending import fetch_repos
from rich.table import Table
from rich.console import Console
import sys

import logging
logging.basicConfig(
    filename='trending_repositories.log',
    encoding='utf-8', level=logging.INFO,
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s'
)


def get_stars_and_forks(repo):
    """
    Formatting repo starts and forks
    :param repo: repo
    :return: formatted string of repo stats
    """
    stats = ""
    stats += f"{repo['stars']} ⭐ " if repo['stars'] else ""
    stats += f"{repo['forks']} ⎇ " if repo['forks'] else ""
    return stats


def calc_repos_security_score(repos):
    """
    Run find missing requirements if repo was changed or
    if the security code is not stored already
    :param repos: repos
    """
    for repo in repos:
        stored_repo = repo_store.get_stored_repo(repo["name"])
        is_changed = repo_security_score.clone_repo(stored_repo)
        if is_changed or "security_score" not in stored_repo.keys():
            security_score = str(repo_security_score.run_find_missing_reqs(stored_repo))
            repo_store.store_repo_security_score(repo["name"], security_score)


def print_repos_in_list(repos):
    """
    Print in a Table format the repos in the list.
    :param repos: repos
    """
    table = Table(leading=1)
    table.add_column("Name", style="bold cyan")
    table.add_column("Description", style="green")
    table.add_column("Stars and Forks", style="magenta")
    table.add_column("Security Score", style="red")

    for repo in repos:
        stored_repo = repo_store.get_stored_repo(repo["name"])
        stats = get_stars_and_forks(stored_repo)
        if not stored_repo["description"]:  # same here
            stored_repo["description"] = "None"

        table.add_row(
            stored_repo["name"],
            stored_repo["description"],
            stats,
            stored_repo["security_score"]
        )
        console = Console()
    console.print(table)


def get_count():
    if not sys.argv[1]:
        raise Exception("Expecting a count input")
    return sys.argv[1]


def verify_count():
    try:
        return int(sys.argv[1])
    except ValueError:
        raise Exception("Wrong input number, expected int value")


def main():
    count = get_count()
    verify_count()
    repos = fetch_repos('python')[0:int(count)]
    repo_store.store_repos(repos)
    calc_repos_security_score(repos)
    print_repos_in_list(repos)


if __name__ == "__main__":
    main()
