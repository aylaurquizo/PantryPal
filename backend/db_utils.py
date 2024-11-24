import mysql.connector

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="aws-0-us-west-1.pooler.supabase.com",
            user="postgres.hzktoiokvmegloflfkyv",
            password="pantrypal2024",
            port=6543,
            database="postgres"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        raise
