from flask import Flask,render_template
import flask

app = flask.Flask(__name__)

@app.route("/")
def main():
  #calling index.html from templates folder using render_templates
  return flask.render_template("/index.html")

if __name__ == "__main__":
    app.run(debug=True)