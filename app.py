from flask import Flask
import redis
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello World!"

@app.route('/count')
def count():
    try:
        r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), db=0)
        count = r.get('count')
        r.set('count', count+1)
        return f"Count: ${count}"
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')