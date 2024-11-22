import json
import os

# Set the working directory where the JSON file will be stored
os.chdir("Your\\Path\\Here")
print("Current working directory:", os.getcwd())

patients_data = {}

def load_data():
    global patients_data
    if os.path.exists("patients_data.json"):
        try:
            with open("patients_data.json", "r", encoding="utf-8") as file:
                patients_data = json.load(file)
                print("Patient data loaded successfully.")
                print(patients_data)  # Debug: Print the loaded data
        except json.JSONDecodeError:
            print("Error loading JSON data. The file might be corrupted.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
    else:
        print("No previous patient data found.")

def save_data():
    global patients_data
    try:
        with open("patients_data.json", "w", encoding="utf-8") as file:
            json.dump(patients_data, file, indent=4, ensure_ascii=False)  # Make sure special characters are saved properly
        print("Patient data saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")



def PatientNumber():
    """Get a unique patient number from the user."""
    while True:
        try:
            Patient_Number = int(input("Write the pantient number: "))
            if Patient_Number == 0:
                print("Zero is not allowed please write a valid patient number.")
                continue
            if str(Patient_Number) in patients_data:
                print(f"Patient number {Patient_Number} already exists! Please use a unique number.")
                continue
            return Patient_Number
        except ValueError:
            print("That`s not a valid number.")
        
def PatientName():
    """Get the patient's name, ensuring it does not contain numbers."""
    while True:            
        try:
            Patient_Name = input("Write the patient`s name and surname separated by space: " ).title()
            if any(char.isdigit() for char in Patient_Name):
                raise ValueError
            return Patient_Name
        except ValueError:
             print("Thats not valid name please write the correct name.(DO NOT USE NUMBERS)")
             

def PatientAge():
    """Get the patient's age as a positive integer."""
    while True:
        try:
            Patient_Age = int(input("Please write the patient`s age: "))
            if Patient_Age == 0:
                print("Zero is not valid as an age.")
                continue
            return Patient_Age
        except ValueError:
            print("Not write age with letters.")
        
def StorePatientData():
    global patients_data
    patient_number = PatientNumber()
    patient_name = PatientName()
    patient_age = PatientAge()

    patients_data[str(patient_number)] = {
        "name": patient_name,
        "age": patient_age
    }
    save_data()
    print("Patient data saved successfully.")

def search_patient():
    """Search for a patient by their unique number."""
    global patients_data
    try:
        patient_number = int(input("Enter patient number to search: "))
        patient_number_str = str(patient_number)
    except ValueError:
        print("Please enter a valid number.")
        return
    
    if patient_number_str in patients_data:
        patient = patients_data[patient_number_str]
        print(f"Patient Found Name: {patient['name']}, Age: {patient['age']}")
    else:
        print("Patient not found.")

def delete_patient():
    """Delete a patient by their unique number."""
    global patients_data
    try:
        patient_number = int(input("Enter the patient number to delete: "))
        patient_number_str = str(patient_number)
    except ValueError:
        print("Please enter a valid number.")
        return

    if patient_number_str in patients_data:
        del patients_data[patient_number_str]
        save_data()
        print(f"Patient number {patient_number} has been deleted successfully.")
    else:
        print("Patient not found.")


# Load data when the program starts
load_data()

# Main menu loop
while True:
    print("\n1. Store Patient Data")
    print("2. Search for Patient by Number")
    print("3. Delete a Patient")
    print("4. Exit and Save the Data")

    choice = input("Chose an option: ")

    if choice == "1":
        StorePatientData()
    elif choice == "2":
        search_patient()
    elif choice == "3":
        delete_patient()
    elif choice == "4":
        print("Stopping the code.")
        save_data()
        break
    else:
        print("Invalid option. Please choose again.")
