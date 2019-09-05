from flask import Flask, render_template, request
from random import randrange
from pygame import mixer

mixer.init()
mixer.music.load("home.mp3")
mixer.music.play()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index.html/answer", methods=["GET", "POST"])
def fanswer():
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) != num:
        return render_template("incorrect.html")
    if int(answer) == num:
        return render_template("correct.html")


@app.route("/index.html")
def first():
    x = randrange(10)
    y = randrange(15)
    global num
    num = x * y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET", "POST">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/quit.html")
def oquit():
    return render_template("quit.html")
