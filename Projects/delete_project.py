import json
def delete():
    fileproject=open('project.json', 'r')
    title=input('Enter Title of project you want to delete ')
    projects=fileproject.readlines()
    # for proj in projects:
    #     proj = json.loads(proj)
    #     if title == proj['Title']:
    #

    for number, line in enumerate(fileproject):
        line=json.loads(line)
        data=line.get('Title')
        if title==line['Title']:
            line_number=number
            print(number)
            del projects[line_number]
            break
        fileproject.close()

    new=open('project.json', 'w+')
    for proj in projects:
        new.write(proj)

    new.close()


delete()