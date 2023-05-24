#!/usr/bin/env python3
import http.client
import os

import requests

def enable_workflows():
    pat = os.environ['PERSONAL_ACCESS_TOKEN']

    session = requests.Session()
    session.headers["Accept"] = "application/vnd.github+json"
    session.headers["Authorization"] = f"Bearer {pat}"
    session.headers["X-GitHub-Api-Version"] = "2022-11-28"

    with open('workflows.txt') as f:
        workflows = f.read().strip().splitlines()

    for w in workflows:
        url = f'{w}/enable'
        print(f'PUT {url}')
        r = session.put(url)
        print(f'> {r.status_code} {http.client.responses.get(r.status_code, "???")}')
        for hn, hv in r.headers.items():
          print(f'> {hn}: {hv}')
        print('>')
        if not (response_text_lines := r.text.strip().splitlines()):
          print('> [NO BODY]')
        for line in response_text_lines:
          print(f'> {line}')


if __name__ == '__main__':
    enable_workflows()
