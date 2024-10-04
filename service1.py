from flask import Flask
import requests
import subprocess

app = Flask(__name__)


def call_service_2():
    try:
        response = requests.get("http://service2:8200")
        return response.json()
    except requests.exceptions.RequestException as e:
        return {e}


@app.route('/', methods=['GET'])
def get_ssytem_info():
    service_1 = {
        "ip address": subprocess.check_output(["hostname", "-I"]).decode("utf-8").strip(),
        "list of running processes": subprocess.check_output(["ps", "-aux"]).decode("utf-8").strip(),
        "available disk space": subprocess.check_output(["df", "-h"]).decode("utf-8").strip(),
        "time since last boot": subprocess.check_output(["uptime", "-p"]).decode("utf-8").strip()
    }
    service_2 = call_service_2()

    combined = {"service1": service_1,
                "service2": service_2}

    return combined



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8199)