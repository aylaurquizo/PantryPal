from flask import Flask
from flask_cors import CORS
from supabase import create_client
from routes.meal import MealRoutes  
from routes.user import UserRoutes

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ayla'
app.config['CORS_HEADERS'] = 'Content-Type'

# Allow CORS for all routes with specific origin
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173"]}})

# Manually add CORS headers to all responses
@app.after_request
def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:5173")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS")
    return response

# Initialize Supabase client
SUPABASE_URL = "https://hzktoiokvmegloflfkyv.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh6a3RvaW9rdm1lZ2xvZmxma3l2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIzODI4NTcsImV4cCI6MjA0Nzk1ODg1N30.s9W81XXaWlxVIru3eglisZBXx2uhHe1A76EfucGjbAI"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Register routes
UserRoutes(app, supabase)
MealRoutes(app, supabase)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
