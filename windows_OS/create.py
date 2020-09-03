import sys
import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

# Read Arguments
folder_name = str(sys.argv[1])
public_private = str(sys.argv[2])

# Load from .env
path = os.getenv('mp')
token = os.getenv('gt')
ide = os.getenv('ide')

# define new directory
_dir = path + '/' + folder_name

# GitHub connect + create Repository
g = Github(token)
user = g.get_user()
login = user.login

if (public_private == "private"):
    repo = user.create_repo(folder_name, private=True)
else:
    repo = user.create_repo(folder_name)

print(f'https://github.com/{login}/{folder_name}.git created')

commands = [
    f'echo # {repo.name} >> README.md',
    'git init',
    f'git remote add origin https://github.com/{login}/{folder_name}.git',
    'git add .',
    'git commit -m "Initial commit"',
    'git push -u origin master'
]

# Create a new directory and push to remote repository
os.mkdir(_dir)
os.chdir(_dir)

for c in commands:
    os.system(c)

print(f'{folder_name} created locally')
os.system(f'{ide} .')

