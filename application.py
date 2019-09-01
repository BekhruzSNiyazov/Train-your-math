from flask import Flask, render_template, request
from random import randrange

app = Flask(__name__)

@app.route("/")
def home():
    #playsound("home.mp3")
    return render_template("home.html")

@app.route("/index.html/answer", methods=["GET", "POST"])
def fanswer():
    from playsound import playsound
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) != num:
        playsound("incorrect.mp3")
        return render_template("incorrect.html")
    if int(answer) == num:
        playsound("correct.mp3")
        return render_template("correct.html")

@app.route("/index.html/index.html/answer", methods=["GET"])
def sanswer():
    from playsound import playsound
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) != num:
        playsound("incorrect.mp3")
        return render_template("incorrect.html")
    if int(answer) == num:
        playsound("correct.mp3")
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/answer", methods=["GET"])
def tanswer():
    from playsound import playsound
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) != num:
        playsound("incorrect.mp3")
        return render_template("incorrect.html")
    if int(answer) == num:
        playsound("correct.mp3")
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def foanswer():
    from playsound import playsound
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) != num:
        playsound("incorrect.mp3")
        return render_template("incorrect.html")
    if int(answer) == num:
        playsound("correct.mp3")
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def fianswer():
    from playsound import playsound
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) != num:
        playsound("incorrect.mp3")
        return render_template("incorrect.html")
    if int(answer) == num:
        playsound("correct.mp3")
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def sianswer():
    from playsound import playsound
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) != num:
        playsound("incorrect.mp3")
        return render_template("incorrect.html")
    if int(answer) == num:
        playsound("correct.mp3")
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def seanswer():
    from playsound import playsound
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) != num:
        playsound("incorrect.mp3")
        return render_template("incorrect.html")
    if int(answer) == num:
        playsound("correct.mp3")
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def enswer():
    from playsound import playsound
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) != num:
        playsound("incorrect.mp3")
        return render_template("incorrect.html")
    if int(answer) == num:
        playsound("correct.mp3")
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def nanswer():
    from playsound import playsound
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) != num:
        playsound("incorrect.mp3")
        return render_template("incorrect.html")
    if int(answer) == num:
        playsound("correct.mp3")
        return render_template("correct.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/answer", methods=["GET"])
def tenanswer():
    from playsound import playsound
    answer = request.args.get("answer")
    print(answer)
    print(num)
    if int(answer) != num:
        playsound("incorrect.mp3")
        return render_template("incorrect.html")
    if int(answer) == num:
        playsound("correct.mp3")
        return render_template("correct.html")

@app.route("/index.html")
def first():
    x = randrange(15)
    y = randrange(15)
    global num
    num = x * y

    return render_template("iindex.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/quit.html")
def oquit():
    return render_template("quit.html")

@app.route("/index.html/index.html/quit.html")
def tquit():
    return render_template("quit.html")

@app.route("/index.html/index.html/index.html/quit.html")
def thquit():
    return render_template("quit.html")

@app.route("/index.html/index.html/index.html/index.html/quit.html")
def fquit():
    return render_template("quit.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/quit.html")
def fiquit():
    return render_template("quit.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/quit.html")
def siquit():
    return render_template("quit.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/quit.html")
def sequit():
    return render_template("quit.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/quit.html")
def equit():
    return render_template("quit.html")

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/quit.html")
def niquit():
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
    x = randrange(10)
    y = randrange(10)
    global num
    num = x * y

    return render_template("iindex.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
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
    x = randrange(10)
    y = randrange(10)
    global num
    num = x * y

    return render_template("iindex.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html")
def sixth():
    x = randrange(1000)
    y = randrange(1000)
    global num
    num = x + y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html")
def seventh():
    x = randrange(10)
    y = randrange(100)
    global num
    num = x * y

    return render_template("iindex.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
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
    num = x * y

    return render_template("iindex.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html")
def tenth():
    x = randrange(500)
    y = randrange(500)
    global num
    num = x + y

    return render_template("index.html", x=x, y=y) + """<form action="index.html/answer" method="GET">
            <input type="number" name="answer" placeholder="Enter answer here" class="ans">
            <button class="ans">Check!</button>
        </form>"""

@app.route("/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html/index.html")
def end():
    return render_template("end.html")
