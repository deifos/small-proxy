from flask import Flask, jsonify
import requests
from flask_cors import CORS  

app = Flask(__name__)
CORS(app) 
@app.route('/')
def proxy():
    url = 'https://www.nea.gov.sg/api/ultraviolet/getall'
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify({"result": response.json()})
    else:
        return f"Error: {response.status_code}", response.status_code

if __name__ == '__main__':
    app.run()
