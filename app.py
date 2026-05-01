from flask import Flask, jsonify

app=Flask(__name__)
@app.route('/')
def home():
    return "App V1 Running Successfully!"
@app.route('/users')
def users():
    return jsonify([
        {"name": "User1"},
        {"name": "User2"},
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
