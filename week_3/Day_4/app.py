from ast import literal_eval

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import requests


DB = SQLAlchemy()

class Record(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String, nullable=False)
    age = DB.Column(DB.SmallInteger, nullable=False)

    def __repr__(self):
        return f'[Id: {self.id} | Name: {self.name} | Predicted Age: {self.age}]'


def create_app():
    APP = Flask(__name__)
    APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agify_data.sqlite3'

    DB.init_app(APP)

    @APP.route('/')
    def base():
        if not Record.query.all():
            return 'There are no records!'
        else:
            return str(Record.query.all())

    @APP.route('/check_name')
    def check_name():
        BASE_URL = 'https://api.agify.io/?name='
        name = request.args['name']

        # /check_name?name=<some_name>
        data = literal_eval(requests.get(BASE_URL + name).text)

        if not Record.query.all():
            last_id = -1
        else:
            last_id = DB.session.query(DB.func.max(Record.id)).first()[0]

        try:
            rec =Record(id=last_id+1,name=name, age=data['age'])
            DB.session.add(rec)
            DB.session.commit()
            return f'Record added: {rec}'
        except Exception as e:
            return str(e)

    @APP.route('/no_older_than_40')
    def filter_age():
        filtered_records = Record.query.filter(Record.age <= 40).all()
        return str(filtered_records)


    @APP.route('/refresh')
    def refresh():
        DB.drop_all()
        DB.create_all()
        return 'Database Refreshed!'




    return APP

# Name is a variable that generates when you run a script
# Name becomes something else if it gets imported
# When you run something after you import,
#  it becomes something else
# If you want to do quick de-bugging you can create 
# class instances then test the functions locally by running the script
# Whenever you import a script whenever the import is 
# exicuted, anything that's associated to that is ran
if __name__ == '__main__':
    create_app.run()

