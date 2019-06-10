from flask import Flask, redirect, url_for, render_template, session, request
from youtubekb import YouTubeKeyboardController
from roku import Roku
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
from flask_wtf import Form
from youtubekb import YouTubeKeyBoardForm





roku = Roku('10.1.10.96')

@app.route('/')
def discovery():
    session['lastKey'] = 'A'
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
        currentKey = session['lastKey']
        sendkeys = request.form['sendkeys'].upper()
        button_list = yt.type_phrase(sendkeys, currentKey)
        session['lastKey'] = yt.currentKey

        return render_template("youtubekb.html", lastkey=session['lastKey'], form=form,
                               sendkeys=sendkeys, button_list = button_list)
    else:
        return render_template("youtubekb.html", lastkey=session['lastKey'], form=form)


            # yt.input_keys(roku, directions, i)

    # return render_template("youtubekb.html", lastkey = session['LastKey'], form = form, directions=directions, sendkeys = sendkeys )


if __name__ == '__main__':
    app.run(use_reloader=True)

