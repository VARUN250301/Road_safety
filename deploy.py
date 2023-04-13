import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/Shree/Desktop/even acc pred/trained_model.sav', 'rb'))

#function for prediction
def accident_severity_prediction(input_data):
    #input_data = (1, 0, 0, 7, 4, 5, 1, 0, 3, 2, 2, 1, 0, 1, 2, 1, 5, 0)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0] == 0):
        return 'low'
    elif(prediction[0] == 1):
        return 'medium'
    else:
        return 'high'

def main():
    st.title('Accident Severity Prediction Web App')

    # age band of driver, driving experience, type of vehicle, area accident occurence, lanes or medians, road allignment, types of junction, road surface condition, light condition, weather condition, type of collision, number of vehicles involved, number of casualties, vehicle movement, casualty class, age band of casualty, pedestrian movement, cause of accident

    age = st.text_input('Age band of driver')

    exp = st.text_input('Experience of Driver')

    vtype = st.text_input('Type of Vehicle?')

    area = st.text_input('Area of accident occurence?')

    lanes = st.text_input('Lanes or medians?')

    align = st.text_input('Road allignment?')

    junction = st.text_input('Type of junction?')

    surface = st.text_input('Road Surface condition?')

    light = st.text_input('Light Condition?')

    weather = st.text_input('Weather Condition?')

    collision = st.text_input('Type of Collision?')

    number_of_vehicles = st.text_input('Number of Vehicles involved?')

    number_of_casualties = st.text_input('Number of casualties?')

    movement = st.text_input('Vehicle movement?')

    cclass = st.text_input('Casualty Class?')

    age_band = st.text_input('Age band of casualty?')

    pedestrian_m = st.text_input('Pedestrian movement?')

    cause = st.text_input('Cause of Accident?')
    
    result = ''

    #button for prediction

    if st.button('severity'):
        result = accident_severity_prediction([age, exp, vtype, area, lanes, align, junction, surface, light, weather, collision, number_of_vehicles, number_of_casualties, movement, cclass, age_band, pedestrian_m, cause])

    st.success(result)

if __name__ == '__main__':
    main()

