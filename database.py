# import mysql.connector
# import pandas as pd

# mydb = mysql.connector.connect(host = "localhost",
#                                user = "root",database = "empl")
# cursor = mydb.cursor()

# # cursor.execute("Create database empl;")
# # cursor.execute("Use empl")
# # p=cursor.execute("create table emp_details(user_id varchar(10),password varchar(20),emp_role int,primary key(user_id))")
# # q=cursor.execute("Insert into emp_details values('hr_1','1235',2)")
# # r=cursor.execute("Insert into emp_details values('mgr_1','1275',1)")
# # mydb.commit()
# def execute(str1):
#     cursor.execute(str1)
#     p= pd.DataFrame(cursor.fetchall(),columns=[i[0] for i in cursor.description])
#     return p
import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="password",
    database="empl"
)
c = mydb.cursor()

def auth(u_id,password):
    # print(u_id)
    c.execute(f"select * from emp_details where user_id = '{u_id}'")
    res = c.fetchall()
    if res == []:
        st.info("Check your user id and password")
        return 0,None
    else :
        if password == res[0][1]:
            #correct auth
            return 1,res[0][2]
        else :
            st.info("Invalid Password!")
            return 0,None
        
def execute_cmd(str1):
    try:
        c.execute(str1)
        mydb.commit()
    except Exception as e:
        st.info(e)
        st.error("Entered information is incomplete!Please fill all the fields since they are important")
        
def get_name_e(eid):
    c.execute(f"select e_name from employee where eid='{eid}'")
    res = c.fetchall()
    return res[0][0]
    
def get_name_m(mid):
    c.execute(f"select m_name from manager where m_id='{mid}'")
    res = c.fetchall()
    return res[0][0]

def get_first_column(res):
    arr=[]
    for i in range(len(res)):
        arr.append(res[i][0])
    
    return arr
def show_employees(m_id):
    # print(u_id)
    
    c.execute(f"select eid from employee where manager_id = '{m_id}'")
    res = c.fetchall()
    res=get_first_column(res)
    
    return res

def get_emp_details(e_id):
    # print(u_id)
  
    c.execute(f"select e_name,eid,mail_id,ph_no from employee where eid = '{e_id}'")
    res = c.fetchall()
    
    return res[0]

def get_mgr_Ids():
    c.execute(f"select m_id from manager")
    res = c.fetchall()
    res=get_first_column(res)

    return res

def get_mgr_details(m_id):
    c.execute(f"select m_name,m_id,mail_id,ph_no from manager where m_id = '{m_id}'")
    res = c.fetchall()
    
    return res[0]

def get_emp_resp_details(e_id):
    # print(u_id)
  
    c.execute(f"select no_of_task_assigned,no_of_task_completed,no_of_hrs_saved,no_of_defects_found,no_of_defects_fixed,additional_accomplishments from emp_resp where eid = '{e_id}'")
    res = c.fetchall()
    
    return res[0]

    
    
