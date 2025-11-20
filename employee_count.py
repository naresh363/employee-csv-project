import csv
with open("employees.csv","r")as file:
    reader=list(csv.DictReader(file))
    deparatment_id=input("Enter Department ID: ")
    employee_count=0
    manager_count=0
    list1=[]
    for row in reader:
        if row['DEPARTMENT_ID']==deparatment_id:
            employee_count+=1
            if row['MANAGER_ID'] not in list1:
               if row['MANAGER_ID']!='-':
                manager_count+=1
                list1.append(row['MANAGER_ID'])
    print("Total Employees:",employee_count)
    print("Total Managers:",manager_count)