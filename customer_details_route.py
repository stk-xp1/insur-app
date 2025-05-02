from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from extensions import mysql
from customer_service import get_customer_detail

customer_bp = Blueprint('customer_detail', __name__)

@customer_bp.route('/customer_detail', methods=['GET', 'POST'])
def customer_detail_search():
    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        if not customer_id:
            flash('Please enter a Customer ID.', 'error')
            return render_template('customer_detail_search.html')
        return redirect(url_for('customer_detail.customer_detail', customer_id=customer_id))
    return render_template('customer_detail_search.html')

@customer_bp.route('/customer_detail/<customer_id>')
def customer_detail(customer_id):
    result = get_customer_detail(mysql, customer_id)
    if result is None:
        abort(404, description="Customer not found")
    customer_info, policies = result
    return render_template('customer_detail.html', customer=customer_info, policies=policies)
