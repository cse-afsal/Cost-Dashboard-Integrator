import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="aws_cost_db",
        user="postgres",
        password="your_password",
        port="5432"
    )
