import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def post_pig_lat(rand_post):
    response = requests.post("http://hidden-journey-62459.herokuapp.com/piglatinize/",
                             data={'input_text': rand_post}, allow_redirects=True)
    return response.text


@app.route('/')
def home():
    fact = get_fact()
    return post_pig_lat(fact)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

