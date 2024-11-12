# app.py

import os
from flask import Flask
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username and "top" output
    username = os.getenv('USER', 'Unknown')
    top_output = subprocess.getoutput("top -b -n 1 | head -n 10")
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')

    # HTML response format
    response = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> Krishnandan pandit</p>
    <p><strong>Username:</strong> {username}</p>s
    <p><strong>Server Time in IST:</strong> {current_time}</p>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
