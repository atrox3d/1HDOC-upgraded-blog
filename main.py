from flask import (
    Flask,
    render_template,
    request,
    Request
)
import util.network
import util.params
import api
import functools
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(name)-15s | %(funcName)15s() | %(message)s'
)


def log_decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        logger.info(f"calling {fn.__name__}({util.params.params2str(*args, **kwargs)})")
        retval = fn(*args, **kwargs)
        logger.info(f"return value: {retval}")
        return retval

    return wrapper


app = Flask(__name__)


@app.route("/")
@log_decorator
def home():
    logger.info('return render_template("index.html", all_posts=api.gest_posts(api.URL))')
    return render_template("index.html", all_posts=api.gest_posts(api.URL))


@app.route("/post/<int:id>")
@log_decorator
def post(id):
    post = api.get_post(id, api.URL)
    return render_template("post.html", post=post)


@app.route("/about")
@log_decorator
def about():
    logger.info('return render_template("about.html")')
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
@log_decorator
def contact():
    if request.method == "GET":
        logger.info('return render_template("contact.html")')
        return render_template("contact.html")
    elif request.method == "POST":
        logger.info(f'return render_template("contact.html", {util.params.kwargs2str(**request.form)})')
        return render_template("contact.html", **request.form)


if __name__ == "__main__":
    app.run(debug=True, host=util.network.get_ipaddress())
