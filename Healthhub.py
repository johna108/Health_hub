"""
Health Hub - An enhanced healthcare management system
"""
import streamlit as st
from streamlit_js_eval import get_geolocation
import time
import random
from datetime import datetime, timedelta

# Initialize session state
if "show_appointment_form" not in st.session_state:
    st.session_state.show_appointment_form = False
if "show_health_records" not in st.session_state:
    st.session_state.show_health_records = False
if "location_allowed" not in st.session_state:
    st.session_state.location_allowed = False

# Application Header
st.title("Health Hub")
st.subheader("Your Health, Your Way")

# Sidebar for navigation
with st.sidebar:
    st.title("Navigation")
    page = st.radio(
        "Go to",
        ["🏥 Find Hospitals", "📅 Book Appointment", "🚨 Emergency Info", "📋 Health Records"]
    )

# Hospital specializations
SPECIALIZATIONS = [
    "---Select---",
    "Cardiologist",
    "Dermatologist",
    "Orthopedic",
    "Pediatrician",
    "Neurologist",
    "Urologist",
    "Obstetrics and gynaecology",
    "Gastroenterologist",
    "Other"
]

def show_find_hospitals():
    """Display the hospital finder section."""
    st.header("Find Nearby Hospitals")
    
    # Checkbox to initiate location check
    if st.checkbox("Allow location access", value=st.session_state.location_allowed):
        loc = get_geolocation()
        st.session_state.location_allowed = True
        
        # Button to get geolocation and display map when clicked
        if st.button("Find nearby hospitals"):
            st.balloons()
            if st.session_state.location_allowed:
                map_html = """
                <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1Z_HW9b9K1ejzS6wjzkIJgCrPFrOossg&ehbc=2E312F&noprof=1" width="640" height="480">
                </iframe>
                """
                st.markdown(map_html, unsafe_allow_html=True)
            else:
                st.warning("Please allow 'location access'")

def show_appointment_form():
    """Display the appointment booking form."""
    st.header("Book an Appointment")
    
    if st.button("Book an appointment"):
        st.session_state.show_appointment_form = True

    if st.session_state.show_appointment_form:
        with st.form("appointment_form"):
            user_name = st.text_input("Your Name", max_chars=50)
            contact_number = st.text_input("Contact Number", max_chars=10)
            
            # Additional input boxes
            specialization = st.selectbox("Select Doctor's Specialization", SPECIALIZATIONS)
            patient_issue = st.text_area("Describe Patient's Issue", max_chars=500)
            
            appointment_date = st.date_input("Select Appointment Date")
            appointment_time = st.time_input("Select Appointment Time")
            submit_button = st.form_submit_button("Book Appointment")

        # Check if the form is submitted and display a confirmation message
        if submit_button:
            if user_name and contact_number and specialization != "---Select---":
                st.success(f"Appointment booked successfully! {user_name}, you have an appointment on {appointment_date} at {appointment_time}.")
                st.info(f"Specialization: {specialization}, Patient's Issue: {patient_issue}")
                st.session_state.show_appointment_form = False
            else:
                st.warning("Please provide Important details dont leave blank boxes.")

def show_emergency_info():
    """Display emergency information."""
    st.header("Emergency Info")
    
    if st.button("Emergency Info"):
        with st.spinner("Fetching emergency information..."):
            # Simulate fetching data with a random delay
            time.sleep(random.uniform(2, 5))
            
            st.table({
                "Hospital Name": ["Malla Reddy Narayana Multispeciality Hospital", "Lifespan Super Speciality Hospitals", "MEDIVISION SUPER SPECIALTY HOSPITAL"],
                "Contact Number": ["087903 87903", "95151 51274", "093914 21275"],
                "Distance": ["4.5 km", "7.2 km", "8 km"]
            })

def show_health_records():
    """Display personal health records."""
    st.header("Personal Health Records")
    
    if st.button("Show my health records"):
        with st.spinner("Fetching health records..."):
            # Simulate fetching data with a random delay
            time.sleep(random.uniform(1, 3))
            st.info("No health records found.")

# Page routing
if page == "🏥 Find Hospitals":
    show_find_hospitals()
elif page == "📅 Book Appointment":
    show_appointment_form()
elif page == "🚨 Emergency Info":
    show_emergency_info()
else:  # Health Records
    show_health_records() 