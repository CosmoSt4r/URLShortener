from app import app
from database import db
from flask import render_template, url_for, request


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # GET

        return render_template('index.html', display='none')
    else:
        # POST
        long_url = request.form['long_url']

        if long_url:
            if "http" not in long_url:
                long_url = "https://" + long_url
            if "." not in long_url:
                long_url = long_url + ".com/"

            short_url = long_url[:10]  # # # # #
        else:
            return render_template('index.html', display='none')

        return render_template('index.html', short_url=short_url, long_url=long_url, display='block')


@app.route("/<url_name>", methods=['GET', 'POST'])
def url(url_name):
    return f'<h1>{url_name}</h1>'


if __name__ == '__main__':
    db.create_all()
    app.run()
