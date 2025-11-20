import csv
with open("employees.csv","r")as file:
    reader=csv.DictReader(file)
    employee_id=input("Enter Employee ID: ")
    for row in reader:
        if row['EMPLOYEE_ID']==employee_id:
            print( row['DEPARTMENT_ID'])
            manager_id=row['MANAGER_ID']
    for row in reader:
        if row['EMPLOYEE_ID']==manager_id:
            print(row['FIRST_NAME'],row['LAST_NAME'])