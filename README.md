# Health Hub - Demo Healthcare Management System

A demonstration project showcasing a simple healthcare management system built with Python and Streamlit. This is a testing demo website created while learning Python web development.

## Overview

Health Hub is a demo web application that simulates a healthcare facility finder and appointment booking system. It was initially created with hardcoded values for testing and learning purposes, and later improved based on user feedback to remove unnecessary complexity while maintaining core functionality.

## Features

- **Hospital Finder (Demo)**
  - Simple location-based hospital search
  - View nearby hospitals on an embedded Google Map
  - Basic hospital information display

- **Appointment Booking**
  - Simple appointment form
  - Select from various medical specializations
  - Basic appointment confirmation

- **Emergency Info**
  - Quick access to hospital contacts
  - Basic emergency information display
  - Hospital distance information

- **Health Records**
  - Basic health records view
  - Simple data display

## Technical Details

- **Built with:**
  - Python
  - Streamlit (for web interface)
  - streamlit-js-eval (for basic location services)

## Important Note

This is a TESTING DEMO project created while learning Python. All data shown is simulated and should not be used for actual medical purposes. The hospital information and other data are hardcoded for demonstration only.

## Project Structure

```
Health_hub/
  └── health_hub/
      ├── Healthhub.py    # Main application file
      └── README.md       # This file
```

## Running the Application

1. Install the required packages:
```bash
pip install streamlit streamlit-js-eval
```

2. Run the application:
```bash
streamlit run Healthhub.py
```

## Development Notes

This project has gone through several iterations based on user feedback:
- Initially created with hardcoded values for learning purposes
- Simplified the location services implementation
- Removed unnecessary coordinate displays
- Kept core functionality simple and straightforward
- Removed unused files and dependencies

## Learning Project Details

This project demonstrates:
- Basic web application development with Python
- Simple location-based services
- Form handling
- Basic user interface design

## Disclaimer

This is a demo project created for learning and testing purposes only. All data shown is simulated and should not be used for any real-world purposes.

## Author

Created as a personal learning project while exploring Python web development.

## License

This project is open source and available for learning purposes. 