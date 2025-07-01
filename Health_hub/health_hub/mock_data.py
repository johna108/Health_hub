"""
Mock data generation for Health Hub application.
"""
import random
from typing import List, Dict, Any
from dataclasses import dataclass
from datetime import datetime, timedelta
import math

@dataclass
class MockHospital:
    name: str
    address: str
    phone: str
    distance: float
    specialties: List[str]
    emergency_available: bool
    wait_time: int  # in minutes
    beds_available: int

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate rough distance between two points using simplified formula."""
    # This is a simplified distance calculation, good enough for demo
    dx = (lon2 - lon1) * 111.0 * math.cos(math.radians(lat1))
    dy = (lat2 - lat1) * 111.0
    return round(math.sqrt(dx * dx + dy * dy), 2)

def generate_mock_hospitals(user_lat: float, user_lon: float, count: int = 10) -> List[MockHospital]:
    """Generate mock hospital data."""
    hospital_names = [
        "City General Hospital", "St. Mary's Medical Center", "Unity Healthcare",
        "Metropolitan Hospital", "Central Medical Hub", "Community Care Center",
        "Regional Medical Center", "Hope Memorial Hospital", "Sunshine Healthcare",
        "Valley View Medical", "Riverside Hospital", "Healing Hands Clinic"
    ]
    
    areas = [
        "Downtown", "North Side", "South End", "West Wing", "East Gate",
        "Central District", "Harbor View", "Highland Park", "River Valley",
        "Lake District"
    ]
    
    specialties_list = [
        "Emergency Care", "Cardiology", "Pediatrics", "Orthopedics",
        "Neurology", "Oncology", "General Surgery", "Internal Medicine",
        "Obstetrics", "Dental Care"
    ]

    hospitals = []
    used_names = set()

    for _ in range(min(count, len(hospital_names))):
        # Generate a location within ~5km of the user
        lat_offset = random.uniform(-0.05, 0.05)
        lon_offset = random.uniform(-0.05, 0.05)
        hospital_lat = user_lat + lat_offset
        hospital_lon = user_lon + lon_offset
        
        # Calculate actual distance
        distance = calculate_distance(user_lat, user_lon, hospital_lat, hospital_lon)
        
        # Select a unique name
        available_names = [n for n in hospital_names if n not in used_names]
        if not available_names:
            break
        name = random.choice(available_names)
        used_names.add(name)
        
        area = random.choice(areas)
        
        hospital = MockHospital(
            name=name,
            address=f"{random.randint(100, 999)} {area} Street",
            phone=f"+1-{random.randint(200, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            distance=distance,
            specialties=random.sample(specialties_list, k=random.randint(3, 6)),
            emergency_available=random.choice([True, True, True, False]),  # 75% chance of emergency availability
            wait_time=random.randint(5, 120),
            beds_available=random.randint(0, 50)
        )
        hospitals.append(hospital)
    
    # Sort by distance
    return sorted(hospitals, key=lambda x: x.distance)

def get_hospital_status(hospital: MockHospital) -> Dict[str, Any]:
    """Get real-time status of a hospital."""
    return {
        "wait_time": hospital.wait_time,
        "beds_available": hospital.beds_available,
        "emergency_status": "Accepting Patients" if hospital.emergency_available else "Diverting",
        "last_updated": datetime.now().strftime("%H:%M:%S")
    } 