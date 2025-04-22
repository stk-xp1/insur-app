# insert_logic.py
from flask import flash, request
from flask_mysqldb import MySQL  # Import MySQL here

class InsertLogic:
    def __init__(self, mysql):
        self.mysql = mysql

    def insert_customer_logic(self):
        customer_id = request.form.get('customer_id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        gender = request.form.get('gender')
        dob = request.form.get('dob')  # Format: YYYY-MM-DD
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        zip_code = request.form.get('zip')
        phone = request.form.get('phone')
        email = request.form.get('email')

        if not (customer_id and first_name and last_name):
            flash('Customer ID, First Name and Last Name are required.', 'error')
            return False

        try:
            cur = self.mysql.connection.cursor()
            query = """
                INSERT INTO Customers (customer_id, first_name, last_name, gender, dob, address, city, state, zip, phone, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (customer_id, first_name, last_name, gender, dob, address, city, state, zip_code, phone, email))
            self.mysql.connection.commit()
            cur.close()
            flash('New customer inserted successfully!', 'success')
            return True
        except Exception as e:
            flash(f'Error inserting customer: {e}', 'error')
            return False

    def insert_policy_logic(self):
        policy_id = request.form.get('policy_id')
        customer_id = request.form.get('customer_id')
        policy_type = request.form.get('policy_type')
        policy_start_date = request.form.get('policy_start_date')
        policy_end_date = request.form.get('policy_end_date')
        premium_amount = request.form.get('premium_amount')
        policy_status = request.form.get('policy_status')

        if not (policy_id and customer_id and policy_type):
            flash('Policy ID, Customer ID, and Policy Type are required.', 'error')
            return False

        try:
            cur = self.mysql.connection.cursor()
            query = """
                INSERT INTO Policies (policy_id, customer_id, policy_type, policy_start_date, policy_end_date, premium_amount, policy_status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (policy_id, customer_id, policy_type, policy_start_date, policy_end_date, premium_amount, policy_status))
            self.mysql.connection.commit()
            cur.close()
            flash('New policy inserted successfully!', 'success')
            return True
        except Exception as e:
            flash(f'Error inserting policy: {e}', 'error')
            return False

