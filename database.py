#to establish python-sql connection

import mysql.connector as sql
db = sql.connect(host='localhost', user='root', passwd='****')
cursor = db.cursor()

#to create database
def createdb():
    cmd= "CREATE DATABASE SCHOOL"
    cursor.execute(cmd)
    cmd= "USE SCHOOL"
    cursor.execute(cmd)

#to create table 'STUDENT'
def createTableStudent():
    cmd= "USE SCHOOL"
    cursor.execute(cmd)
    cmd="CREATE TABLE STUDENT(STUDENT_ID INT PRIMARY KEY, NAME VARCHAR(200), DOB DATE, GENDER CHAR(1), AGE INT, GRADE INT, SECTION CHAR(1), STREAM CHAR(3), TRANSPORT VARCHAR(10), BUS_NO INT, BUS_STOP VARCHAR(40), GUARDIAN VARCHAR(60), TEL CHAR(8), EMAIL VARCHAR(30), ADDRESS VARCHAR(60) , CPR VARCHAR(9), PASSWORD VARCHAR(30))"
    cursor.execute(cmd)

#to create table 'ACADEMIC'
def createTableAcademic():
    cmd= "USE SCHOOL"
    cursor.execute(cmd)
    cmd = "CREATE TABLE ACADEMIC(SNO INT PRIMARY KEY, STUDENT_ID INT, TERM VARCHAR(6), SUB1 FLOAT, SUB2 FLOAT, SUB3 FLOAT, SUB4 FLOAT, SUB5 FLOAT, AVG FLOAT, REMARKS varchar(10) )"
    cursor.execute(cmd)

#to create table 'STAFF'
def createTableStaff():
    cmd= "USE SCHOOL"
    cursor.execute(cmd)
    cmd = "CREATE TABLE STAFF(STAFF_ID INT PRIMARY KEY, NAME VARCHAR(200), DEPARTMENT VARCHAR(20), CPR INT NOT NULL, PASSWORD VARCHAR(10))"
    cursor.execute(cmd)

#to create table 'ANNOUNCEMENT'
def createTableAnnouncements():
    cmd= "USE SCHOOL"
    cursor.execute(cmd)
    cmd = "CREATE TABLE ANNOUNCEMENT(REF INT PRIMARY KEY, SENDER INT, RECEIPIENT_TYPE varchar(20), RECEIPIENT varchar(20), DATE date, SUBJECT TEXT; CONTENT text)"
    cursor.execute(cmd)
