
from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template('index.html')


@app.get("/SQLstatements")
def sql():
    return render_template('statements.html')


@app.get("/About")
def about():
    me = {
        "first_name": "Sebastian",
        "last_name": "Lopez-Wells",
        "hobbies": "Baseball, literature, Programming",
        "bio": "My name is Sebastian Lopez Wells and I am a student in ITT and SDGKU's online courses."
    }
    return render_template('about.html', about_dict=me)
