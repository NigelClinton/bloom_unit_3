from flask import Flask
from flask import render_template
from flask import request
from .models import db, User, Tweet
import os

app_dir = os.path.dirname(os.path.abspath(__file__))
database = "sqlite:///{}".format(os.path.join(app_dir, "twitoff.sqlite3"))


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/users", methods=['GET', 'POST'])
    def users_page():
        # request.form checks if someone just submitted the form.
        name = request.form.get('name')

        if name:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()

        users = User.query.all()
        return render_template("users.html", users=users)

    @app.route("/tweet", methods=['GET', 'POST'])
    def tweet_page():
        # request.form checks if someone just submitted the form.
        tweet = request.form.get('tweet')

        if tweet:
            user = Tweet(tweet=tweet)
            db.session.add(user)
            db.session.commit()

        tweets = Tweet.query.all()
        return render_template("tweet.html", users=tweets)

    @app.route("/about")
    def about():
        return "This is the best application ever!"

    return app
