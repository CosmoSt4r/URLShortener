from app import app
from settings import url_map
from database import db, Url
from flask import render_template, request, redirect


def url_shorting():

    last_url = Url.query.order_by(Url.id)[-1]
    url_id = last_url.id + 1

    short_url = ''
    while url_id > 0:
        short_url += url_map[url_id % 62]
        url_id //= 62
    return short_url


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # POST
        try:
            short_url = request.form['short_url']
            short_url = short_url[short_url.find('/')+1:]

            found_url = Url.query.filter_by(short=short_url).first()
            long_url = found_url.long

            return render_template('index.html', long_url=long_url, short_url=short_url, display='block')
        except:
            long_url = request.form['long_url']

            if long_url:
                if "http" not in long_url:
                    long_url = "https://" + long_url
                if "." not in long_url:
                    long_url = long_url + ".com"

                found_url = Url.query.filter_by(long=long_url).first()

                if not found_url:
                    short_url = url_shorting()

                    new_url = Url(long_url, short_url)
                    db.session.add(new_url)
                    db.session.commit()

                    return render_template('index.html', short_url=short_url, long_url=long_url, display='block')
                else:
                    return render_template('index.html', short_url=found_url.short, long_url=long_url, display='block')

            else:
                return render_template('index.html', display='none')
    else:
        # GET

        return render_template('index.html', display='none')


@app.route("/<url_name>")
def url(url_name):
    found_url = Url.query.filter_by(short=url_name).first()

    return redirect(found_url.long)


if __name__ == '__main__':
    db.create_all()
    app.run()
