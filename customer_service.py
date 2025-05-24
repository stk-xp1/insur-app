
def get_customer_detail(mysql, customer_id):
    cur = mysql.connection.cursor()
    query = """
    SELECT
        c.customer_id, c.first_name, c.last_name, c.gender, c.dob, c.address, c.city, c.state, c.zip, c.phone, c.email,
        p.policy_id, p.policy_type, p.policy_start_date, p.policy_end_date, p.premium_amount, p.policy_status,
        a.agent_id, a.first_name AS agent_first_name, a.last_name AS agent_last_name, a.phone AS agent_phone, a.email AS agent_email,
        cl.claim_id, cl.claim_type, cl.claim_date, cl.claim_amount, cl.claim_status,
        pay.payment_id, pay.payment_date, pay.amount_paid, pay.payment_method
    FROM Customers c
    LEFT JOIN Policies p ON c.customer_id = p.customer_id
    LEFT JOIN Policy_Agents pa ON p.policy_id = pa.policy_id
    LEFT JOIN Agents a ON pa.agent_id = a.agent_id
    LEFT JOIN Claims cl ON p.policy_id = cl.policy_id
    LEFT JOIN Payments pay ON p.policy_id = pay.policy_id
    WHERE c.customer_id = %s
    ORDER BY p.policy_id, cl.claim_date, pay.payment_date;
    """
    cur.execute(query, (customer_id,))
    rows = cur.fetchall()
    cur.close()

    if not rows:
        return None

    customer_info = {
        'customer_id': rows[0][0],
        'first_name': rows[0][1],
        'last_name': rows[0][2],
        'gender': rows[0][3],
        'dob': rows[0][4],
        'address': rows[0][5],
        'city': rows[0][6],
        'state': rows[0][7],
        'zip': rows[0][8],
        'phone': rows[0][9],
        'email': rows[0][10],
    }

    policies = {}
    for row in rows:
        policy_id = row[11]
        if policy_id is None:
            continue

        if policy_id not in policies:
            policies[policy_id] = {
                'policy_type': row[12],
                'policy_start_date': row[13],
                'policy_end_date': row[14],
                'premium_amount': row[15],
                'policy_status': row[16],
                'agents': {},
                'claims': {},
                'payments': {}
            }

        agent_id = row[17]
        if agent_id and agent_id not in policies[policy_id]['agents']:
            policies[policy_id]['agents'][agent_id] = {
                'first_name': row[18],
                'last_name': row[19],
                'phone': row[20],
                'email': row[21]
            }

        claim_id = row[22]
        if claim_id and claim_id not in policies[policy_id]['claims']:
            policies[policy_id]['claims'][claim_id] = {
                'claim_type': row[23],
                'claim_date': row[24],
                'claim_amount': row[25],
                'claim_status': row[26]
            }

        payment_id = row[27]
        if payment_id and payment_id not in policies[policy_id]['payments']:
            policies[policy_id]['payments'][payment_id] = {
                'payment_date': row[28],
                'amount_paid': row[29],
                'payment_method': row[30]
            }

    return customer_info, policies
