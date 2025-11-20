#All Employees Salary Calculation 
import csv
from datetime import datetime
with open("employees.csv","r")as f:
    reader=csv.DictReader(f)
    present_date=datetime.strptime("01-FEB-09","%d-%b-%y")
    for i in reader:
          hire_date=datetime.strptime(i['HIRE_DATE'],'%d-%b-%y')
          salary=int(i['SALARY'])
          sal=salary/30
          diff=present_date-hire_date
          days=abs(diff.days)
          print(i['FIRST_NAME'],    i['LAST_NAME'],"salary is",days*sal)