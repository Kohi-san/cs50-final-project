import flask

app = flask.Flask(__name__)

@app.route("/home")
def index():
    return flask.render_template('index.html')