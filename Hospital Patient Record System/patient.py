from person import Person


class Patient(Person):

    def __init__(self, patient_id, name, age, disease):
        super().__init__(patient_id, name, age)
        self.__disease = disease

    # Getter
    def get_disease(self):
        return self.__disease

    # Setter
    def set_disease(self, disease):
        self.__disease = disease

    # Display Patient Details
    def display_details(self):
        print("\n" + "=" * 60)
        print("                    PATIENT DETAILS")
        print("=" * 60)
        print(f"Patient ID : {self._person_id}")
        print(f"Name       : {self._name}")
        print(f"Age        : {self._age}")
        print(f"Disease    : {self.__disease}")
        print("=" * 60)