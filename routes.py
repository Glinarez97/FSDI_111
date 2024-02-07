from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name": "Gerardo",
        "last_name": "Linarez",
        "hobbies": "DIY stuff",
        "online": True
    }
    return me