from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

# Retrieve the API key from environment variables
API_KEY = os.getenv("API_KEY")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Sports Data API!"

@app.route('/get-data', methods=['GET'])
def get_data():
    # Example of fetching data from an external API using the API_KEY
    api_url = "https://api.example.com/sports?api_key=" + API_KEY
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()  # Assuming the external API returns JSON
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)