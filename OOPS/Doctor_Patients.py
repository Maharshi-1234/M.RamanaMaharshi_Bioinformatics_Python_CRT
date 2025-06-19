class Person:
    def __init__(self, name, age, gender):
        self.Name = name
        self.Age = age
        self.Gender = gender

    def Details(self):
        print(f"Name of the person: {self.Name}")
        print(f"Age of the Person: {self.Age}")
        print(f"Gender of the person: {self.Gender}")


class Patient(Person):
    def __init__(self, name, age, gender, disease):
        super().__init__(name, age, gender)
        self.Disease = disease

    def Details(self):
        print(f"Name of the Patient: {self.Name}")
        print(f"Age of the Patient: {self.Age}")
        print(f"Gender of the Patient: {self.Gender}")
        print(f"Disease of the Patient: {self.Disease}")


class Doctor(Person):
    def __init__(self, name, age, gender, specialization):
        super().__init__(name, age, gender)
        self.Specialization = specialization
        self._patients = []  # Use the same name (_patients) consistently

    def assign_patient(self, patient):
        self._patients.append(patient)

    def Details(self):
        print(f"Name of the Doctor: {self.Name}")
        print(f"Age of the Doctor: {self.Age}")
        print(f"Gender of the Doctor: {self.Gender}")
        print(f"Specialization of the Doctor: {self.Specialization}")

    def Details_Patients(self):
        if not self._patients:
            return "No patients assigned"
        result = ""
        for p in self._patients:
            result += f"- {p.Name} ({p.Disease})\n"
        return result.strip()


# Sample Usage
doctors = []
Patients = []

def find_doctor_by_name(name):
    for doc in doctors:
        if doc.Name.lower() == name.lower():
            return doc
    return None


# Example to test:
doc1 = Doctor("Dr. Ravi", 45, "Male", "Cardiology")
pat1 = Patient("Anita", 30, "Female", "Heart Pain")
pat2 = Patient("Ramesh", 50, "Male", "Arrhythmia")

doc1.assign_patient(pat1)
doc1.assign_patient(pat2)

doctors.append(doc1)
Patients.append(pat1)
Patients.append(pat2)

# Display Doctor and their patients
doc1.Details()
print("Assigned Patients:\n" + doc1.Details_Patients())
