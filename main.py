# flask application
from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    with open('data.json', 'w') as f:
        json.dump(data, f)
    return 'Data submitted successfully!'
if __name__ == '__main__':
    app.run(debug=True)