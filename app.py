from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        import redis
        r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), username=os.environ.get('REDIS_USER'), password=os.environ.get('REDIS_PW'), db=0)
        count = r.get('count')
        r.set('count', count+1)
        return f"Count: {count}"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')