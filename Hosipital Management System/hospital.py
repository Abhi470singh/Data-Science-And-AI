from patient import Patient
from doctor import Doctor
from database import load_data, save_data


class Hospital:
    def __init__(self):
        self.patient_file = 'patients.json'
        self.doctor_file = 'doctors.json'
        
        self.patients = load_data(self.patient_file)
        self.doctors = load_data(self.doctor_file)
        
# --------------------
# Patient Functions
# --------------------
        
    def add_patient(self):
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age:"))
        gender = input("Enter Gender :")
        disease = input("Enter Disease :")
        
        patient = Patient(patient_id, name, age, gender, disease)
        
        self.patients.append(patient.to_dict())
        save_data(self.patient_file, self.patients)
        
        print('Patiebt added successfully!')
        
    def view_patients(self):
        if not self.patients:
            print("No patients found.")
            return
        
        print("\\n--- Patient Recoads ---")
        for p in self.patients:
            print(f'ID: {p["patient_id"]}, Name: {p["name"]}, Age: {p["age"]}, Disease: {p["disease"]}')
            
    def search_patient(self):
        patient_id = input("Enter Patient ID: ")
        
        for p in self.patients:
            if p['patient_id'] == patient_id:
                print('\\nPatient Founnd:')
                print(p)
                return
            
        print("Patient Not Found.")
        
    def delete_patient(self):
        patient_id = input("Enter Patient ID to delete: ")
        
        for p in self.patients:
            if p['patient_id'] == patient_id:
                self.patients.remove(p)
                save_data(self.patient_file, self.patients)
                print('Patient deleted successfully!')
                return
            
        print('Patient not found.')
        
# -----------------------
# Doctor Functions
# -----------------------

    def add_doctor(self):
        doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Specialization: ")
        
        doctor = Doctor(doctor_id, name, specialization)
        
        
        self.doctors.append(doctor.to_dict())
        save_data(self.doctor_file, self.doctors)

        print('Doctor added successfully!')
        
    def view_doctors(self):
        if not self.doctors:
            print("No doctors found.")
            return
        
        print("\\n--- Doctor Recoads ---")
        for d in self.doctors: 
            print(f'ID: {d["doctor_id"]}, Name: {d["name"]}, Specialization: {d["specialization"]}')       
        
        
        
        
        
        
        