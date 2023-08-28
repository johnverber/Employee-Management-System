import mysql.connector
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *


con = mysql.connector.connect(host="localhost", user="root", password="eden1981!", database="emp")

#function to check if employee with given id exists or not

def check_employee(employee_id):
    #query to select all rows from employee table
    sql = 'select * from emp where id=%s'

    #making cursor buffered to make rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    #executing the sql query
    c.execute(sql, data)

    #rowcount method to find number of rows with given values

    r = c.rowcount

    if r == 1:
        return True
    else:
        return False

#function to add employee

def Add_Employ():

    Id = input("Enter Employee Id : " )

    #checking if employe with given id exists or not
    if(check_employee(Id) == True):
        popup("Employee already exists\n Try again \n")
        menu()
    else:
        Name = input("Enter employee name: ")
        Post = input("Enter employee post: ")
        Salary = input("Enter employee salary: ")
        data = (Id, Name, Post, Salary)

        #inserting employee details into the employee table

        sql = 'insert into emp values(%s,%s,%s,%s)'
        c = con.cursor()

        #execusting the sql qwuery
        c.execute(sql, data)

        #commit() method to make changes to the table
        con.commit()
        popup("Employee successfully added")
        menu()

def Remove_Employ():
    Id = input("Enter employee id: ")

    #checking if employee with given id exists
    if(check_employee(Id) == False):
        popup("Employee does not exits\n Try again \n")
        menu()
    else:
        #quest to delete employee from table
        sql = 'delete from emp where id=%s'
        data = (Id,)
        c = con.cursor()

        #executing the sql quesy
        c.execute(sql, data)

        #commit() method to make changes in the table
        con.commit()
        popup("Employee removed")
        menu()

def Promote_Employee():
    Id = int(input("Enter Employees Id"))

    #checking to see if employee exists
    if(check_employee(Id) == False):
        popup("Employee doesn't exits \n Try again \n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))

        #Query to fetch salary of employee
        sql = 'select salary from emp where id=%s'
        data = (Id,)
        c = con.cursor()

        #executing the sql query
        c.execute(sql, data)

        #fetching the salary of employee with given id
        r = c.fetchone()
        t = r[0]+Amount
        #query to update salary of employee
        sql = 'update emp set salary=%s where id=%s'
        d = (t, Id)

        #executing the sql query
        c.execute(sql, d)

        #commit() method to make changes to the table
        con.commit()
        popup("Employee promoted")
        menu()

def Display_Employees():

    #query to select rows from employee table
    sql = 'select * from emp'
    c = con.cursor()

    #executing sql query
    c.execute(sql)

    #geting all details of the employees
    r = c.fetchall()
    for i in r:
        put_table([
        ["Employee Id : " , i[0]],
        ["Employee Name " , i[1]],
        ["Employee Post: ", i[2]],
        ["Employee Salary : ", i[3]],
        ])
    menu()



def menu():

    put_text("Welcome to the Employee Management Record System").style('font-size: 30px; font-weight: bold')
    put_button(['1 to Add Employee '], onclick=Add_Employ)
    put_button(['2 to Remove Employee'], onclick=Remove_Employ)
    put_button(['3 to Promote Employee'], onclick=Promote_Employee)
    put_button(['4 to Display Employees'], onclick=Display_Employees)
    put_button(['5 to exit'], onclick=exit)


        
        
menu()
