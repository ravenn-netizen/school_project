#to establish python-sql connection

import mysql.connector as sql
db = sql.connect(host='localhost', user='root', passwd='****',database='SCHOOL')
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
    cmd="CREATE TABLE STUDENT(STUDENT_ID VARCHAR(6) PRIMARY KEY, NAME VARCHAR(30), DOB DATE, GENDER CHAR(1), AGE INT, GRADE INT, SECTION CHAR(1), STREAM VARCHAR(10), TRANSPORT VARCHAR(10), BUS_NO INT, BUS_STOP VARCHAR(20), GUARDIAN VARCHAR(40), TEL CHAR(8), EMAIL VARCHAR(20), ADDRESS VARCHAR(60) , CPR VARCHAR(9))"
    cursor.execute(cmd)

#to create table 'ACADEMIC'
def createTableAcademic():
    cmd= "USE SCHOOL"
    cursor.execute(cmd)
    cmd = "CREATE TABLE ACADEMIC(STUDENTID VARCHAR(6) PRIMARY KEY, TERM VARCHAR(6), SUB1 FLOAT, SUB2 FLOAT, SUB3 FLOAT, SUB4 FLOAT, SUB5 FLOAT, AVG FLOAT, REMARKS varchar(10) )"
    cursor.execute(cmd)

#to create table 'STAFF'
def createTableStaff():
    cmd= "USE SCHOOL"
    cursor.execute(cmd)
    cmd = "CREATE TABLE STAFF(STAFFID INT PRIMARY KEY, NAME VARCHAR(30), DEPARTMENT VARCHAR(20), CPR INT NOT NULL, PASSWORD VARCHAR(10))"
    cursor.execute(cmd)

#to create table 'COMMUNICATION' for comm interface
def createTableAnnouncements():
    cmd= "USE SCHOOL"
    cursor.execute(cmd)
    cmd = "CREATE TABLE ANNOUNCEMENT(REF INT, SENDER varchar(20), RECEIPIENT_TYPE varchar(20), RECEIPIENT varchar(20), DATE date, CONTENT text)"
    cursor.execute(cmd)
