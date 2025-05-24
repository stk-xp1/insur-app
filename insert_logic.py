# insert_logic.py
from flask import flash, request
from flask_mysqldb import MySQL

class InsertLogic:
    def __init__(self, mysql):
        self.mysql = mysql

    def insert_customer_logic(self):
        customer_id = request.form.get('customer_id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        gender = request.form.get('gender')
        dob = request.form.get('dob')
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

    def insert_payment_logic(self):
        payment_id = request.form.get('payment_id')
        policy_id = request.form.get('policy_id')
        payment_date = request.form.get('payment_date')
        amount_paid = request.form.get('amount_paid')
        payment_method = request.form.get('payment_method')

        if not (payment_id and policy_id and amount_paid):
            flash('payment_id, policy_id, amount_paid are required.', 'error')
            return False

        try:
            cur = self.mysql.connection.cursor()
            query = """
                INSERT INTO Payments (payment_id, policy_id, payment_date, amount_paid, payment_method)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (payment_id, policy_id, payment_date, amount_paid, payment_method))
            self.mysql.connection.commit()
            cur.close()
            flash('New payment inserted successfully!', 'success')
            return True
        except Exception as e:
            flash(f'Error inserting payment: {e}', 'error')
            return False


    def insert_agent_logic(self):
        agent_id = request.form.get('agent_id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        address = request.form.get('address')

        if not (agent_id and first_name and last_name):
            flash('agent_id, first_name, last_name are required.', 'error')
            return False

        try:
            cur = self.mysql.connection.cursor()
            query = """
                INSERT INTO Payments (agent_id, first_name, last_name, phone, email, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (agent_id, first_name, last_name, phone, email, address))
            self.mysql.connection.commit()
            cur.close()
            flash('New agent inserted successfully!', 'success')
            return True
        except Exception as e:
            flash(f'Error inserting agent: {e}', 'error')
            return False


    def insert_claims_logic(self):
        claim_id = request.form.get('claim_id')
        policy_id = request.form.get('policy_id')
        claim_type = request.form.get('claim_type')
        claim_date = request.form.get('claim_date')
        claim_amount = request.form.get('claim_amount')
        claim_status = request.form.get('claim_status')

        if not (claim_id and policy_id and claim_type):
            flash('claim_id, policy_id, claim_type are required.', 'error')
            return False

        try:
            cur = self.mysql.connection.cursor()
            query = """
                INSERT INTO Payments (claim_id, policy_id, claim_type, claim_date, claim_amount, claim_status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (claim_id, policy_id, claim_type, claim_date, claim_amount, claim_status))
            self.mysql.connection.commit()
            cur.close()
            flash('New claim inserted successfully!', 'success')
            return True
        except Exception as e:
            flash(f'Error inserting claim: {e}', 'error')
            return False


    def insert_adjuster_logic(self):
        adjuster_id = request.form.get('adjuster_id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        experience_years = request.form.get('experience_years')
        phone = request.form.get('phone')
        email = request.form.get('email')

        
        if not (adjuster_id and first_name and last_name and experience_years and phone and email):
            flash('All fields are required.', 'error')
            return False

        try:
            cur = self.mysql.connection.cursor()
            query = """
                INSERT INTO Adjusters (adjuster_id, first_name, last_name, experience_years, phone, email)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (adjuster_id, first_name, last_name, experience_years, phone, email))
            self.mysql.connection.commit()
            cur.close()
            flash('New adjuster inserted successfully!', 'success')
            return True
        except Exception as e:
            flash(f'Error inserting adjuster: {e}', 'error')
            return False
        
    def insert_auto_policies_logic(self):
        auto_policy_id = request.form.get('auto_policy_id')
        policy_id = request.form.get('policy_id')
        make = request.form.get('make')
        model = request.form.get('model')
        year = request.form.get('year')
        liability_amount = request.form.get('liability_amount')
        uninsured_motorist = request.form.get('uninsured_motorist')
        underinsured_motorist = request.form.get('underinsured_motorist')
        med_pay = request.form.get('med_pay')
        collision_damage = request.form.get('collision_damage')
        named_insured = request.form.get('named_insured')
        additional_driver = request.form.get('additional_driver')

        # Basic validation
        required_fields = [auto_policy_id, policy_id, make, model, year, liability_amount, uninsured_motorist, underinsured_motorist, med_pay, collision_damage]
        if not all(required_fields):
            flash('All fields are required.', 'error')
            return False

        try:
            cur = self.mysql.connection.cursor()
            query = """
                INSERT INTO Auto_Policies (
                    auto_policy_id, policy_id, make, model, year, liability_amount,
                    uninsured_motorist, underinsured_motorist, med_pay, collision_damage,
                    named_insured, additional_driver
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (
                auto_policy_id, policy_id, make, model, year, liability_amount,
                uninsured_motorist, underinsured_motorist, med_pay, collision_damage,
                named_insured, additional_driver
            ))
            self.mysql.connection.commit()
            cur.close()
            flash('New auto policy inserted successfully!', 'success')
            return True
        except Exception as e:
            flash(f'Error inserting auto policy: {e}', 'error')
            return False
        

    def insert_beneficiaries_logic(self):
        beneficiary_id = request.form.get('beneficiary_id')
        life_policy_id = request.form.get('life_policy_id')
        beneficiary_name = request.form.get('beneficiary_name')
        relationship = request.form.get('relationship')
        percentage = request.form.get('percentage')
    
        # Basic validation
        if not (beneficiary_id and life_policy_id and beneficiary_name and relationship and percentage):
            flash('All fields are required.', 'error')
            return False
    
        try:
            cur = self.mysql.connection.cursor()
            query = """
                INSERT INTO Beneficiaries (
                    beneficiary_id, life_policy_id, beneficiary_name, relationship, percentage
                )
                VALUES (%s, %s, %s, %s, %s)
            """
            cur.execute(query, (
                beneficiary_id, life_policy_id, beneficiary_name, relationship, percentage
            ))
            self.mysql.connection.commit()
            cur.close()
            flash('New beneficiary inserted successfully!', 'success')
            return True
        except Exception as e:
            flash(f'Error inserting beneficiary: {e}', 'error')
            return False





