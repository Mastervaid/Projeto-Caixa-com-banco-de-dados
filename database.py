from peewee import *

db = SqliteDatabase('freelancers.db')

class Usuario(Model):
    nome  = CharField()
    email = CharField(unique=True)
    senha = CharField()
    valor = CharField()

    class Meta():
        database = db

dbv = SqliteDatabase('caixa.db')

class Caixa(Model):
    nota200 = CharField()
    nota100 = CharField()
    nota50  = CharField()
    nota20  = CharField()
    nota10  = CharField()
    nota5   = CharField()
    nota2   = CharField()
    moeda1  = CharField()
    class Meta():
        database = dbv