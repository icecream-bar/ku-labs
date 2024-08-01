from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/rce', methods=['GET'])
def rce():
    cmd = request.args.get('cmd')
    if cmd:
        return os.popen(cmd).read()
    return "Please provide a command."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

