import streamlit as st
import pandas as pd
import joblib
model = joblib.load('p1')
def main():
    nav=st.sidebar.radio("Navigation",["Home","Prediction","Data and Graphs"]) 
    if nav == "Home":
        st.write(f"hey dear you are welcome here..together we will win the fight")
    if nav == "Prediction":
        st.write("Hey dear,dont worry!! Have a relux")
        st.title("Breast cancer prediction")
        s1=st.number_input(" 1st Sample input, Range: -10 to 1000",0,1000,step=25)
        s2=st.number_input(" 2nd Sample input, Range: -10 to 1000",0,1000,step=25)
        s3=st.number_input("3rd Sample input, Range: -10 to 1000",0,1000,step=25)
        s4=st.number_input("4th Sample input, Range: -10 to 1000",0,1000,step=25)
        s5=st.number_input("5th Sample input, Range: -10 to 1000",0,1000,step=25)
        x=[[s1,s2,s3,s4,s5]]
        prediction = model.predict(x)
        if st.button("prediction"):
            if prediction == 1:
                st.success(f"You have Breast Cancer")
            else:
                st.success(f"Relax You are Safe!!! You don't have breast cancer")

        if nav == "Data and Graphs":
            pass
   
if __name__ =='__main__':
  main()    

    