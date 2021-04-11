app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")


@app.route("/failure")
def failure():
    return render_template("failure.html")


if __name__ == "__main__":
    app.run(debug=True)