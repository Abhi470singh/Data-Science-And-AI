class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        
    def to_dict(self):
        return {
            'doctor_id': self.doctor_id,
            'name': self.name,
            'specialization': self.specialization
        }