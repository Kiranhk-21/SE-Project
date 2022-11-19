import streamlit as st
import datetime
from database import *
# from helper import get_form_responces
# st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def M_UI():
    # st.write('logged in as manager'
    col1, col2 = st.columns([12,1])
    with col2:
         if st.button("LogOut"):
             st.session_state['loggedIn']=False    
    st.write('##')
    st.info('logged in as Manager')
    st.write('##')
    mgr_id = st.session_state['user_id']
    # c , col ,d =st.columns[1,3,1]
    st.title(f"Welcome _{get_name_m(mgr_id)}_.")
    # dummy = st.button("LogOut")   
    st.session_state['emp_value'] = st.selectbox(f'select employee to view',show_employees(mgr_id))
    tab1, tab2, tab3 , tab4,tab5,tab6 = st.tabs(["View Details", "Review", "Schedule Meeting","Check Status","calculate score","ShortList"])
    c1,c2,c3 = st.columns(3)
    with tab1:
        
        with st.expander('Employee Details'):
            [e_name,e_id,mail_id,ph_no]=get_emp_details(st.session_state['emp_value'])
            
            st.write(f'Name of the Employee \t: {e_name}')
            # st.write('Name of the Employee :'str(e_name))
            st.write(f'Company ID of the Employee \t: {e_id}')
            st.write(f'Email ID of the Employee \t: {mail_id}')
            st.write(f'Contact number of the Employee \t: {ph_no}')

        [n_task_assn,n_task_comp,n_hour_saved,n_defect_found,n_defect_fixed,accomp]=get_emp_resp_details(st.session_state['emp_value'])
        with st.expander('Form responses'):
            
            st.write(f'Number of Tasks assigned   \t:{n_task_assn}')
            st.write(f'Number of Tasks completed  \t:{n_task_comp}')
            st.write(f'Number of Hours saved      \t:{n_hour_saved}')
            st.write(f'Number of Defects found    \t:{n_defect_found}')
            st.write(f'Number of Defects fixed    \t:{n_defect_fixed}')
        with st.expander('Additional Acomplishments:'):
            st.write(f'Accomplishments of the Employee with respect to previous review\n:{accomp}')
                

    with tab2:
        st.write(f'Employee ID selected: {st.session_state["emp_value"]}')
        st.write(f'Employee name: {get_name_e(st.session_state["emp_value"])}')
        E_id = st.session_state['emp_value']
        M_tasks_A = st.number_input('Number of tasks assigned',min_value=0)
        M_tasks_C = st.number_input('Number of tasks completed',min_value=0)
        M_hours= st.number_input('Number of hours saved',min_value=0)
        M_defects_F  = st.number_input('Number of defects found',min_value=0)
        M_defects_Fix = st.number_input('number of defects fixed',min_value=0)
        age1 = st.slider('Effectiveness in work', 0, 10, 5)
        age2 = st.slider('Integrity', 0, 10, 5)
        age3 = st.slider('Accountability', 0, 10, 5)
        age4 = st.slider('Quality of work', 0, 10, 5)
        age5 = st.slider('Time management', 0, 10, 5)
        acc = st.text_area('Additional NOTE')
        bt = st.button('Submit')
        if (M_tasks_A>=0) and (M_tasks_C>=0) and (M_hours>=0) and (M_defects_F>=0) and (M_defects_Fix>=0) and (age1>=0) and (age2>=0) and (age3>=0) and (age4>=0) and (age5>=0) and acc:
            if bt:
            #if successful
                print("HI")
                execute_cmd(f"Insert into m_resp values('{mgr_id}','{get_name_m(mgr_id)}',{M_tasks_A},{M_tasks_C},{M_hours},{M_defects_F},{M_defects_Fix},{age1},{age2},'{E_id}',{age3},{age4},{age5},'{acc}');")
                st.success("Successfully received your response")
         
    with tab3:
        c1,c2,c3 = st.columns(3)
        with c2:
            d = st.date_input("select a date to schedule the meeting",datetime.date(2019, 7, 6))
            t = st.time_input('Set start time', datetime.time(8, 45))
            st.button('schedule')   
    
    with tab4:
        st.write('##')
        with st.expander('Employees'):
            st.write('show employees_name,id,m_status in DF')
            #query to display number of pending employees
    
    with tab5:
        st.write('##')
        with st.expander('Pending Review'):
            st.write("Displays DF with Employees who's review is pending ID,name,status")
        #if they are pending employees then give a warning 
        st.write('##')
        st.info('Please ensure that all the Employees are reviewed ')
        st.write('##')  
        st.subheader("Calculate Rating Of All Reviewed Employees")
        trig = 0
        if st.button('Calculate'):
            with st.expander('Employees rating'):
                st.write('Displays Ename,ID,rating in ascending order')
        with tab6:
            st.write('##')  
            new_title = '<p style="font-family:Roboto; color:white; font-size: 20px;">Choose an option to select Employees</p>'
            st.markdown(new_title, unsafe_allow_html=True)
            choice = st.radio('',('Based on TOP-N rated Employees', 'Based on Rating-Cutoff'))
            if choice == 'Based on TOP-N rated Employees':
                #handle max_val case
                num = st.number_input('Number of Employees to be selected',min_value=0)     
                with st.expander("Selected Employees"):
                    st.write("Display DF with top k rating E selected ")
                if st.button("Approve"):
                    #implement reconfirmation
                    st.success('Approve successful')
            else:
                num = st.number_input('Enter cutoff Rating',min_value=0)
                with st.expander("Selected Employees"):
                    st.write("Display DF with top k rating E selected ")
                if st.button("Approve"):
                    #implement reconfirmation
                    st.success('Approve successful')




        # with c2 :
        #      center_button = st.button('Button')
    # st.write('---')
    # st.write('')
    # resp = get_form_responces()
    # st.write(resp)
   