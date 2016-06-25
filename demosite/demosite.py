import os
import sys
from flask import Flask, render_template, redirect, request

this_dir = os.path.dirname(os.path.realpath(__file__))
config = os.path.join(this_dir, 'demosite.cfg')

oxd_path = os.path.dirname(this_dir)
if oxd_path not in sys.path:
    sys.path.insert(0, oxd_path)

import oxdpython

app = Flask(__name__)
oxc = oxdpython.Client(config)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/authorize/')
def authorize():
    """The endpoint which is to be accessed but the user in order to start the
    authorization by the user"""

    auth_url = oxc.get_authorization_url()
    return redirect(auth_url)


@app.route('/callback')
def callabck():
    # parse the state, code and scopes from the callback url
    state = request.args.get('state')
    code = request.args.get('code')
    scopes = request.args.get('scope').split(" ")

    # pass that information to obtain the access_token
    tokens = oxc.get_tokens_by_code(code, scopes, state)

    # usingthe access token obtain user info
    user = oxc.get_user_info(tokens.access_token)

    return render_template("home.html", user=user)


@app.route('/logout')
def logout():
    logout_url = oxc.get_logout_uri()
    return redirect(logout_url)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
