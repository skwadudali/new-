import streamlit as st
import pandas as pd

#building the model
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
df =pd.read_csv("breast_cancer.csv")
x=df.iloc[:,:-1]
y=df.outcome
pca=PCA()
X_pca=pd.DataFrame(pca.fit_transform(x))
x_pca_select = X_pca.iloc[:,:5]
x_train,x_test,y_train,y_test = train_test_split(x_pca_select,y,test_size=0.2,random_state=4)
model= SVC(kernel='linear',C=1)
model.fit(x_train,y_train)


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
    prediction = model.predict(x)[0]
    if st.button("prediction"):
        if prediction == 1:
            st.success(f"You have Breast Cancer")
        else:
            st.success(f"Relax You are Safe!!! You don't have breast cancer")

        
 

if nav == "Data and Graphs":
    df
