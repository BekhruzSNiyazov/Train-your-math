from flask import Flask, render_template, request
from random import randrange, choice

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index.html/answer", methods=["GET", "POST"])
def fanswer():
    answer = request.args.get("answer")
    if int(answer) != num:
        print(answer)
        print(num)
        print("INCORRECT!")
        return render_template("incorrect.html")
    if int(answer) == num:
        print(answer)
        print(num)
        print("CORRECT!")
        return render_template("correct.html")

@app.route("/subtraction.html/answer", methods=["GET", "POST"])
def sanswer():
    answer = request.args.get("answer")
    if int(answer) != num:
        print(answer)
        print(num)
        print("INCORRECT!")
        return render_template("sincorrect.html")
    if int(answer) == num:
        print(answer)
        print(num)
        print("CORRECT!")
        return render_template("scorrect.html")

@app.route("/multiplication.html/answer", methods=["GET", "POST"])
def manswer():
    answer = request.args.get("answer")
    if int(answer) != num:
        print(answer)
        print(num)
        print("INCORRECT!")
        return render_template("mincorrect.html")
    if int(answer) == num:
        print(answer)
        print(num)
        print("CORRECT!")
        return render_template("mcorrect.html")

@app.route("/division.html/answer", methods=["GET", "POST"])
def danswer():
    answer = request.args.get("answer")
    if int(answer) != num:
        print(answer)
        print(num)
        print("INCORRECT!")
        return render_template("dincorrect.html")
    if int(answer) == num:
        print(answer)
        print(num)
        print("CORRECT!")
        return render_template("dcorrect.html")

@app.route("/index.html")
def first():
    a = randrange(1000)
    x = randrange(500)
    y = a - x
    global num
    num = a

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET", "POST">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/multiplication.html")
def fmirst():
    a = randrange(100)
    x = randrange(10)
    y = a / x
    global num
    num = a

    return render_template("multiplication.html", x=x, y=y) + """<form action="multiplication.html/answer" method="GET", "POST">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/quit.html")
def oquit():
    return render_template("quit.html")

@app.route("/multiplication.html/quit.html")
def omquit():
    return render_template("quit.html")

@app.route("/division.html/quit.html")
def quit():
    return render_template("quit.html")

@app.route("/subtraction.html/quit.html")
def osquit():
    return render_template("quit.html")

@app.route("/subtraction.html")
def fsirst():
    a = randrange(20)
    x = randrange(100)
    y = x - a
    global num
    num = a

    return render_template("subtraction.html", x=x, y=y) + """<form action="subtraction.html/answer" method="GET", "POST">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/division.html")
def fdirst():
    a = randrange(15)
    b = choice(range(1, 10))
    d = a * b
    global num
    num = a

    return render_template("division.html", x=d, y=b) + """<form action="division.html/answer" method="GET", "POST">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""
