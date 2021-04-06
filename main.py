from flask import Flask, render_template
import util.network

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host=util.network.get_ipaddress())
