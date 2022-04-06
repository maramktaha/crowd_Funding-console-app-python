import json
import re


def Register (id):

    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_regex= r'\b^01[0125][0-9]{8}$\b'


    user={'id':id,'First Name':'','Last Name':'','Email':'','Password':'','phone':''}


    userfile=open('user.json','a')
    while True:
        firstname=input("Enter Your First Name ")
        if (firstname.isdigit() or not firstname.isspace()):
            user['First Name']=firstname
        else:
            print( "Please Enter a valid name")
            continue
        lastname=input("Enter Your last Name ")
        if (lastname.isdigit() or not lastname.isspace()):
            user['Last Name']=lastname
        else:
            print( "Please Enter a valid name")
            continue
        email=input("Wrte Your Email ")
        if(re.fullmatch(email_regex,email)):
            user['Email']=email
        else:
            continue
        password=input("Write your password ")
        if(len(password) > 8 ):
            user['Password']=password
        else:
            continue
        confirm=input("Confirm Your password ")
        if(confirm==user['Password']):
            user['Password']=confirm
        else:
            print("Enter the same password")
            continue
        phone=input("Enter Your Phone number ")
        if re.fullmatch(phone_regex, phone):
            user['phone']=phone
        else:
            print("Enter valid egyptian phone number")
            continue


        userfile.write(json.dumps(user))
        userfile.write("\n")
        userfile.close()

        return True






