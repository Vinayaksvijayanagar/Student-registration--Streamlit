import streamlit as st
import pandas as pd
# background-image:url(" "); for url
st.markdown (
    """
    <style>
    .stApp{
        background-color: black;

    }
    </style>
    """,
    unsafe_allow_html = True
)
if "students" not in st.session_state:
    st.session_state.students = []
st.sidebar.selectbox("Select Course",("AI","DS","WEB DEV"))
st.sidebar.selectbox("Select Mode",("Online","Ofline"))

with st.form("student details"):


    

    name  = st.text_input("enter the name")
   
    age  = st.slider("enter the age",18,60,18)
    
    gender = st.radio("enter the gender",("male","female"))
   

    skills = st.multiselect("enter the skills",("AI","DS","ML","DSA","OS","Other"))
    

    joining_date = st.date_input("enter the date")
    

    paid_fee= st.number_input("enter the amount you have paid")
  
    a = st.form_submit_button("click") 
    
if a:
    st.write("successfully Submited")    
    data = {
        "name":name,
        "age":age,
        "gender":gender,
        "skills":skills,
        "joining_date":joining_date,
        "paid_fee":paid_fee
        }
    st.session_state.students.append(data)
    st.dataframe(data)
#Display
if st.session_state.students:
    st.write("total number of applied students",len(st.session_state.students))

if st.session_state.students:
    st.write("total students")
    datas = pd.DataFrame(st.session_state.students)
    st.dataframe(datas)

#avegae age of students
if st.session_state.students:
    avg_age = sum(student["age"] for student in st.session_state.students)/len(st.session_state.students)
    st.write("average age of students",avg_age)
    total_fee = sum(student["paid_fee"] for student in st.session_state.students)
    st.write("total amount paid is",total_fee)