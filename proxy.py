from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def proxy():
    url = 'https://www.nea.gov.sg/api/ultraviolet/getall'
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return f"Error: {response.status_code}", response.status_code

if __name__ == '__main__':
    app.run()