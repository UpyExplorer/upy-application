import os

print('List Branch: ')
list_branch = input()

print('Merge Branch: ')
merge = input()

os.system("git checkout develop")

if type(list_branch) == str:
    list_branch = list_branch.split(",")

if list_branch:
    for branch in list_branch:
        os.system("git checkout UPY-#"+ str(branch))
        os.system("git pull")
        os.system("git merge " +str(merge))
        os.system("git push")
