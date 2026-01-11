# Cost Dashboard Integrator

## 📌 Project Description
This project integrates AWS resource and cost data stored in a PostgreSQL database
and aggregates it into a structured JSON format. The generated JSON is exposed
through a Flask API endpoint and can be directly consumed by frontend dashboards
for AWS cost visualization and analysis.

---

## 🎯 Objective
- Query and join multiple AWS-related tables from PostgreSQL
- Aggregate AWS cost data by service type and subscription
- Generate frontend-compatible JSON output
- Understand backend and frontend data contracts

---

## 🛠️ Tech Stack
- Python
- Flask
- PostgreSQL
- psycopg2
- GitHub

---

## 🗄️ Database Tables Used
- aws_resources
- aws_costs
- top_cost_resources

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash


git clone https://github.com/your-username/cost-dashboard-integrator.git
cd cost-dashboard-integrator
{
  "submitted_by": "your_muid",
  "grouped_by": "service_type",
  "data": {
    "EC2": {
      "sub-001": [
        {
          "resource_name": "ec2-instance-1",
          "cost": 120.75
        }
      ]
    },
    "S3": {
      "sub-001": [
        {
          "resource_name": "s3-bucket-logs",
          "cost": 45.6
        }
      ]
    }
  }
}

cost-dashboard-integrator/
├── app.py
├── db_config.py
├── generate_json.py
├── requirements.txt
├── README.md
├── sample_output.json
└── screenshots/
    └── json_output.png

---

