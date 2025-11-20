import csv
from datetime import datetime
# given a date print details of employees who joined after that date
join_date=input("Enter Join Date (DD-MM-Y): ")
with open("employees.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        emp_join_date=datetime.strptime(row['HIRE_DATE'],'%d-%b-%y')
        input_date=datetime.strptime(join_date,'%d-%b-%y')
        if emp_join_date>input_date:
            print(row)