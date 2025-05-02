from flask import Blueprint, render_template, request, redirect, abort, url_for
from insert_logic import InsertLogic
from extensions import mysql

insert_bp = Blueprint('insert', __name__)
insert_logic = InsertLogic(mysql)

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

@insert_bp.route('/insert_select_table')
def insert_select_table():
    # Render page to select which table to insert into
    return render_template('insert_select_table.html', tables=tables)

@insert_bp.route('/insert/<table_name>', methods=['GET', 'POST'])
def insert_table_form(table_name):
    table_name = table_name.lower()
    if table_name not in [t.lower() for t in tables]:
        abort(404)

    if table_name == 'customers':
        if request.method == 'POST':
            success = insert_logic.insert_customer_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                # On failure, re-render the form with flash messages
                return render_template('insert_customer.html')
        # GET request: render the insert customer form
        return render_template('insert_customer.html')


    if table_name == 'policies':
        if request.method == 'POST':
            success = insert_logic.insert_policy_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('insert_policy.html')
        return render_template('insert_policy.html')

    if table_name == 'payments':
        if request.method == 'POST':
            success = insert_logic.insert_payment_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('insert_payment.html')
        return render_template('insert_payment.html')

    if table_name == 'agents':
        if request.method == 'POST':
            success = insert_logic.insert_agent_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('insert_agents.html')
        return render_template('insert_agents.html')

    if table_name == 'claims':
        if request.method == 'POST':
            success = insert_logic.insert_claims_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('insert_claims.html')
        return render_template('insert_claims.html')

    # work from here
    if table_name == 'auto_policies':
        if request.method == 'POST':
            success = insert_logic.insert_auto_policies_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('insert_auto_policies.html')
        return render_template('insert_auto_policies.html')


    if table_name == 'beneficiaries':
        if request.method == 'POST':
            success = insert_logic.insert_beneficiaries_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('insert_beneficiaries.html')
        return render_template('insert_beneficiaries.html')


    if table_name == 'claims_Adjusters':
        if request.method == 'POST':
            success = insert_logic.insert_claims_Adjusters_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('insert_claims_Adjusters.html')
        return render_template('insert_claims_Adjusters.html')


    if table_name == 'customer_payments':
        if request.method == 'POST':
            success = insert_logic.insert_customer_payments_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('insert_customer_payments.html')
        return render_template('insert_customer_payments.html')

    if table_name == 'claim_investigations':
        if request.method == 'POST':
            success = insert_logic.insert_claim_investigations_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('insert_claim_investigations.html')
        return render_template('insert_claim_investigations.html')

    if table_name == 'claim_status_history':
        if request.method == 'POST':
            success = insert_logic.insert_claim_status_history_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('insert_claim_status_history.html')
        return render_template('insert_claim_status_history.html')


    if table_name == 'claim_status_reasons':
        if request.method == 'POST':
            success = insert_logic.insert_claim_status_reasons_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('claim_status_reasons.html')
        return render_template('insert_claim_status_reasons.html')

    if table_name == 'homeowners_policies':
        if request.method == 'POST':
            success = insert_logic.insert_homeowners_policies_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('homeowners_policies.html')
        return render_template('homeowners_policies.html')


    if table_name == 'homeowners_policies':
        if request.method == 'POST':
            success = insert_logic.insert_homeowners_policies_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('homeowners_policies.html')
        return render_template('homeowners_policies.html')


    if table_name == 'life_lnsurance_policies':
        if request.method == 'POST':
            success = insert_logic.insert_life_lnsurance_policies_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('life_lnsurance_policies.html')
        return render_template('life_lnsurance_policies.html')


    if table_name == 'renters_policies':
        if request.method == 'POST':
            success = insert_logic.insert_renters_policies_logic()  # Call method using the instance
            if success:
                return redirect(url_for('index'))
            else:
                return render_template('renters_policies.html')
        return render_template('renters_policies.html')


    # Auto_Policies, Beneficiaries, claims_Adjusters , customer_payments, claim_investigations, renters_policies
    # claim_status_history, claim_status_reasons, homeowners_policies, life_lnsurance_policies
    # Placeholder for other tables - to be implemented
    return f"Insert form for '{table_name}' not implemented yet.", 501
