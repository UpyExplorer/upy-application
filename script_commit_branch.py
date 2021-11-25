import os

print('Branch: ')
branch = input()

print('Description: ')
description = input()

os.system("git checkout develop")

if branch and description:
    os.system("git stash")
    os.system("git checkout UPY-#"+ str(branch))
    os.system("git pull")
    os.system("git stash apply")
    os.system("git add .")
    os.system("git commit -m 'UPY-#"+ str(branch) + " - " + str(description) + "'")
    os.system("git push")
