from flask import Flask, render_template
import util.network
import api
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)-8s | %(name)-15s | %(funcName)15s() | %(message)s'
)

app = Flask(__name__)


@app.route("/")
def home():
    logger.info('return render_template("index.html", all_posts=api.gest_posts(api.URL))')
    return render_template("index.html", all_posts=api.gest_posts(api.URL))


@app.route("/about")
def about():
    logger.info('return render_template("about.html")')
    return render_template("about.html")


@app.route("/contact")
def contact():
    logger.info('return render_template("contact.html")')
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, host=util.network.get_ipaddress())
