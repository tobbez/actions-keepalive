#!/usr/bin/env python3
import argparse
import os

import requests

class App:
    def __init__(self):
        pat = os.environ['PERSONAL_ACCESS_TOKEN']
        self.s = requests.Session()

        self.s.headers["Accept"] = "application/vnd.github+json"
        self.s.headers["Authorization"] = f"Bearer {pat}"
        self.s.headers["X-GitHub-Api-Version"] = "2022-11-28"

    def get_repos(self):
        r = self.s.get('https://api.github.com/user/repos')
        r.raise_for_status()
        return r.json()

    def get_workflows(self, repo):
        r = self.s.get(f'https://api.github.com/repos/{repo}/actions/workflows')
        r.raise_for_status()
        return r.json()['workflows']

    def run(self):
        ap = argparse.ArgumentParser()
        ap.add_argument('repo', nargs='*')
        args = ap.parse_args()

        if args.repo:
            repos = args.repo
        else:
            repos = [r['full_name'] for r in self.get_repos()]

        for r in repos:
            workflows = self.get_workflows(r)
            if workflows:
                print(f'{r}:')
                for w in workflows:
                    url, name = w['url'], w['name']
                    print(f'  {url} {name}')



if __name__ == '__main__':
    App().run()
