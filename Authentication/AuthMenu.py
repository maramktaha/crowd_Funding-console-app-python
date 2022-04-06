from Register import Register
from Login import Login
import json
import os
def menu():
    file='user.json'
    if(os.path.getsize(file)==0):
        id=1
    else:
        userfile=open('user.json','r')
        last_line=json.loads(userfile.readlines(0)[-1])
        id=last_line['id']+1

    print(''' Please choose an option
     1- Register 
     2-Login
    ''')
    option=int(input("option: "))
    if(option==1):

        Register(id)
    else:
        Login()

menu()