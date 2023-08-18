import mysql.connector

dbobj = mysql.connector.connect(user="root", host="localhost", password="Gmailsid2211", charset="utf8")
cobj = dbobj.cursor()

cobj.execute("create database polisysrms")
cobj.execute("use polisysrms")
cobj.execute("Create table criminalrec(Case_ID varchar(45) primary key, Criminal_Number varchar(10), criminal_name "
             "varchar(50),date_of_arrest varchar(12), date_of_crime varchar(12), address varchar(50), age  varchar(3), "
             "occupation  varchar(50), birthmark varchar(45), crime_type   varchar(40), father_name  varchar(50), "
             "gender varchar(10), wanted varchar(5))")
cobj.execute("Create table registeruser(fname varchar(45), lname varchar(45), contact int, email varchar(200), "
             "ssq varchar(100), ssa varchar(100), password varchar(20))")

dbobj.commit()
dbobj.close()
