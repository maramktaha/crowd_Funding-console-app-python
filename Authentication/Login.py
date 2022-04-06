import json
from Projects.projectsmenu import proj_menu
def Login():
    fileusers=open('user.json','r')
    users=fileusers.readlines()
    email= input("Enter Your Email ")
    password = input("Enter Your Password ")

    for user in users:
        user=json.loads(user)
        if(email==user['Email'] and password==user['Password']):
            return proj_menu()
    print("Invalid credentials please login again")

