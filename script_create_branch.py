import os

print('List Branch: ')
list_branch = input()
os.system("git checkout develop")

if list_branch:
    for branch in list_branch:
        os.system("git checkout -b UPY-#"+ str(branch))
        os.system("git push --set-upstream origin UPY-#"+ str(branch))
        os.system("git checkout develop")
        print("===== Create branch UPY-#"+ str(branch))
