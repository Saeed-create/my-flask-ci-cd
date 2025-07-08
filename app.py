# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, CI/CD World from Flask on EC2!'

@app.route('/test')
def test_route():
    return 'This is a test route!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # Listen on all interfaces, port 5000    
