
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
## Tech Stack
- Python
- Flask
- PostgreSQL
- psycopg2
- GitHub

## Database Tables
- aws_resources
- aws_costs
- top_cost_resources

##  Setup Instructions

### 1. Clone Repository

git clone https://github.com/cse-afsal/cost-dashboard-integrator.git
cd cost-dashboard-integrator

2. Install Dependencies
pip install -r requirements.txt

3. Configure Database

4. Run Application
python app.py


---


##  Sample JSON Output
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



```
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
---
## 📚 Learning Outcomes
- Learned how to query and join multiple PostgreSQL tables
- Understood AWS cost aggregation logic
- Generated frontend-ready JSON data
- ---   screenshots
- ---

<img width="1860" height="961" alt="Screenshot 2026-01-11 153856" src="https://github.com/user-attachments/assets/9a009122-593e-42d7-b23d-d9fb74fadabd" />





<img width="1505" height="953" alt="Screenshot 2026-01-11 154156" src="https://github.com/user-attachments/assets/b4a2edf3-b827-400d-9e5c-6f8606c4d85b" />





