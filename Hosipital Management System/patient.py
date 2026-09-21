class Patient:
    def __init__(self, patient_id, name, age, gender, disease):
         self.patient_id = patient_id
         self.name = name
         self.age = age
         self.gender = gender
         self.disease = disease
         
    def to_dict(self):
        return {
            'patient_id' : self.patient_id,
            'name' : self.name,
            'age' : self.age,
            'gender': self.gender,
            'disease': self.disease
            }
         