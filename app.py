from flask import Flask, render_template
from insert_routes import insert_bp
from customer_details_route import customer_bp
from select_routes import select_bp
from extensions import mysql

app = Flask(__name__)
app.secret_key = 'Kiram0B0kh0r009878!!'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Qazwsxedc78!!'
app.config['MYSQL_DB'] = 'insurance'

mysql.init_app(app)

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

app.register_blueprint(customer_bp)
app.register_blueprint(select_bp)
app.register_blueprint(insert_bp)

@app.route('/')
def index():
    return render_template('index.html', tables=tables)

@app.route('/dev_info')
def dev_info():
    return render_template('dev_info.html')

if __name__ == '__main__':
    app.run(debug=True)
