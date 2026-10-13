#Task 2: Read a CSV File
#python3 -m pytest -v -x assignment2-test.py

import csv

def read_employees():
    empty_dict = {}
    empty_list = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            first_row = True
            for row in reader:
                if first_row: 
                    empty_dict["fields"] = row
                    first_row = False
                else:
                    empty_list.append(row)
            
        empty_dict["rows"] = empty_list
        return empty_dict
            
    except Exception as e:
        print(e)

employees = read_employees()
print(employees)

#Task 3: Find the Column Index

def column_index(name):
    return employees["fields"].index(name)

employee_id_column = column_index("employee_id")
print(employee_id_column)

#Task 4: Find the Employee First Name
def first_name(row_number):
    return employees["rows"][row_number][column_index("first_name")]

#Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches



#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches



#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

print(sort_by_last_name())

#Task 8: Create a dict for an Employee
def employee_dict(row):
    fields = employees["fields"]
    result = {}
    for i in range(len(fields)):
        if fields[i] != "employee_id":
            result[fields[i]] = row[i]
    return result

print(employee_dict(employees["rows"][0]))

#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    all_employees = {}
    for row in employees["rows"]:
        all_employees[row[employee_id_column]] = employee_dict(row)
    return all_employees
   
#Task 10: Use the os Module
import os

def get_this_value():
    return os.getenv("THISVALUE")

#Task 11: Creating Your Own Module
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("hi")
print(custom_module.secret)

#Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    minutes1 ={}
    rows1=[]
    minutes2 ={}
    rows2 =[]

    try:
        with open("../csv/minutes1.csv", "r") as file:
            reader = csv.reader(file)
            first_row = True
            for row in reader:
                if first_row:
                    minutes1["fields"] = row
                    first_row = False
                else:
                    rows1.append(tuple(row))
        minutes1["rows"] = rows1

        with open("../csv/minutes2.csv", "r") as file:
            reader = csv.reader(file)
            first_row = True
            for row in reader:
                if first_row:
                    minutes2["fields"] = row
                    first_row = False
                else:
                    rows2.append(tuple(row))
        minutes2["rows"] = rows2
        return minutes1, minutes2

    except Exception as e:
        print(e)
minutes1, minutes2 = read_minutes()

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()

#Task 14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    minutes_list = list(minutes_set)
    converted = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)
    return list(converted)

minutes_list = create_minutes_list()

#Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key = lambda x: x[1])
    converted = list(map(lambda x: (x[0],  datetime.strftime(x[1], "%B %d, %Y")), minutes_list))

    with open("./minutes.csv", "w",) as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted)

    return converted

