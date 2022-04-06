import json
def edit():
    fileproject=open('project.json', 'r')
    projects=fileproject.readlines()
    title=input('Enter Title of project you want to edit on')
    for proj in projects:
        proj = json.loads(proj)
        if title == proj['Title']:
            key=input("What field you want to edit on? ")
            new=input("Enter new data ")
            proj[key]=new

    return "This title doesn't exist"


