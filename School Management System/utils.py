import os
import json
from datetime import datetime

# ------------------------------
# Clear Console Screen
# -------------------------------
def clear_screen():
    os.system("cls" if os.name =="nt" else "clear")
    
# ---------------------------------
# Pause Program
# -----------------------------------
def pause():
    input("\nPress Enter to contin...")
    
# -----------------------------
# Generate Next ID
# ----------------------------
def generate_id(data, prefix ="S"):
    
    """Example:
    S001
    S002
    S003
    T001
    C001
    """
    
    if not data:
        return f"{prefix}001"
    
    last_id = data[-1]["id"]
    
    number = int(last_id[1:]) + 1
    
    return f"{prefix}{number:03d}"

# ---------------------------------
# Validate Integer
# --------------------------------
def input_int(message):
    
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid Input! Enter an integer.")
            
# ------------------------            
# Validate float
# -----------------------
def input_float(message):
    
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid Input! Enter a valid number.")
            
# ------------------------------------
# Validate Non-Emmpty String
# -----------------------------------
def input_string(message):
    
    while True:
        
        value = input(message).strip()
        
        if value:
            return value
        
        print("Input cannot be empty.")
        
# ---------------------
# Validate Phone Number
# -------------------------
def input_phone():
    
    while True:
        
        phone = input("Enter Phone Number : ")
        
        if phone.isdigit() and len(phone) == 10:
            return phone
        
        print("Phone number must contain exactly 10 digits.")
        
        
# ----------------------------
# Validate Age 
# ------------------------------
def input_age():
    
    while True:
        
        age = input_int("Enter Age : ")
        
        if 3 <= age <= 100:
            return age
        
        print("Age must be beetween 3 and 100.")
        
        
# ------------------------------------
# validate Percentage
# ----------------------------
def input_percentage(message):
    
    while True:
        
        per = input_float(message)
        
        if 0 <= per <=100:
            return per
        
        print("percentage must be beetween 0 and 100. ")
        
        
# --------------------------------
# Current Data
# ---------------------------------
def current_data():
    return datetime.now().strftime("%d-%m-%y")



# --------------------------
# Save JSON File
# -----------------------------
def save_json(filename, data):
    
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        
        
# ---------------------------
# Load JSON File
# -------------------------------
def load_json(filename):
    
    try:
        with open(filename, "r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        return []
    
# -----------------------
# Print Line
# ------------------------    
def line(length=50):
    print("-" * length)
    
    
# -----------------------
# Print Title
# ------------------------
def title(text):
    
    line()
    print(text.center(50))
    line()
    
# ---------------------------------
# Display Manu
# -------------------------------
def menu(options):
    
    for key, value in options.items():
        print(f"{key}. {value}")
        
# ---------------------------
# Search by ID
# -----------------------------
def search_by_id(data, item_id):
    
    for item in data:
        if item["id"] == item_id:
            
            return item
        
    return None
    