from flask import Flask, redirect, url_for, render_template, session, request
from youtubekb import YouTubeKeyboardController
from roku import Roku
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
from flask_wtf import Form
from youtubekb import YouTubeKeyBoardForm





roku = Roku('10.1.10.96')

# class FakeRoku:
#     def __init__(self):
#         pass
#     def left(self):
#         pass
#     def right(self):
#         pass
#     def up(self):
#         pass
#     def down(self):
#         pass
#     def select(self):
#         pass
#
# roku = FakeRoku()

@app.route('/')
def discovery():
    try: session['lastKey']
    except: session['lastKey'] = 'A'

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



    if request.method == 'POST':
        currentKey = session['lastKey']
        yt = YouTubeKeyboardController(roku, currentKey)

        phrase = request.form['sendkeys'].upper()
        button_list = yt.type_phrase(phrase, 0.1)
        session['lastKey'] = yt.currentKey

        return render_template("youtubekb.html", lastkey=session['lastKey'], form=form,
                               phrase=phrase, button_list=button_list)
    else:
        return render_template("youtubekb.html", lastkey=session['lastKey'], form=form)


            # yt.input_keys(roku, directions, i)

    # return render_template("youtubekb.html", lastkey = session['LastKey'], form = form, directions=directions, sendkeys = sendkeys )


if __name__ == '__main__':
    app.run(use_reloader=True)

