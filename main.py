from app import app
from database import db
from flask import render_template, url_for, request, redirect


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # POST
        try:
            short_url = request.form['short_url']
            # long_url = take url from database

            return render_template('index.html', short_url=short_url, display='block')
        except:
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
    else:
        # GET

        return render_template('index.html', display='none')


@app.route("/<url_name>")
def url(url_name):
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run()
