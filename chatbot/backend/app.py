from flask import Flask, request, jsonify
from flask_cors import CORS
from nlp import engine

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint to handle chat messages."""
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Missing message field'}), 400

    user_message = data['message']
    bot_response = engine.get_response(user_message)
    return jsonify({'response': bot_response})

@app.route('/health', methods=['GET'])
def health():
    """Simple health check endpoint."""
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
