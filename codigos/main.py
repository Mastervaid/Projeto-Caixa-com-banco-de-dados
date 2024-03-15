from databaseUsuario import db, Usuario
from databaseCaixa import dbv, Caixa
from JanelaInicial import JanelaInicial
from tkinter import Tk

db.connect()
db.create_tables([Usuario])
dbv.connect()
dbv.create_tables([Caixa])

if __name__ == "__main__":
    janela_principal = Tk()
    janela_inicial = JanelaInicial(janela_principal)
    janela_inicial.show()

