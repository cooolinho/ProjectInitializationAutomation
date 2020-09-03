from dotenv import load_dotenv
load_dotenv()

import sys
import os

folder_name = str(sys.argv[1])
path = os.getenv('mp')
ide = os.getenv('ide')
_url = path + '/' + folder_name

try:
    os.mkdir(_url)
    os.chdir(_url)
    os.system('git init')
    os.system(f'echo "# {folder_name}" > README.md')
    os.system('git add README.md')
    os.system('git commit -m "first commit"')

    print(f'{folder_name} created locally')
    os.system(f'{ide} .')

except:
    print("create <project_name> l")
