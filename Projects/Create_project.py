from datetime import datetime
import json
def create_project():
    format = "%d-%m-%Y"
    project={'Title':'','Details':'','Total_target':'','start Campaign':'','End Campaign':''}
    projectfile = open('project.json', 'a')

    while True:
        Proj_title = input("Enter Your Project Title ")
        project['Title']= Proj_title
        details = input("Enter Your Project Details ")
        project['Details']=details
        total_target = input("Enter Your Project Target ")
        project['Total_target']=f"{total_target} EGP"
        start_campain = input("Enter Start Date for the campain ")
        if(bool(datetime.strptime(start_campain, format))):
            project['start Campaign']=start_campain
        else:
           print("Enter valid date")
           continue
        end_campain = input("Enter Start Date for the campain ")
        if (bool(datetime.strptime(end_campain, format))):
            project['End Campaign']=end_campain
        else:
            print("Enter valid date")
            continue

        projectfile.write(json.dumps(project))
        projectfile.write("\n")
        projectfile.close()

        return True