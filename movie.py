import streamlit as st

st.set_page_config(page_title="Movie ticket")

st.title("Movie ticket")

st.write("Enter Age ")


num1 = st.number_input("Enter your age :", value=0.0)

if st.button("Check"):
    if num1>18:
        st.success(f"You can watch movie")

    
    else:
         
        st.success(f"You can watch movie only with parents")






    