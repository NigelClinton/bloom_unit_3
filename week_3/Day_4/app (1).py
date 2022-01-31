import os
from flask import Flask, render_template, request, redirect
from .models import db, User, Tweet

def create_app():
    app_dir = os.path.dirname(os.path.abspath(__file__))
    database = "sqlite:///{}".format(os.path.join(app_dir, "twitoff.sqlite3"))

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route("/", methods=["GET", "POST"])
    def home():
        name = request.form.get("name")
        text = request.form.get("text")
        userid = request.form.get("userid")

        if name:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()

        if (text and userid):
            tweet = Tweet(text=text, user_id=userid)
            db.session.add(tweet)
            db.session.commit()

        users = User.query.all()
        tweets = Tweet.query.all()
        return render_template("home.html", users=users, tweets=tweets)

    @app.route("/delete", methods=["POST"])
    def delete():
        name = request.form.get("name")
        text = request.form.get("text")

        if name:
            user = User.query.filter_by(name=name).first()
            db.session.delete(user)
            db.session.commit()

        if text:
            tweet = Tweet.query.filter_by(text=text).first()
            db.session.delete(tweet)
            db.session.commit()

        return redirect("/")

    return app