from datetime import date
from sqlite3 import Date
from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from playhouse.postgres_ext import ArrayField

db = PostgresqlDatabase('biohazard', user='leontzuchiangchan',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Titles(BaseModel):
    name = CharField()
    main_characters = ArrayField(CharField)
    virus = CharField()
    date = IntegerField()
    location = CharField()


db.connect()
db.drop_tables([Titles])
db.create_tables([Titles])

Titles(name='Resident Evil 0', main_characters=['Rebecca', 'Billy'],
       virus='Leech', date=1998, location='Arklay Mountain').save()
Titles(name='Resident Evil', main_characters=['Chris', 'Jill'],
       virus='T-Virus', date=1998, location='Spencer Mansion').save()
Titles(name='Resident Evil 2', main_characters=['Leon', 'Claire'],
       virus='G-Virus', date=1998, location='Raccoon City').save()
Titles(name='Resident Evil 3', main_characters=['Jill', 'Carlos'],
       virus='T-Virus', date=1998, location='Raccoon City').save()
Titles(name='Resident Evil Code Veronica', main_characters=['Claire', 'Chris'],
       virus='t-Veronica Virus', date=1998, location='Antarctica').save()
Titles(name='Resident Evil 4', main_characters=['Leon', 'Ada'],
       virus='Las Plagas', date=2004, location='Spain').save()
Titles(name='Resident Evil Revelations', main_characters=['Jill', 'Chris'],
       virus='t-Abyss Virus', date=2005, location='Queen Zenobia').save()
Titles(name='Resident Evil 5', main_characters=['Chris', 'Sheva'],
       virus='Uroboros', date=2009, location='Kijuju').save()
Titles(name='Resident Evil Revelations 2', main_characters=['Claire', 'Barry'],
       virus='t-Phobos Virus', date=2011, location='Sein Island').save()
Titles(name='Resident Evil 6', main_characters=['Leon', 'Chris', 'Jake', 'Ada'],
       virus='C-Virus', date=2013, location='Lanshang').save()
Titles(name='Resident Evil 7', main_characters='Ethan',
       virus='Mold', date=2017, location='Dulvey').save()
Titles(name='Resident Evil Village', main_characters=['Ethan', 'Chris'],
       virus='Mold', date=2021, location='Europe').save()

app = Flask(__name__)


@ app.route('/games/', methods=['GET', 'POST'])
@ app.route('/games/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Titles.get(Titles.id == id)))
        else:
            titleList = []
            for name in Titles.select():
                titleList.append(model_to_dict(name))
            return jsonify(titleList)

    if request.method == 'PUT':
        body = request.get_json()
        game = Titles.update(body).where(Titles.id == id)
        game.execute()
        return jsonify({"updated": True})

    if request.method == 'POST':
        new_name = dict_to_model(Titles, request.get_json())
        new_name.save()
        return jsonify({"success": True})

    if request.method == 'DELETE':
        deleted = Titles.delete().where(Titles.id == id)
        deleted.execute()
        return jsonify({"deleted": True})


app.run(debug=True)
