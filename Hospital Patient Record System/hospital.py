import csv
import os
from patient import Patient


class Hospital:

    def __init__(self):
        self.patients = []
        self.filename = "patients.csv"
        self.load_patients()

    # -----------------------------
    # Load Patient Records
    # -----------------------------
    def load_patients(self):

        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r", newline="") as file:

                reader = csv.reader(file)
                next(reader, None)

                for row in reader:

                    if len(row) == 4:

                        patient = Patient(
                            row[0],
                            row[1],
                            int(row[2]),
                            row[3]
                        )

                        self.patients.append(patient)

        except Exception:
            print("\nError loading patient records.")

    # -----------------------------
    # Save Patient Records
    # -----------------------------
    def save_patients(self):

        try:

            with open(self.filename, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow(["ID", "Name", "Age", "Disease"])

                for patient in self.patients:

                    writer.writerow([
                        patient._person_id,
                        patient._name,
                        patient._age,
                        patient.get_disease()
                    ])

        except Exception:
            print("\nError saving patient records.")

    # -----------------------------
    # Register Patient
    # -----------------------------
    def add_patient(self):

        try:

            print("\nEnter Patient Details")
            print("-" * 40)

            patient_id = input("Patient ID      : ")

            for patient in self.patients:

                if patient._person_id == patient_id:
                    print("\nPatient ID already exists.")
                    return

            name = input("Patient Name    : ")
            age = int(input("Patient Age     : "))
            disease = input("Patient Disease : ")

            patient = Patient(
                patient_id,
                name,
                age,
                disease
            )

            self.patients.append(patient)

            self.save_patients()

            print("\n" + "=" * 60)
            print("Patient registered successfully.")
            print("=" * 60)

        except ValueError:
            print("\nInvalid age entered.")

    # -----------------------------
    # Display Patients
    # -----------------------------
    def display_patients(self):

        if len(self.patients) == 0:

            print("\nNo patient records available.")
            return

        print("\n" + "=" * 75)
        print("{:<10}{:<25}{:<10}{:<25}".format(
            "ID",
            "NAME",
            "AGE",
            "DISEASE"
        ))
        print("=" * 75)

        for patient in self.patients:

            print("{:<10}{:<25}{:<10}{:<25}".format(
                patient._person_id,
                patient._name,
                patient._age,
                patient.get_disease()
            ))

        print("=" * 75)

    # -----------------------------
    # Search Patient
    # -----------------------------
    def search_patient(self):

        patient_id = input("\nEnter Patient ID : ")

        for patient in self.patients:

            if patient._person_id == patient_id:

                patient.display_details()
                return

        print("\nPatient not found.")

    # -----------------------------
    # Update Patient
    # -----------------------------
    def update_patient(self):

        patient_id = input("\nEnter Patient ID : ")

        for patient in self.patients:

            if patient._person_id == patient_id:

                print("\nEnter New Details")
                print("-" * 40)

                patient._name = input("New Name    : ")
                patient._age = int(input("New Age     : "))
                patient.set_disease(input("New Disease : "))

                self.save_patients()

                print("\n" + "=" * 60)
                print("Patient record updated successfully.")
                print("=" * 60)

                return

        print("\nPatient not found.")

    # -----------------------------
    # Delete Patient
    # -----------------------------
    def delete_patient(self):

        patient_id = input("\nEnter Patient ID : ")

        for patient in self.patients:

            if patient._person_id == patient_id:

                self.patients.remove(patient)

                self.save_patients()

                print("\n" + "=" * 60)
                print("Patient record deleted successfully.")
                print("=" * 60)

                return

        print("\nPatient not found.")