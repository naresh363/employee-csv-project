import csv
manager_id=input("Enter Manager ID: ")
with open("employees.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        if row['MANAGER_ID']==manager_id:
            print(row)