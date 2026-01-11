import json
from db_config import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

cursor.execute("""
    SELECT r.service_type, r.resource_name, SUM(c.cost)
    FROM aws_resources r
    JOIN aws_costs c ON r.resource_id = c.resource_id
    GROUP BY r.service_type, r.resource_name;
""")

rows = cursor.fetchall()

output = {
    "submitted_by": "your_muid",
    "grouped_by": "service_type",
    "services": {}
}

for service, resource, cost in rows:
    output["services"].setdefault(service, [])
    output["services"][service].append({
        "resource": resource,
        "cost": float(cost)
    })

with open("sample_output.json", "w") as f:
    json.dump(output, f, indent=4)

cursor.close()
conn.close()
