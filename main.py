from app import app
from database import db


@app.route("/", methods=['GET', 'POST'])
def index():
    return '<h1> Hello </h1>'


if __name__ == '__main__':
    db.create_all()
    app.run()
