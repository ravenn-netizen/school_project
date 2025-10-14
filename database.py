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
    cmd="CREATE TABLE STUDENT(STUDENTID INT PRIMARY KEY, NAME VARCHAR(30), DOB DATE, GENDER CHAR(1), CLASS INT, SECTION CHAR(1), STREAM VARCHAR(10), TRANSPORT VARCHAR(10), BUS_NO INT, BUS_STOP VARCHAR(20), GUARDIAN VARCHAR(40), TEL INT, EMAIL VARCHAR(20), PO_BOX INT, ADDRESS DICT, CPR INT)"
    cursor.execute(cmd)

#to create table 'ACADEMIC'
def createTableAcademic():
    cmd = "CREATE TABLE ACADEMIC(STUDENTID INT PRIMARY KEY, SUB1 FLOAT, SUB2 FLOAT, SUB3 FLOAT, SUB4 FLOAT, SUB5 FLOAT, AVG FLOAT, REMARKS varchar(10) '''pass or fail'''"
    cursor.execute(cmd)

#to create table 'STAFF'
def createTableStaff():
    cmd = "CREATE TABLE STAFF(STAFFID INT PRIMARY KEY, NAME VARCHAR(30), DEPARTMENT VARCHAR(20), CPR INT DISTINCT)
    cursor.execute(cmd)
#to create table 'COMMUNICATION' for comm interface
def createTableCommunication():
    cursor.execute("USE DATABASE SCHOOL")
    cmd = "CREATE TABLE COMMUNICATION(REF INT PRIMARY KEY, SENDER INT, RECIPIENT INT, SENDER_TYPE CHAR(10), RECIPIENT_TYPE CHAR(10), CONTENT TEXT, DATE DATE)"
    # here using cpr for sender and recipient as their ids may clash but cpr is unique
    cursor.execute(cmd)
