import os

print('List Branch: ')
list_branch = input()
os.system("git checkout develop")

if type(list_branch) == str:
    list_branch = list_branch.split(",")

if list_branch:
    for branch in list_branch:
        os.system("git checkout develop")
        os.system("git push origin --delete UPY-#"+ str(branch))
        print("===== Delete branch UPY-#"+ str(branch))
