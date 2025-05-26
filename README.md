# AgentKit

#  HSN Code Validation Agent using Google ADK Concept

This project implements an intelligent agent designed to validate Harmonized System Nomenclature (HSN) codes using the conceptual framework of Google's Agent Developer Kit (ADK). The agent is built using Python, Flask, and Pandas, and uses a master Excel dataset to verify the validity of input HSN codes.

---

##  Project Objectives

- Validate HSN codes (2- to 8-digit numeric codes) against a master dataset.
- Accept single or multiple HSN code inputs.
- Return validation results in structured JSON format.
- Provide information on valid/invalid codes and their descriptions.
- Demonstrate agent behavior through an API built with Flask.

---

##  Project Structure

HSN-Code-Validation-Agent/
│
├── fulfill.py # Main Flask API application
├── test_api.py # Script to test API with sample HSN codes
├── HSN_SAC.xlsx # Master data containing HSN and SAC codes
├── requirements.txt # Python dependencies
└── README.md # Project overview and instructions

##  Agent Architecture 

- **Intent**: ValidateHSNCode
- **Entities**:
  - `HSNCode`: The code(s) to be validated.
- **Fulfillment**:
  - Logic implemented in `fulfill.py` using Flask and Pandas.
- **Data Store**:
  - Excel file (`HSN_SAC.xlsx`) with known HSN and SAC code mappings.
- **Response**:
  - JSON with code, validity, description (if valid), and reason (if invalid).

 ### How to Run

 1.Install the dependencies  
   pip install -r requirements.txt

 2. Start the Flask Server
    python fulfill.py

 3.Testing the API
   python test_api.py

Sample Response

Status Code: 200
Response JSON: {'validation_result': [{'code': '01', 'description': 'LIVE ANIMALS', 'hierarchy': {'01': 'LIVE ANIMALS'}, 'status': 'Valid'}, {'code': '0101', 'description': 'LIVE HORSES, ASSES, MULES AND HINNIES.', 'hierarchy': {'01': 'LIVE ANIMALS', '0101': 'LIVE HORSES, ASSES, MULES AND HINNIES.'}, 'status': 'Valid'}, {'code': '9954', 'description': 'Construction services', 'hierarchy': {'99': 'All Services', '9954': 'Construction services'}, 'status': 'Valid'}, {'code': '123', 'message': 'HSN code must be numeric and length must be 2, 4, 6, or 8', 'status': 'Invalid Format'}, {'code': '995431', 'description': 'Demolition services', 'hierarchy': {'99': 'All Services', '9954': 'Construction services', '995431': 'Demolition services'}, 'status': 'Valid'}]}

