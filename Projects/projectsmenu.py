from Create_project import create_project
from Projects.View_projects import view_projects
from Edit_project import edit
from delete_project import delete
def proj_menu():
    print('''           welcome to dashboard          ''')

    print(''' 
    1-Create Project
    2-View Projects
    3-Edit projects
    4-Delete Project
    5-Search Project
    ''')
    choice=int(input("Enter from 1 to 5 "))
    if(choice==1):
       create_project()
    if choice==2:
       view_projects()
    if choice==3:
        edit()
    if choice==4:
        delete()
    proj_menu()
