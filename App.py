import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ('<h1>Schlwyn S. Sarabia</h1>'
            '<h2>BSIT - 3A</h2>'
            '<h3>System Integration and Architecture 1</h3>'
            '<h4>Semi-Final Exam</h4>')
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)