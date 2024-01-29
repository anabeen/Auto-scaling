from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Run the CPU stress script as a separate process
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return 'CPU stress process started.', 200

@app.route('/', methods=['GET'])
def get_private_ip():
    # Get the private IP address
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
