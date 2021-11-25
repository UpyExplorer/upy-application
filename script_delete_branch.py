import os

print('List Branch: ')
list_branch = input()
os.system("git checkout develop")

if list_branch:
    for branch in list_branch:
        os.system("git checkout develop")
        os.system("git push origin --delete UPY-#"+ str(branch))
        print("===== Delete branch UPY-#"+ str(branch))
