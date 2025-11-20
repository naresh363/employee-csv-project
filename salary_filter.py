import csv
with open("employees.csv","r")as file:
    raeder=csv.DictReader(file)
    for row in raeder:
        if int(row['SALARY'])>18000:
            print(row)
