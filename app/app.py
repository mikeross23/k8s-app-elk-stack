from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def get_ip():
    return f"Server IP: {socket.gethostbyname(socket.gethostname())}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
