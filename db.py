import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="password",
    database="empl"
)
c = mydb.cursor()

# def auth(u_id,password):
    # print(u_id)
u_id= 'mgr_2'
c.execute(f"select * from emp_details where user_id = '{u_id}'")
res = c.fetchall()
print(res)
if res == []:
    print('j')
    