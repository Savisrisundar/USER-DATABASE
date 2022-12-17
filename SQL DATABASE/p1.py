import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Srihari1!",
    database="employee")

mycursor=mydb.cursor()




mycursor.execute("insert emp_det(abc,frg) values(123,123)")