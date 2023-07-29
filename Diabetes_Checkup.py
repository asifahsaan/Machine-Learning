import streamlit as st
import pickle
import numpy as np

# loading the saved model
loaded_model = pickle.load(open('LSVC_model.pkl', 'rb'))

# write prediction function
def diabetes_prediction(input_data):
    # Convert input_data to numpy array and ensure it is of numeric type
    input_data_as_numpy_array = np.asarray(input_data, dtype=np.float32)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return ':sparkle: The person is not diabetic'
    else:
        return ':sos: The person is diabetic'

def main():
    # giving title to app
    st.title(':male-doctor: Diabetes Prediction WebApp :registered:')

    # Input fields organized into five rows, two input fields per row
    cols = st.columns(2)

    with cols[0]:
        Pregnancies = st.text_input('Number of Pregnancies', key='Pregnancies')
        Glucose = st.text_input('Glucose Level', key='Glucose')
        BloodPressure = st.text_input('Blood Pressure value', key='BloodPressure')
        SkinThickness = st.text_input('Skin Thickness value', key='SkinThickness')

    with cols[1]:
        Insulin = st.text_input('Insulin Level', key='Insulin')
        BMI = st.text_input('BMI value', key='BMI')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', key='DiabetesPedigreeFunction')
        Age = st.text_input('Age of the Person', key='Age')

    # creating a centered and larger button for Prediction
    # if st.beta_container():
    #     st.button('Diabetes Test Result', key='DiabetesTestButton', help='Click this button to perform the prediction.')
        
    # Validation and Error Handling
    btn = st.button('Diabetes Test Result')
    if btn:
        # Display messages for each input field if they are empty
        if not Pregnancies:
            st.empty()
            st.warning("Please enter the number of pregnancies.")
            return
        if not Glucose:
            st.empty()
            st.warning("Please enter the glucose level.")
            return
        if not BloodPressure:
            st.empty()
            st.warning("Please enter the blood pressure value.")
            return
        if not SkinThickness:
            st.empty()
            st.warning("Please enter the skin thickness value.")
            return
        if not Insulin:
            st.empty()
            st.warning("Please enter the insulin level.")
            return
        if not BMI:
            st.empty()
            st.warning("Please enter the BMI value.")
            return
        if not DiabetesPedigreeFunction:
            st.empty()
            st.warning("Please enter the diabetes pedigree function value.")
            return
        if not Age:
            st.empty()
            st.warning("Please enter the age of the person.")
            return

        try:
            # Convert input values to floats
            Pregnancies = float(Pregnancies)
            Glucose = float(Glucose)
            BloodPressure = float(BloodPressure)
            SkinThickness = float(SkinThickness)
            Insulin = float(Insulin)
            BMI = float(BMI)
            DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
            Age = float(Age)
        except ValueError:
            st.warning("Please enter valid numeric values for all input fields.")
            return

        # code for Prediction
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

        # Display the result
        st.success(diagnosis)


if __name__ == "__main__":
    main()