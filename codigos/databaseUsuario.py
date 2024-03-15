from peewee import *

db = SqliteDatabase('freelancers.db')

class Usuario(Model):
    nome  = CharField()
    email = CharField(unique=True)
    senha = CharField()
    valor = CharField()

    class Meta():
        database = db

