import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ('<h1>Schlwyn S. Sarabia</h1>'
            '<h1>BSIT - 3A</h1>'
            '<h1>System Integration and Architecture 1</h1>'
            '<h1>Semi-Final Exam</h1>')
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)