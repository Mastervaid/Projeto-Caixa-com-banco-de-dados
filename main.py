from database import db,Usuario,dbv,Caixa
from funções import *

db.connect()
db.create_tables([Usuario])
dbv.connect()
dbv.create_tables([Caixa])
janela_inicial()

