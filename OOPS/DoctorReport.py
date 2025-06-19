# Report: Doctor - Patient Details

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
        self._patients = []

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


# Global Lists
doctors = []
Patients = []

# Search function
def find_doctor_by_name(name):
    for doc in doctors:
        if doc.Name.lower() == name.lower():
            return doc
    return None


# ======= Sample Usage (you can remove below if using in production) =======

# Create doctor and patients
doc1 = Doctor("Dr. Lalasa", 40, "Female", "Neurology")
pat1 = Patient("Jaggu", 30, "Male", "Migraine")
pat2 = Patient("Maharshi", 35, "Male", "Seizures")

# Assign patients to doctor
doc1.assign_patient(pat1)
doc1.assign_patient(pat2)

# Add to lists
doctors.append(doc1)
Patients.extend([pat1, pat2])

# Print Doctor and Patient Info
doc1.Details()
print("\nAssigned Patients:")
print(doc1.Details_Patients())
