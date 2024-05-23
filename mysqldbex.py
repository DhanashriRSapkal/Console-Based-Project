'''
xampp / mysql commands to view the result:

mysql -u root
show databases;
create database employee;
create table itvedant(empID int, project_name varchar(20), location varchar(20));
create table mobile(ID int, brand varchar(20), features varchar(20));
use pydb;
show tables;
desc student;
select * from student 
Truncate table //clear the entries, keeping the fields and attributes
drop table // deletes the table 
'''

from mydbmodule import *

while 1:
    choice = int(input('''
1: > insert
2: > display
3: > delete
4: > update
5: > exit
1 to 5: '''))
    if choice == 1:
        ID = int(input("Enter ID: "))
        brand = input("Enter brand name: ")
        features = input("Enter features: ")
        t= (ID,brand,features)
        insert_data(t)
    elif choice == 2:
        res = display_data()
        for i in res:
            print(i)
    elif choice == 3:
        ID = int(input("Enter  ID: "))
        delete_data((ID))
    elif choice == 4:
        ID = int(input("Enter Employee ID: "))
        brand = input("Enter brand name: ")
        features = input("Enter features: ")
        update_data((brand,features,ID))
    elif choice == 5:
        break
    else:
        print("Invalid choice ")
