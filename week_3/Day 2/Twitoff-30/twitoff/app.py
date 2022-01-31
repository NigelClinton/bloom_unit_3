from decouple import config
from flask import Flask, render_template, request
from .models import db, User, Tweet
from .twitter import get_user_and_tweets
from .predict import predict_user
import os

app_dir = os.path.dirname(os.path.abspath(__file__))
database = config("DATABASE_URI")


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route("/")
    def home():
        return render_template("home_final.html")

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
        return render_template("test_table.html")

    @app.route('/compare', methods=["POST"])
    def compare():
        user0, user1 = sorted(
            [request.values['user0'], request.values["user1"]])

        if user0 == user1:
            message = "Cannot compare users to themselves!"

        else:
            # prediction returns a 0 or 1
            prediction = predict_user(
                user0, user1, request.values["tweet_text"])
            message = "'{}' is more likely to be said by {} than {}!".format(
                request.values["tweet_text"],
                user1 if prediction else user0,
                user0 if prediction else user1
            )

        return render_template('prediction.html', title="Prediction", message=message)

    return app

if __name__ == '__main__':
    create_app().run()
