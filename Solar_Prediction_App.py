import pandas as pd
import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
model = pickle.load(open(r"SolarXG.pkl", 'rb'))

st.title("Solar Radiance Prediction")
st.image("https://storage.googleapis.com/kaggle-datasets-images/1296/2322/0b16f3559783c578157e0997dc15d4af/dataset-cover.jpg",caption ="Radiating Solar Power",use_column_width=True)

st.sidebar.header("More Details:")
st.sidebar.markdown("[For More facts about the Solar Irradiance here](https://en.wikipedia.org/wiki/Solar_irradiance#:~:text=Solar%20irradiance%20is%20the%20power,m2)")
st.sidebar.markdown("[and here](https://www.sciencedirect.com/topics/engineering/solar-irradiation)")
st.title("         Check Solar Irradiance          ")
st.title("                                                 ")
Temperature = st.number_input("Enter Temperature :",min_value = 25, max_value = 75,step=1, value = 30)
Pressure	= st.number_input("Enter Pressure :",min_value = 30., max_value = 35.,step=0.01,format="%.2f", value = 30.)
Humidity    = st.number_input("Enter Humidity :",min_value = 5, max_value = 108,step=1, value = 75)
WindDirection = st.number_input("Enter WindDirection(Degrees) :",min_value = 0., max_value = 360.,step=0.01,format="%.2f", value = 108.)
Speed = st.number_input("Enter Speed :",min_value = 0., max_value = 45.,step=0.01,format="%.2f", value = 10.)
Month = st.selectbox("Select a Month :", ['September', 'October', 'November', 'December'])
max_day = 30
if(Month == "September"):
    Month = 9
    max_day = 30
elif(Month == "October"):
    Month = 10
    max_day = 31
elif(Month == "November"):
    Month = 11
    max_day = 30
Day = st.number_input("Enter the day of the month: ", min_value = 1, max_value = max_day, step = 1, value = 15)
Hour   = st.number_input("Enter Hour :",min_value = 0, max_value = 23,step=1, value = 12)
Minute = st.number_input("Enter Minute :",min_value = 0, max_value = 59,step=1, value = 36)
Second = st.number_input("Enter Second :",min_value = 0, max_value = 59,step=1, value = 36)
risehour = st.radio("risehour :", options = (5,6), horizontal = True)
riseminute = st.number_input("Enter RiseMinute :" , min_value = 0, max_value = 59, step = 1, value = 36)
sethour = st.radio("Choose SetHour :", options = (17,18), horizontal = True)
setminute = st.number_input("Enter SetMinute :" , min_value = 0, max_value = 59, step = 1, value = 36)

data = {"Temperature" : Temperature, "Pressure" : Pressure, "Humidity" : Humidity, "WindDirection(Degrees)" :WindDirection, "Speed" : Speed, 
        'Month': Month, "Day" : Day, 'Hour': Hour, "Minute" : Minute, "Second" : Second, "risehour" : risehour,"riseminute":risehour, 'sethour' : sethour, 'setminute': setminute}

df=pd.DataFrame(data,index=[0])
#scaler = StandardScaler()
#df = scaler.fit_transform(df)

if st.button("Predict"):                                                                ## prediction button created,which returns predicted value from ml model(pickle file)
    result = model.predict(df)                                                        ## prediction of user-input
    st.write("Solar Irradiance (in watts per square metre (W/m2)) : {}".format(result))






















