from flask import Flask, jsonify
from db_config import get_db_connection

app = Flask(__name__)

@app.route("/api/cost-dashboard")
def cost_dashboard():
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT r.service_type, r.subscription_id, r.resource_name, SUM(c.cost)
    FROM aws_resources r
    JOIN aws_costs c ON r.resource_id = c.resource_id
    GROUP BY r.service_type, r.subscription_id, r.resource_name;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    result = {}

    for service, sub, resource, cost in rows:
        result.setdefault(service, {})
        result[service].setdefault(sub, [])
        result[service][sub].append({
            "resource_name": resource,
            "cost": float(cost)
        })

    response = {
        "submitted_by": "your_muid",
        "grouped_by": "service_type",
        "data": result
    }

    cursor.close()
    conn.close()

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
