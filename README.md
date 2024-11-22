# Patient Management System  

A simple Python-based patient management system that allows users to:  
- Add new patients with unique patient numbers, names, and ages.  
- Search for patients by their patient number.  
- Delete existing patient records.  
- Save and load patient data using a JSON file for persistent storage.  

### Features:  
- **Error Handling**: Ensures inputs are valid (e.g., no duplicate patient numbers, no invalid ages or names).  
- **Persistent Data**: Patient data is stored in a JSON file, which is loaded when the program starts and saved when it ends.  
- **UTF-8 Encoding Support**: Handles special characters in names and data.  
- **Customizable Directory**: You can set your file directory for storing the `patients_data.json`.  

### Requirements:  
- Python 3.7 or later.  

### How to Use:  
1. Clone the repository.  
2. Set your working directory in the `os.chdir()` function (replace `"Your\\Path\\Here"` with your path).  
3. Run the script and follow the menu options to add, search, or delete patient records.    

Contributions and feedback are welcome!  
