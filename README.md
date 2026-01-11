# Cost Dashboard Integrator

## Objective
Aggregate AWS resource and cost data from PostgreSQL and expose it as JSON for frontend dashboards.

## Tech Stack
- Python
- Flask
- PostgreSQL
- psycopg2

## Setup Instructions
1. Clone the repo
2. Install dependencies
   pip install -r requirements.txt
3. Configure DB credentials in db_config.py
4. Run Flask app
   python app.py

## API Endpoint
GET /api/cost-dashboard

## Example JSON Response
Includes service-wise and subscription-wise AWS costs.

## Tables Used
- aws_resources
- aws_costs
- top_cost_resources

## Submitted By
your_muid
