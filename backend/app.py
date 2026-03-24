from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow GitHub Pages to call this backend

# ═══ HEALTH CHECK ═══
@app.route('/health', methods=['GET'])
def health():
    return {"status": "online", "version": "1.0.0"}, 200

# ═══ AUTH (simple for now) ═══
@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    return {
        "success": True, 
        "userId": "user_123",
        "message": f"Welcome {email}"
    }, 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    
    return {
        "success": True,
        "userId": "user_123",
        "token": "jwt_token_here"
    }, 200

# ═══ PORTFOLIO ═══
@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    user_id = request.args.get('user_id')
    return {
        "portfolio": []
    }, 200

@app.route('/api/portfolio', methods=['POST'])
def add_to_portfolio():
    data = request.json
    return {
        "success": True,
        "id": "portfolio_item_123"
    }, 201

# ═══ WATCHLIST ═══
@app.route('/api/watchlist', methods=['GET'])
def get_watchlist():
    user_id = request.args.get('user_id')
    return {"watchlist": []}, 200

@app.route('/api/watchlist', methods=['POST'])
def add_to_watchlist():
    data = request.json
    return {"success": True}, 201

# ═══ PRICE HISTORY ═══
@app.route('/api/prices/<card_id>', methods=['GET'])
def get_price_history(card_id):
    days = request.args.get('days', 30, type=int)
    return {
        "card_id": card_id,
        "history": []
    }, 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
