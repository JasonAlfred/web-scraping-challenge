from flask import current_app as app
from flask import render_template, url_for
from flask import Flask

#Setup Flask Local Server
app = Flask(__name__)



@app.route('/')
def home():
    """Landing page."""
    return render_template('home.html',
                           title="Genealogy App",
                           description="Researching Family History")


if __name__ == "__main__":
    app.run(debug=True)