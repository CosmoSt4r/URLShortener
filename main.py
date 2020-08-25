from app import app
from database import db
from flask import render_template, url_for


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    db.create_all()
    app.run()
