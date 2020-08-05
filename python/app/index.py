import mysql.connector
from flask import Flask 
from faker import Faker
fake = Faker()
host = "mysql"
user = "root"
password = "supersecret"
database = "mydatabase"
# table= "employees"

def create_db():
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE mydatabase")

def create_table():
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE employees (name VARCHAR(255), address VARCHAR(255))")
    sql = "INSERT INTO employees (name, address) VALUES (%s, %s)"
    for _ in range(10):
        val = (fake.name(), fake.address())
        mycursor.execute(sql, val)
    mydb.commit()

app=Flask(__name__)
@app.route('/')
def instruction():
        return "/init to initialize db, /list to list the content, /flush to clear database"

@app.route('/init')
def initialize():
    create_db()
    create_table()
    return "Initialized! Go to /list for the content"

@app.route('/list')
def list_employees():
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM employees")
    myresult = mycursor.fetchall()
    listToStr = ' '.join(map(str, myresult))
    return "List of Employees :"+ listToStr

@app.route('/flush')
def delete_database():
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
    mycursor = mydb.cursor()
    sql = "DROP DATABASE mydatabase"
    mycursor.execute(sql)
    return "Database Cleared"

app.run(host="0.0.0.0",port=5000)
