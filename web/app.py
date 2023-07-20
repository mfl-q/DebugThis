from flask import Flask
from redis import Redis
import socket

app = Flask(__name__)
redis = Redis(host='redis', port=1111)

@app.route('/')
def hello():
    redis.incr('hit')
    counter = str(redis.get('hits'),'utf-8')
    hostname = socket.gethostname()
    return f"{hostname}: This webpage has been viewed {counter} time(s)"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
