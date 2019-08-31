from flask import Flask, render_template, request
from random import randrange

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index.html/answer", methods=["GET"])
def fanswer():
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) > num or int(answer) < num:
        return render_template("incorrect.html")
    if int(answer) == num:
        return render_template("correct.html")

@app.route("/index.html/index.html/answer", methods=["GET"])
def sanswer():
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) > num or int(answer) < num:
        return render_template("incorrect.html")
    if int(answer) == num:
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/answer", methods=["GET"])
def tanswer():
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) > num or int(answer) < num:
        return render_template("incorrect.html")
    if int(answer) == num:
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def foanswer():
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) > num or int(answer) < num:
        return render_template("incorrect.html")
    if int(answer) == num:
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def fianswer():
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) > num or int(answer) < num:
        return render_template("incorrect.html")
    if int(answer) == num:
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def sianswer():
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) > num or int(answer) < num:
        return render_template("incorrect.html")
    if int(answer) == num:
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def seanswer():
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) > num or int(answer) < num:
        return render_template("incorrect.html")
    if int(answer) == num:
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def enswer():
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) > num or int(answer) < num:
        return render_template("incorrect.html")
    if int(answer) == num:
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def nanswer():
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) > num or int(answer) < num:
        return render_template("incorrect.html")
    if int(answer) == num:
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def tenanswer():
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) > num or int(answer) < num:
        return render_template("incorrect.html")
    if int(answer) == num:
        return render_template("correct.html")

@app.route("/index.html")
def first():
    x = randrange(100)
    y = randrange(100)
    global num
    num = x + y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/quit.html")
def quit():
    return render_template("quit.html")
@app.route("/index.html/index.html/quit.html")
def quit():
    return render_template("quit.html")
@app.route("/index.html/index.html/index.html/quit.html")
def quit():
    return render_template("quit.html")
@app.route("/index.html/index.html/index.html/index.html/quit.html")
def quit():
    return render_template("quit.html")
@app.route("/index.html/index.html/index.html/index.html/index.html/quit.html")
def quit():
    return render_template("quit.html")
@app.route("/index.html/index.html/index.html/index.html/index.html/quit.html")
def quit():
    return render_template("quit.html")
@app.route("/index.html/index.html/index.html/index.html/index.html/quit.html")
def quit():
    return render_template("quit.html")
@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/quit.html")
def quit():
    return render_template("quit.html")

@app.route("/index.html/index.html")
def second():
    x = randrange(100)
    y = randrange(100)
    global num
    num = x + y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html")
def third():
    x = randrange(100)
    y = randrange(100)
    global num
    num = x + y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html/index.html")
def fourth():
    x = randrange(100)
    y = randrange(100)
    global num
    num = x + y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html/index.html/index.html")
def fifth():
    x = randrange(100)
    y = randrange(100)
    global num
    num = x + y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html")
def sixth():
    x = randrange(100)
    y = randrange(100)
    global num
    num = x + y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html")
def seventh():
    x = randrange(100)
    y = randrange(100)
    global num
    num = x + y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html")
def eighth():
    x = randrange(100)
    y = randrange(100)
    global num
    num = x + y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html")
def ninth():
    x = randrange(100)
    y = randrange(100)
    global num
    num = x + y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html")
def tenth():
    x = randrange(100)
    y = randrange(100)
    global num
    num = x + y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html")
def end():
    return render_template("end.html")
