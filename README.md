
## Project Description
This project integrates AWS resource and cost data from a PostgreSQL database
and aggregates it into a structured JSON format. The generated JSON is exposed
through a Flask API endpoint and can be used directly in frontend dashboards
for cost visualization.

Objective
##  Objective
- Query multiple AWS-related tables from PostgreSQL
- Aggregate cost data by service and subscription
- Generate structured JSON for frontend integration
- Understand backend–frontend data contracts

Tech Stack Used
## 🛠️ Tech Stack
- Python
- Flask
- PostgreSQL
- psycopg2
- GitHub

## 🗄️ Database Tables
- aws_resources
- aws_costs
- top_cost_resources

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone https://github.com/your-username/cost-dashboard-integrator.git
cd cost-dashboard-integrator

2. Install Dependencies
pip install -r requirements.txt

3. Configure Database

Update database credentials in db_config.py

4. Run Application
python app.py


---


## 📄 Sample JSON Output
```json
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
    }
  }
}


---
```

## Project Structure

## 📁 Project Structure

```
cost-dashboard-integrator/
├── app.py
├── db_config.py
├── generate_json.py
├── requirements.txt
├── README.md
├── sample_output.json
└── screenshots/
└── json_output.png
```
## 📚 Learning Outcomes
- Learned how to query and join multiple PostgreSQL tables
- Understood AWS cost aggregation logic
- Created backend API using Flask<img width="1920" height="1080" alt="Screenshot (2)" src="https://github.com/user-attachments/assets/cf0fe62c-5edf-46b5-827e-6ef96bc00632" />

- Generated frontend-ready JSON data






