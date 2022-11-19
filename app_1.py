import streamlit as st
from manager_UI import M_UI
from HR_UI import H_UI
from Employee_UI import E_UI
# from login import show_login_page,login_clicked,show_logout_page,LogOut_Clicked
# from database import Authenticate

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)


c1, c2,c3,c4,c5 = st.columns(5)
f1,f2,f3 = st.columns(3)    

def show_login_page():
    if st.session_state['loggedIn']==False:
        with f2: 
            with st.form('login'):
                    user_id=st.text_input(label="",value="",placeholder="User ID")  
                    password=st.text_input(label="",value="",placeholder="Password",type="password")
                    st.form_submit_button("Login",on_click=login_clicked,args=(user_id,password))



def login_clicked(user_id,password):
    # var=Authenticate(user_id,password)
    var = 1
    if var: 
        st.session_state['loggedIn']=True
    else:
        st.session_state['loggedIn']==False
        st.error("Invalid User")
def show_logout_page():
    st.button("LogOut",on_click=LogOut_Clicked)

def LogOut_Clicked():
    st.session_state['loggedIn']=False
with c3:
    st.header("APPRAISER")
if 'loggedIn' not in st.session_state:
    st.session_state['loggedIn']=False
    show_login_page()
else:
    if st.session_state['loggedIn']:
        a = 2
        if a==1 :
            M_UI()
            # show_logout_page()
        elif a==2:
            H_UI()
            # show_logout_page()
        else:
            E_UI()
    else:
        show_login_page()


    
    

    



