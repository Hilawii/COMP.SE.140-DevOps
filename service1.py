from flask import Flask
import subprocess

app = Flask(__name__)

def make_system_info():
    return{
        "service": "service1",
        "ip address": subprocess.check_output(["hostname", "-I"]).decode("utf-8").strip(),
        "list of running processes": subprocess.check_output(["ps", "-aux"]).decode("utf-8").strip(),
        "available disk space": subprocess.check_output(["df", "-h"]).decode("utf-8").strip(),
        "time since last boot": subprocess.check_output(["uptime", "-p"]).decode("utf-8").strip()
    }

@app.route('/', methods=['GET'])
def get_ssytem_info():
    return make_system_info()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8199)