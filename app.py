import sys
sys.path.append(os.environ['WORKSPACE'])

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!\n'
    
if __name__ == '__main__':
    app.run()
