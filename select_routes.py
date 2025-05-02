from flask import Blueprint, render_template
from extensions import mysql

select_bp = Blueprint('select', __name__)

@select_bp.route('/customers')
def customers():
    cur = mysql.connection.cursor()
    cur.execute('SELECT customer_id, first_name, last_name, gender, dob, address, city, state, zip, phone, email FROM Customers ')
    data = cur.fetchall()
    cur.close()
    return render_template('customers.html', customers=data)

@select_bp.route('/customers_payment')
def c_payment():
    cur = mysql.connection.cursor()
    cur.execute('SELECT payment_id, customer_id, payment_date, amount, payment_method FROM Customer_Payments')
    data = cur.fetchall()
    cur.close()
    return render_template('customers_payment.html', payments=data)

@select_bp.route('/claims')
def claims():
    cur = mysql.connection.cursor()
    cur.execute('SELECT claim_id, policy_id, claim_type, claim_date, claim_amount, claim_status FROM Claims')
    data = cur.fetchall()
    cur.close()
    return render_template('claims.html', claims=data)

@select_bp.route('/policies')
def policies():
    cur = mysql.connection.cursor()
    cur.execute('SELECT policy_id, customer_id, policy_type, policy_start_date, policy_end_date, premium_amount, policy_status FROM Policies')
    data = cur.fetchall()
    cur.close()
    return render_template('policies.html', policies=data)

@select_bp.route('/agents')
def agents():
    cur = mysql.connection.cursor()
    cur.execute('SELECT agent_id, first_name, last_name, phone, email, address FROM Agents')
    data = cur.fetchall()
    cur.close()
    return render_template('agents.html', agents=data)

@select_bp.route('/adjusters')
def adjusters():
    cur = mysql.connection.cursor()
    cur.execute('SELECT adjuster_id, first_name, last_name, experience_years, phone, email FROM Adjusters')
    data = cur.fetchall()
    cur.close()
    return render_template('adjusters.html', adjusters=data)

@select_bp.route('/auto_policies')
def auto_policies():
    cur = mysql.connection.cursor()
    cur.execute('SELECT auto_policy_id, policy_id, make, model, year, liability_amount, uninsured_motorist, underinsured_motorist, med_pay, collision_damage, named_insured, additional_driver FROM Auto_Policies')
    data = cur.fetchall()
    cur.close()
    return render_template('auto_policies.html', auto_policies=data)

@select_bp.route('/beneficiaries')
def beneficiaries():
    cur = mysql.connection.cursor()
    cur.execute('SELECT beneficiary_id, life_policy_id, beneficiary_name, relationship, percentage FROM Beneficiaries')
    data = cur.fetchall()
    cur.close()
    return render_template('beneficiaries.html', beneficiaries=data)

@select_bp.route('/claim_investigations')
def claim_investigations():
    cur = mysql.connection.cursor()
    cur.execute('SELECT investigation_id, claim_id, investigator_name, investigation_date, findings FROM Claim_Investigations')
    data = cur.fetchall()
    cur.close()
    return render_template('claim_investigations.html', claim_investigations=data)

@select_bp.route('/claim_status_history')
def claim_status_history():
    cur = mysql.connection.cursor()
    cur.execute('SELECT claim_id, status, reason_id, status_date FROM Claim_Status_History')
    data = cur.fetchall()
    cur.close()
    return render_template('claim_status_history.html', claim_status_historys=data)

@select_bp.route('/claim_status_reasons')
def claim_status_reasons():
    cur = mysql.connection.cursor()
    cur.execute('SELECT reason_id, reason_description FROM Claim_Status_Reasons')
    data = cur.fetchall()
    cur.close()
    return render_template('claim_status_reasons.html', sclaim_status_reasons=data)

@select_bp.route('/claims_adjusters')
def claims_adjusters():
    cur = mysql.connection.cursor()
    cur.execute('SELECT claim_id, adjuster_id FROM Claims_Adjusters ')
    data = cur.fetchall()
    cur.close()
    return render_template('claims_adjusters.html',claims_adjusters=data)

@select_bp.route('/customer_payments')
def customer_payments():
    cur = mysql.connection.cursor()
    cur.execute('SELECT payment_id, customer_id, payment_date, amount, payment_method FROM  Customer_Payments')
    data = cur.fetchall()
    cur.close()
    return render_template('customer_payments.html',customer_payments=data)

@select_bp.route('/homeowners_policies')
def homeowners_policies():
    cur = mysql.connection.cursor()
    cur.execute('SELECT homeowners_policy_id, policy_id, liability_amount, property_damage_amount, premium FROM Homeowners_Policies')
    data = cur.fetchall()
    cur.close()
    return render_template('homeowners_policies.html',homeowners_policies=data)

@select_bp.route('/life_insurance_policies')
def life_insurance_policies():
    cur = mysql.connection.cursor()
    cur.execute('SELECT life_policy_id, policy_id, premium_amount, benefit_amount, beneficiary FROM Life_Insurance_Policies')
    data = cur.fetchall()
    cur.close()
    return render_template('life_insurance_policies.html',life_insurance_policies=data)

@select_bp.route('/payments')
def payments():
    cur = mysql.connection.cursor()
    cur.execute('SELECT payment_id, policy_id, payment_date, amount_paid, payment_method FROM Payments')
    data = cur.fetchall()
    cur.close()
    return render_template('payments.html',payments=data)

@select_bp.route('/policy_agents')
def policy_agents():
    cur = mysql.connection.cursor()
    cur.execute('SELECT policy_id, agent_id FROM Policy_Agents')
    data = cur.fetchall()
    cur.close()
    return render_template('policy_agents.html',policy_agents=data)

@select_bp.route('/policy_coverages')
def policy_coverages():
    cur = mysql.connection.cursor()
    cur.execute('SELECT coverage_id, policy_id, coverage_type, coverage_limit, premium FROM Policy_Coverages ')
    data = cur.fetchall()
    cur.close()
    return render_template('policy_coverages.html',policy_coverages=data)

@select_bp.route('/policy_reinsurance')
def policy_reinsurance():
    cur = mysql.connection.cursor()
    cur.execute('SELECT policy_id, contract_id FROM Policy_Reinsurance')
    data = cur.fetchall()
    cur.close()
    return render_template('policy_reinsurance.html',policy_reinsurances=data)

@select_bp.route('/reinsurance_contracts')
def reinsurance_contracts():
    cur = mysql.connection.cursor()
    cur.execute('SELECT contract_id, reinsurer_name, contract_start_date, contract_end_date, contract_amount FROM Reinsurance_Contracts')
    data = cur.fetchall()
    cur.close()
    return render_template('reinsurance_contracts.html',reinsurance_contracts=data)

@select_bp.route('/renters_policies')
def renters_policies():
    cur = mysql.connection.cursor()
    cur.execute('SELECT renters_policy_id, policy_id, liability_amount, property_damage_amount, premium FROM Renters_Policies')
    data = cur.fetchall()
    cur.close()
    return render_template('renters_policies.html',renters_policies=data)
