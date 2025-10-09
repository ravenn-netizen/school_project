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

#to create table 'student'
def createTableStudent():
    cmd="CREATE TABLE STUDENT(grno int primary key, name )"
    cursor.execute(cmd)

#to create table 'academic'
def createTableAcademic():
    cmd = "CREATE TABLE ACADEMIC(GRNO INT PRIMARY KEY, SUB1 FLOAT, SUB2 FLOAT, SUB3 FLOAT, SUB4 FLOAT, SUB5 FLOAT, AVG FLOAT, REMARKS"
    cursor.execute(cmd)



