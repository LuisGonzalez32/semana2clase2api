from flask import Flask, render_template
from restapi import MtgRestApi

app = Flask(__name__)


@app.route("/")
def home():
    service = MtgRestApi()
    cards = service.getMtgCards()
    return render_template("index.html", mtgCards=cards)


if __name__ == "__main__":
    app.run(debug=True)