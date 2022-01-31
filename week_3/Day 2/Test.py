from decouple import config
from flask import Flask, render_template, request
from .models import db, User, Tweet
from .twitter import get_user_and_tweets
import os


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv()
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

    @app.route('/add_user')
    def add_user():
        user = request.args['username']
        try:
            response = get_user_and_tweets(user)
            if not response:
                return 'Nothing was added.'
            else:
                return f'User: {user} successfully added!'
        except Exception as e:
            return str(e)

    @app.route('/refresh')
    def refresh():
        db.drop_all()
        db.create_all()
        return 'Database Refreshed!'

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

if __name__ == '__main__':
    create_app().run()
