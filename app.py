from flask import Flask, redirect, url_for, render_template, session, request
import time
from youtubekb import YouTubeKeyboardController
import youtubekb
from roku import Roku


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
from flask_wtf import Form
from youtubekb import YouTubeKeyBoardForm





roku = Roku('10.1.10.96')

@app.route('/')
def discovery():
    session['YouTubeLastLetter'] = 'A'
    return redirect(url_for('youtubekeyboard'))


@app.route('/listapps')
def listapps():
    apps = roku.apps
    return render_template("listapps.html", apps = apps)

@app.route('/youtubekb', methods=['GET','POST'])
def youtubekeyboard():
    # roku['YouTube'].launch()
    # time.sleep(15)
    form = YouTubeKeyBoardForm()

    yt = YouTubeKeyboardController(roku)

    if request.method == 'POST':
        directions = []

        # request.form['sendkeys'].upper()

        #    session['LastKey'] = i

        return render_template("youtubekb.html", lastkey=session['LastKey'], form=form, directions=directions,
                               sendkeys=sendkeys)
    else:
        return render_template("youtubekb.html", lastkey=session['LastKey'], form=form)


            # yt.input_keys(roku, directions, i)

    # return render_template("youtubekb.html", lastkey = session['LastKey'], form = form, directions=directions, sendkeys = sendkeys )


if __name__ == '__main__':
    app.run(use_reloader=True)

