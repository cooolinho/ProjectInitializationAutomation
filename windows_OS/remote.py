from dotenv import load_dotenv
load_dotenv()

import sys
import os
from github import Github

folder_name = str(sys.argv[1])
path = os.getenv('mp')
token = os.getenv('gt')
ide = os.getenv('ide')
_dir = path + '/' + folder_name

g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(folder_name)

commands = [
    f'echo # {repo.name} >> README.md',
    'git init',
    f'git remote add origin https://github.com/{login}/{folder_name}.git',
    'git add .',
    'git commit -m "Initial commit"',
    'git push -u origin master'
]

os.mkdir(_dir)
os.chdir(_dir)

for c in commands:
    os.system(c)

print(f'{folder_name} created locally')
os.system(f'{ide} .')
