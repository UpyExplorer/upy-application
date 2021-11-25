import os

print('Branch: ')
branch = input()
os.system("git checkout develop")

if branch:
    os.system("git checkout UPY-#"+ str(branch))
    os.system("git pull")
