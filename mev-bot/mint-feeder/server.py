from flask import Flask, jsonify
import json
import os

app = Flask(__name__)
TOKEN_FILE = 'tokens.json'

def load_tokens():
    if not os.path.exists(TOKEN_FILE):
        return []
    with open(TOKEN_FILE, 'r') as f:
        return json.load(f)

def save_tokens(tokens):
    with open(TOKEN_FILE, 'w') as f:
        json.dump(tokens, f)

@app.route('/tokens', methods=['GET'])
def get_tokens():
    tokens = load_tokens()
    return jsonify(tokens)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18080)
