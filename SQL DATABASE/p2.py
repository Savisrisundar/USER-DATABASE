#from asyncio.windows_events import NULL
from asyncio.windows_events import NULL
from logging import RootLogger
from multiprocessing.sharedctypes import Value
from optparse import Values
import tkinter as tk
from django.forms import NullBooleanField
import mysql.connector
from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
import sys
from numpy import roots
from tkcalendar import Calendar

db = mysql.connector.connect(host ="127.0.0.1", 
									user = "root",
									password = "Srihari1!",
									db ="employee")
def adds(FIRST1,LAST1,EMPID,AGE,CODE,SAL,DOB,DOJ,STAT):
	
	db = mysql.connector.connect(host ="127.0.0.1",
									user = "root",
									password = "Srihari1!",
									db ="employee")
	mycursor=db.cursor()
	if DOB == "":
		print("inside if")
		DOB=NULL
	sql1 = "INSERT INTO details (EMPID,AGE,FIRST_NAME, LAST_NAME,DEPT_CODE,SALARY,DOB,DOJ,STATUS) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	#sql1 = "INSERT INTO details (EMPID,AGE,FIRST_NAME, LAST_NAME,DEPT_CODE,SALARY,DOB,DOJ,STATUS) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	#sql="select * from details"
	print(FIRST1,LAST1,"Test1",DOB)
	usr = (EMPID,AGE,FIRST1,LAST1,CODE,SAL,DOB,DOJ,STAT)
	print(usr)
	mycursor.execute(sql1,usr)
	#mycursor.execute(sql)
	db.commit()
	myresult = mycursor.fetchall()
	print(myresult)
def updata(fn,ln,dc,sa,dob,doj,sta,ID1):
	db = mysql.connector.connect(host ="127.0.0.1",
									user = "root",
									password = "Srihari1!",
									db ="employee")
	mycursor=db.cursor()
	sql="update details set FIRST_NAME=%s , LAST_NAME=%s , DEPT_CODE=%s, SALARY=%s , DOB=%s , DOJ=%s , STATUS=%s where EMPID=%s"
	usr=(fn,ln,dc,sa,dob,doj,sta,ID1)
	mycursor.execute(sql,usr)
	db.commit()
	myresult=mycursor.fetchall()
	print(myresult)


def upscreen(myresult,ID1):
	root=tk.Tk()
	root.geometry("300x500")
	root.title("UPDATE DETAILS")
	c=0
	for i in myresult:
		c+=1
		print("value",i[2])
		fn = tk.Label(root, text="FIRST NAME:")
		fn.place(x = 50, y = 50)
		fn = tk.Entry(root, width = 35, textvariable=i[2])
		fn.insert(END,i[2])
		fn.place(x = 150, y = 50, width = 100)
		ln = tk.Label(root, text="LAST NAME:")
		ln.place(x = 50, y = 100)
		ln = tk.Entry(root, width = 35, textvariable=i[3])
		ln.insert(END,i[3])
		ln.place(x = 150, y = 100, width = 100)
		dc = tk.Label(root, text="DEPT CODE:")
		dc.place(x = 50, y = 150)
		dc = tk.Entry(root, width = 35, textvariable=i[4])
		dc.insert(END,i[4])
		dc.place(x = 150, y = 150, width = 100)
		sa = tk.Label(root, text="SALARY:")
		sa.place(x = 50, y = 200)
		sa = tk.Entry(root, width = 35, textvariable=i[5])
		sa.insert(END,i[5])
		sa.place(x = 150, y = 200, width = 100)
		dob = tk.Label(root, text="DOB:")
		dob.place(x = 50, y = 250)
		dob = tk.Entry(root, width = 35, textvariable=i[6])
		dob.insert(END,i[6])
		dob.place(x = 150, y = 250, width = 100)
		doj = tk.Label(root, text="DOJ:")
		doj.place(x = 50, y = 300)
		doj = tk.Entry(root, width = 35, textvariable=i[7])
		doj.insert(END,i[7])
		doj.place(x = 150, y = 300, width = 100)
		sta = tk.Label(root, text="STATUS:")
		sta.place(x = 50, y = 350)
		sta = tk.Entry(root, width = 35, textvariable=i[8])
		sta.insert(END,i[8])
		sta.place(x = 150, y = 350, width = 100)
		submitbtn = tk.Button(root, text ="Submit",
					bg ='pink', command = lambda:updata(fn.get(),ln.get(),dc.get(),sa.get(),dob.get(),doj.get(),sta.get(),ID1))
	submitbtn.place(x = 150, y = 470, width = 55) 
	print(c)
	root.mainloop()
		
		
		
		
		


def up_s1(ID1):
	db = mysql.connector.connect(host ="127.0.0.1",
									user = "root",
									password = "Srihari1!",
									db ="employee")
	mycursor=db.cursor()
	sql="select * from details where EMPID = %s"
	usr1=(ID1,)
	mycursor.execute(sql,usr1)
	##db.commit()
	myresult = mycursor.fetchall()
	print("myresult : ",myresult)
	print("_________________________")
	upscreen(myresult,ID1)

		

def search12(ID):
	root=tk.Tk()
	root.geometry("300x500")
	root.title("SEARCH")
	db = mysql.connector.connect(host ="127.0.0.1",
									user = "root",
									password = "Srihari1!",
									db ="employee")
	mycursor=db.cursor()
	sql="select * from details where EMPID = %s"
	usr1=(ID,)
	mycursor.execute(sql,usr1)
	##db.commit()
	myresult = mycursor.fetchall()
	for i in myresult:
		
		print("value",i[2])
		fn=tk.Label(root, text="First Name :")
		fn.place(x = 50, y = 50)
		fn = tk.Label(root, text=i[2])
		fn.place(x = 150, y = 50)
		fn=tk.Label(root, text="Last Name :")
		fn.place(x = 50, y = 100)
		ln = tk.Label(root, text=i[3])
		ln.place(x = 150, y = 100)
		fn=tk.Label(root, text="Dept Code :")
		fn.place(x = 50, y = 150)
		dc = tk.Label(root, text=i[4])
		dc.place(x = 150, y = 150)
		fn=tk.Label(root, text="Salary :")
		fn.place(x = 50, y = 200)
		sa = tk.Label(root, text=i[5])
		sa.place(x = 150, y = 200)
		fn=tk.Label(root, text="DOB :")
		fn.place(x = 50, y = 250)
		dob = tk.Label(root, text=i[6])
		dob.place(x = 150, y = 250)
		fn=tk.Label(root, text=" DOJ :")
		fn.place(x = 50, y = 300)
		doj = tk.Label(root, text=i[7])
		doj.place(x = 150, y = 300)
		fn=tk.Label(root, text="STATUS :")
		fn.place(x = 50, y = 350)
		sta = tk.Label(root, text=i[8])
		sta.place(x = 150, y = 350)
	print("myresult : ",myresult)
	print("_________________________")
	root.mainloop()


	





	
	

def search1():
	root=tk.Tk()
	root.geometry("300x300")
	root.title("SEARCH")
	loblfrstrow = tk.Label(root, text ="EMPID:", )
	loblfrstrow.place(x = 50, y = 70)
	ID = tk.Entry(root, width = 35)
	ID.place(x = 150, y = 70, width = 100)
	submitbtn = tk.Button(root, text ="Submit",
					bg ='pink', command = lambda:search12(ID.get()))
	submitbtn.place(x = 150, y = 135, width = 55)
	root.mainloop()
def updates1():
	root=tk.Tk()
	root.geometry("300x300")
	root.title("UPDATE")
	loblfrstrow = tk.Label(root, text ="EMPID:", )
	loblfrstrow.place(x = 50, y = 70)
	ID = tk.Entry(root, width = 35)
	ID.place(x = 150, y = 70, width = 100)
	submitbtn = tk.Button(root, text ="Submit",
					bg ='pink', command = lambda:up_s1(ID.get()))
	submitbtn.place(x = 150, y = 135, width = 55)

	root.mainloop()

def addwin1(): 
	
	root=tk.Tk()
	db = mysql.connector.connect(host ="127.0.0.1", 
									user = "root",
									password = "Srihari1!",
									db ="employee")
	mycursor=db.cursor()
	mycursor.execute("select empid from details")
	res=mycursor.fetchall()
	ID=res[-1][0]
	
	print("***************",ID)
	root.geometry("300x500")
	root.title("ADD")
	lblfrstrow = tk.Label(root, text ="FIRST NAME:", )
	lblfrstrow.place(x = 50, y = 20)
	FIRST = tk.Entry(root, width = 35)
	FIRST.place(x = 150, y = 20, width = 100)
	Qblfrstrow = tk.Label(root, text ="LAST NAME:", )
	Qblfrstrow.place(x = 50, y = 70)
	LAST = tk.Entry(root, width = 35)
	LAST.place(x = 150, y = 70, width = 100)
	iblfrstrow = tk.Label(root, text ="AGE:", )
	iblfrstrow.place(x = 50, y = 170)
	AGE = tk.Entry(root, width = 35)
	AGE.place(x = 150, y = 170, width = 100)
	Jblfrstrow = tk.Label(root, text ="DEPT_CODE:", )
	Jblfrstrow.place(x = 50, y = 220)
	CODE = tk.Entry(root, width = 35)
	CODE.place(x = 150, y = 220, width = 100)
	Kblfrstrow = tk.Label(root, text ="SALARY:", )
	Kblfrstrow.place(x = 50, y = 270)
	SAL = tk.Entry(root, width = 35)
	SAL.place(x = 150, y = 270, width = 100)
	Nblfrstrow = tk.Label(root, text ="DOB:", )
	Nblfrstrow.place(x = 50, y = 320)
	DOB = tk.Entry(root, width = 35)
	DOB.place(x = 150, y = 320, width = 100)
	Bblfrstrow = tk.Label(root, text ="DOJ:", )
	Bblfrstrow.place(x = 50, y = 370)
	DOJ = tk.Entry(root, width = 35)
	DOJ.place(x = 150, y = 370, width = 100)
	Ablfrstrow = tk.Label(root, text ="STATUS:", )
	Ablfrstrow.place(x = 50, y = 420)
	STAT = tk.Entry(root, width = 35)
	STAT.place(x = 150, y = 420, width = 100)
	print(FIRST.get(),"test")
	submitbtn = tk.Button(root, text ="Submit",
					bg ='pink', command = lambda:adds(FIRST.get(),LAST.get(),ID+1,AGE.get(),CODE.get(),SAL.get(),DOB.get(),DOJ.get(),STAT.get()))
	submitbtn.place(x = 150, y = 470, width = 55) 
	root.mainloop()

def add():
	
	addwin1()
    


def window1():
	
	root=tk.Tk()
	root.geometry("300x300")
	root.title("SCREEN-1")
	insert=tk.Button(root,text="INSERT",bg="pink",command=add)
	insert.place(x=100,y=50,width=55)
	update=tk.Button(root,text="UPDATE",bg="pink",command=updates1)
	update.place(x=100,y=100,width=55)
	search=tk.Button(root,text="SEARCH",bg="pink",command=search1)
	search.place(x=100,y=150,width=55)
    

	root.mainloop()
    
def win1():
	root.destroy()
	window1()
	

	

 

def submitact():	
	user = Username.get()
	passw = password.get()
	print("The name entered by you is {user} {passw}")
	logintodb(user, passw)



def exit1():
	root.destroy()

	


def logintodb(user, passw):	
    db = mysql.connector.connect(host ="127.0.0.1",
									user = "root",
									password = "Srihari1!",
									db ="employee")
    mycursor=db.cursor()
    sql = "select password from emp_det where USER= %s and password=%s"
    usr = (user,passw)
    mycursor.execute(sql,usr)
    myresult = mycursor.fetchall()
    print(myresult)
    if myresult == []:
        msg()

    else:
        win1()


					
def msg():
	messagebox.showerror("Error","Incorrect Credentials")    

    


root = tk.Tk()
root.geometry("300x300")
root.title("Employee Login Page")


# Defining the first row
lblfrstrow = tk.Label(root, text ="User -", )
lblfrstrow.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)

lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)

password = tk.Entry(root, width = 35,  show="*")
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(root, text ="Submit",
					bg ='pink', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)
logout=tk.Button(root,text="Exit",bg='pink',command=exit1)
logout.place(x=150,y=200,width=55)
root.mainloop()
