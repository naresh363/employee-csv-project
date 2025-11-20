#given an employee id how much salary he will get till now
import csv
from datetime import datetime
employee_id=input("Enter Employee ID: ")
present_date=input("Enter Present Date (DD-MM-Y): ")
with open("employees.csv","r")as file:
    reader=csv.DictReader(file)
    for i in reader:
       if i['EMPLOYEE_ID']==employee_id:
          hire_date=datetime.strptime(i['HIRE_DATE'],'%d-%b-%y')
          salary=int(i['SALARY'])
          sal=salary/30
          present_date=datetime.strptime(present_date,'%d-%b-%y')

          diff=present_date-hire_date
          days=abs(diff.days)
          print(i['FIRST_NAME'],    i['LAST_NAME'],"salary is",days*sal)
