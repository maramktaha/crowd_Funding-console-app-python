def view_projects():
    projectfile=open('project.json', 'r')
    print(projectfile.readlines())