from flask import Flask, jsonify, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Qazwsxedc78!!'
app.config['MYSQL_DB'] = 'insurance'

mysql = MySQL(app)

@app.route('/')
def index():
    tables = [
        "Adjusters",
        "Agents",
        "Auto_Policies",
        "Beneficiaries",
        "Claim_Investigations",
        "Claim_Status_History",
        "Claim_Status_Reasons",
        "Claims",
        "Claims_Adjusters",
        "Customer_Payments",
        "Customers",
        "Homeowners_Policies",
        "Life_Insurance_Policies",
        "Payments",
        "Policies",
        "Policy_Agents",
        "Policy_Coverages",
        "Policy_Reinsurance",
        "Reinsurance_Contracts",
        "Renters_Policies"
    ]
    return render_template('index.html', tables=tables)


@app.route('/customers')
def customers():
    cur = mysql.connection.cursor()
    cur.execute('SELECT customer_id, first_name, last_name, gender, dob, address, city, state, zip, phone, email FROM Customers ')
    data = cur.fetchall()
    cur.close()
    return render_template('customers.html', customers=data)

@app.route('/customers_payment')
def c_payment():
    cur = mysql.connection.cursor()
    cur.execute('SELECT payment_id, customer_id, payment_date, amount, payment_method FROM Customer_Payments')
    data = cur.fetchall()
    cur.close()
    return render_template('customers_payment.html', payments=data)

@app.route('/claims')
def claims():
    cur = mysql.connection.cursor()
    cur.execute('SELECT claim_id, policy_id, claim_type, claim_date, claim_amount, claim_status FROM Claims')
    data = cur.fetchall()
    cur.close()
    return render_template('claims.html', claims=data)

@app.route('/policies')
def policies():
    cur = mysql.connection.cursor()
    cur.execute('SELECT policy_id, customer_id, policy_type, policy_start_date, policy_end_date, premium_amount, policy_status FROM Policies')
    data = cur.fetchall()
    cur.close()
    return render_template('policies.html', policies=data)

@app.route('/agents')
def agents():
    cur = mysql.connection.cursor()
    cur.execute('SELECT agent_id, first_name, last_name, phone, email, address FROM Agents')
    data = cur.fetchall()
    cur.close()
    return render_template('agents.html', agents=data)

@app.route('/adjusters')
def adjusters():
    cur = mysql.connection.cursor()
    cur.execute('SELECT adjuster_id, first_name, last_name, experience_years, phone, email FROM Adjusters')
    data = cur.fetchall()
    cur.close()
    return render_template('adjusters.html', adjusters=data)

@app.route('/auto_policies')
def auto_policies():
    cur = mysql.connection.cursor()
    cur.execute('SELECT auto_policy_id, policy_id, make, model, year, liability_amount, uninsured_motorist, underinsured_motorist, med_pay, collision_damage, named_insured, additional_driver FROM Auto_Policies')
    data = cur.fetchall()
    cur.close()
    return render_template('auto_policies.html', auto_policies=data)

@app.route('/beneficiaries')
def beneficiaries():
    cur = mysql.connection.cursor()
    cur.execute('SELECT beneficiary_id, life_policy_id, beneficiary_name, relationship, percentage FROM Beneficiaries')
    data = cur.fetchall()
    cur.close()
    return render_template('beneficiaries.html', beneficiaries=data)

@app.route('/claim_investigations')
def claim_investigations():
    cur = mysql.connection.cursor()
    cur.execute('SELECT investigation_id, claim_id, investigator_name, investigation_date, findings FROM Claim_Investigations')
    data = cur.fetchall()
    cur.close()
    return render_template('claim_investigations.html', claim_investigations=data)

@app.route('/claim_status_history')
def claim_status_history():
    cur = mysql.connection.cursor()
    cur.execute('SELECT claim_id, status, reason_id, status_date FROM Claim_Status_History')
    data = cur.fetchall()
    cur.close()
    return render_template('claim_status_history.html', claim_status_historys=data)

@app.route('/claim_status_reasons')
def claim_status_reasons():
    cur = mysql.connection.cursor()
    cur.execute('SELECT reason_id, reason_description FROM Claim_Status_Reasons')
    data = cur.fetchall()
    cur.close()
    return render_template('claim_status_reasons.html', sclaim_status_reasons=data)

@app.route('/claims_adjusters')
def claims_adjusters():
    cur = mysql.connection.cursor()
    cur.execute('SELECT claim_id, adjuster_id FROM Claims_Adjusters ')
    data = cur.fetchall()
    cur.close()
    return render_template('claims_adjusters.html',claims_adjusters=data)

@app.route('/customer_payments')
def customer_payments():
    cur = mysql.connection.cursor()
    cur.execute('SELECT payment_id, customer_id, payment_date, amount, payment_method FROM  Customer_Payments')
    data = cur.fetchall()
    cur.close()
    return render_template('customer_payments.html',customer_payments=data)

if __name__ == '__main__':
    app.run(debug=True)

