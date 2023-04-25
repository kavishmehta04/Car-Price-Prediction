import streamlit as st
import numpy as np
import pickle


#Importing our pickle file
model = pickle.load(open('car_pred_model.pkl', 'rb'))

#Title of app
st.title('Predicted price of car :car:')

#Range of paramenters
#Price	Kilometer	Fuel Type	Transmission	Owners Before	Engine	Fuel Tank Capacity	Age
Kilometer = st.text_input("Kilometer",75,2000000)
Fuel_Type = st.slider("Fuel Type Diesel",0,1)
Transmission = st.slider("Transmission Automatic ",0,1)
Owners = st.slider("Owners Before",0,4)
Engine = st.text_input("Engine in CC",624,6592)
Fuel = st.text_input("Fuel Tank Capacity in L",15,105)
Age = st.text_input("Age of the Car",1,35)

#Pridiction function
def predict():
    float_features = [float(x) for x in [Kilometer,Fuel_Type,Transmission,Owners,Engine,Fuel,Age]]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    label = prediction[0]
    
    print(type(label))
    print(label)

#Printing the output 
    st.success('The car price is : ' + str(label) + ' :thumbsup:')
trigger = st.button('Predict', on_click=predict)

