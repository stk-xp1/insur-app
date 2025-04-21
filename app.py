from flask import Flask, jsonify, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Qazwsxedc78!!'
app.config['MYSQL_DB'] = 'insurance'

mysql = MySQL(app)

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

if __name__ == '__main__':
    app.run(debug=True)

