from flask import Flask, redirect, url_for, render_template, session
import time
from youtube_functions import youtube_search_cursor
import youtube_functions as yt
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'


from roku import Roku

roku = Roku('10.1.10.96')

@app.route('/')
def discovery():
    session['LastKey'] = 'A'
    return redirect(url_for('youtubekeyboard'))


@app.route('/listapps')
def listapps():
    apps = roku.apps
    return render_template("listapps.html", apps = apps)

@app.route('/youtubekb')
def youtubekeyboard():
    # roku['YouTube'].launch()
    # time.sleep(15)
    for i in "STUFF":
        directions = yt.get_key_directions(session['LastKey'], i)
        yt.input_keys(roku, directions, i)

    # put the cursor in a known position on the keyboard
    # call the
    return render_template("youtubekb.html", lastkey = session['LastKey'])



if __name__ == '__main__':
    app.run()

