import streamlit as st
from streamlit_js_eval import streamlit_js_eval, get_geolocation
import json
import time
import random

# Define a function to create a session state
def get_session_state():
    session_state = st.session_state
    if "show_appointment_form" not in session_state:
        session_state.show_appointment_form = False
    if "show_health_records" not in session_state:
        session_state.show_health_records = False
    return session_state

x = None
get_session_state()  # Initialize the session state

st.title("Health Hub")
st.subheader("Your Health, Your Way")

# Checkbox to initiate location check
if st.checkbox("Allow location access"):
    loc = get_geolocation()
    x = True
    st.write(f"Your coordinates are {loc}")

# Button to get geolocation and display map when clicked
if st.button("Find nearby hospitals"):
    st.balloons()
    if x == True:
        map_html = """
     <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1Z_HW9b9K1ejzS6wjzkIJgCrPFrOossg&ehbc=2E312F&noprof=1" width="640" height="480">
     </iframe>
        """
        st.markdown(map_html, unsafe_allow_html=True)
    else:
        st.warning("Please allow 'location access'")

# Button to show the appointment booking form
st.header("Appointment Booking")

if st.button("Book an appointment"):
    get_session_state().show_appointment_form = True

if get_session_state().show_appointment_form:
    # Section for appointment booking
    with st.form("appointment_form"):
        user_name = st.text_input("Your Name", max_chars=50)
        contact_number = st.text_input("Contact Number", max_chars=10)
        
        # Additional input boxes
        specialization = st.selectbox("Select Doctor's Specialization", ["---Select---","Cardiologist", "Dermatologist", "Orthopedic", "Pediatrician","Neurologist","Urologist","Obstetrics and gynaecology","Gastroenterologist","Other"])
        patient_issue = st.text_area("Describe Patient's Issue", max_chars=500)
        
        appointment_date = st.date_input("Select Appointment Date")
        appointment_time = st.time_input("Select Appointment Time")
        submit_button = st.form_submit_button("Book Appointment")

    # Check if the form is submitted and display a confirmation message
    if submit_button:
        if user_name and contact_number and specialization:
            st.success(f"Appointment booked successfully! {user_name}, you have an appointment on {appointment_date} at {appointment_time}.")
            st.info(f"Specialization: {specialization}, Patient's Issue: {patient_issue}")
        else:
            st.warning("Please provide Important details dont leave blank boxes.")

# Section for Emergency Info
st.header("Emergency Info")

# Button to find nearest hospitals and contacts
if st.button("Emergency Info"):
    with st.spinner("Fetching emergency information..."):
        # Simulate fetching data with a random delay
        time.sleep(random.uniform(10, 20))
        
        # Add code here to retrieve and display nearest hospitals and contacts based on user location
        # You can use the loc variable for the user's location
        # Display hospitals and contacts in a formatted way, e.g., in a table
        st.table({"Hospital Name": ["Malla Reddy Narayana Multispeciality Hospital", "Lifespan Super Speciality Hospitals", "MEDIVISION SUPER SPECIALTY HOSPITAL"],
                  "Contact Number": ["087903 87903", "95151 51274", "093914 21275"],
                  "Distance": ["4.5 km", "7.2 km", "8 km"]})

# Section for Personal Health Records
st.header("Personal Health Records")

# Button to show personal health records
if st.button("Show my health records"):
    with st.spinner("Fetching health records..."):
        # Simulate fetching data with a random delay
        time.sleep(random.uniform(5, 15))
        
        # Display a message if no health records are found
        st.info("No health records found.")
