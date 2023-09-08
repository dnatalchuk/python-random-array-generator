#!/usr/bin/env python3
"""
  This module has the following purposes:
    1. Creates API with 1 endpoint using Flask framework;
    2. Implements POST method only for application/json content type;
    3. Takes a sentence as input and returns a random 500-dimensional array of floats.

Usage example:
    ❯ source env/bin/activate
    ❯ ./app.py
    ❯ curl -X POST -H "Content-Type: application/json" -d '{"sentence": "Hello world"}' http://127.0.0.1:5000/random_array_generator
"""

# Import required libraries
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define the endpoint for generating random 500-dimensional arrays
@app.route('/random_array_generator', methods=['POST'])
def random_array_generator():
    try:
        # Validatig input request:
        input_data = request.json.get('sentence')

        if not input_data:
            return jsonify({"error": "Input is missing"}), 400

        # Generating a random 500-dimensional array of floats
        random_500_array = [random.uniform(0.0, 1.0) for _ in range(500)]
        return jsonify({"result": random_500_array}), 200
    
    except Exception as err:
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run()
