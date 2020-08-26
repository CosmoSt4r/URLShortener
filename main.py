from app import app
from database import db
from flask import render_template, url_for


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/<url_name>", methods=['GET', 'POST'])
def url(url_name):
    return f'<h1>{url_name}</h1>'


if __name__ == '__main__':
    db.create_all()
    app.run()
