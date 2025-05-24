# Insurance Management Application

This Flask web app allows viewing and inserting data in an insurance database.

---

## Setup Instructions

1. **Database Setup**

   Download the provided SQL dump file containing the full database schema and data:


    insurance_database.sql

2. **Import Database**

On your local machine, import the SQL file into your MySQL server:

    mysql -u your_username -p your_database_name < insurance_database.sql


Replace `your_username` and `your_database_name` with your MySQL credentials and target database.

---

## Tables Included

- Adjusters  
- Agents  
- Auto_Policies  
- Beneficiaries  
- Claim_Investigations  
- Claim_Status_History  
- Claim_Status_Reasons  
- Claims  
- Claims_Adjusters  
- Customer_Payments  
- Customers  
- Homeowners_Policies  
- Life_Insurance_Policies  
- Payments  
- Policies  
- Policy_Agents  
- Policy_Coverages  
- Policy_Reinsurance  
- Reinsurance_Contracts  
- Renters_Policies  

---

## Running the Application

1. Install dependencies:

    pip install flask flask-mysqldb


2. Configure your MySQL connection in `app.py` (if needed) to match your local setup.

3. Run the Flask app:

    python app.py

4. Open your browser at `http://127.0.0.1:5000/` to access the app.

