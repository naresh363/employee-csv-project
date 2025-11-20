import csv
with open("employees.csv","r")as f:
    reader=list(csv.DictReader(f))
    list1=[]
    for i in reader:
        count=0
        department=i['DEPARTMENT_ID']
        if department not in list1:
           for x in reader:
               if x['DEPARTMENT_ID']==department:
                  count=count+1
           list1.append(department)
           print("department", department,"count=",count)