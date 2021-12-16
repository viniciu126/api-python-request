from flask import Flask, request
import requests

app = Flask("API em Python")

@app.route("/user", methods=["GET"])
def showMe():
    response = requests.get("http://localhost:80/user")

    return {
        "status": response.status_code,
        "data": response.json()
    }

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=70)
