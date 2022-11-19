import streamlit as st
from database import *

def E_UI():
    col1, col2 = st.columns([3.5,1])
    with col2:
            dummy = st.button("LogOut")
            if dummy :
                st.session_state['loggedIn']=False
    c1,c2,c3=st.columns([2,10,2])
    with c2:
        st.write('##')
        st.info('logged in as Employee')
        st.write('##')
    
        with st.form('E_details'):
            E_id = st.session_state['user_id']
            st.write(f"Employee ID : {E_id}")
            # st.write("fetch and display corresponding ename")
            name = get_name(E_id)
            st.write(name)
            tasks_A = st.number_input('Number of tasks assigned',min_value=0)
            tasks_C = st.number_input('Number of tasks completed',min_value=0)
            hours= st.number_input('Number of hours saved',min_value=0)
            defects_F  = st.number_input('Number of defects found',min_value=0)
            efects_Fix = st.number_input('number of defects fixed',min_value=0)
            acc = st.text_area('Additional Accomplishments')
            if E_id and tasks_A and tasks_C and hours and defects_F and efects_Fix and acc :
                
                if st.form_submit_button('submit'):
                # st.session_state['loggedIn']=False
                    execute_cmd(f"Insert into emp_resp values('{name}',\"{E_id}\",{tasks_A},{tasks_C},{hours},{defects_F},{efects_Fix},\"{acc}\");")
                    st.success("Successfully submitted your form.Please wait for our response")