#to create database and tables 

import mysqlconnector as sql
db = sql.conect(host='localhost', user='root', passwd='****')
cursor = db.cursor()

def createdb():
  com= "CREATE DATABASE SCHOOL"
  cursor.execute(com)
  com= "USE SCHOOL"
  cursor.execute(com)

def createTableStudent():
  
