from flask import Flask
import redis
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        print(f"host: {os.environ.get('REDIS_HOST')}, port: {os.environ.get('REDIS_PORT')}, pw: {os.environ.get('REDIS_PW')}", flush=True)
        r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), password=os.environ.get('REDIS_PW'), db=0)
        count = r.get('count')
        r.set('count', count+1)
        count = r.get('count')
        return f"Count: {count}"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')