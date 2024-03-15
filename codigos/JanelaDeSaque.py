from tkinter import Tk, Label, Entry, Button
from databaseCaixa import Caixa  

class JanelaDeSaque:
    def __init__(self, usuario_logado):
        self.caixa = Caixa.get(Caixa.id == 1)
        self.usuario_logado = usuario_logado
        self.janela_saque = Tk()
        self.janela_saque.title("Janela de saque")
        self.janela_saque.maxsize(560, 547)
        self.janela_saque.minsize(560, 547)
        self.center_window(self.janela_saque, 560, 547)

        saldo_usuario = int(usuario_logado.valor)
        nome_usuario = str(usuario_logado.nome)

        self.label_nome_usuario = Label(self.janela_saque, text=f'Usuário: {nome_usuario}', font=('Minecraft'))
        self.label_nome_usuario.place(x=10, y=1)

        self.label_saldo_usuario = Label(self.janela_saque, text=f'Saldo: {saldo_usuario}', font=('Minecraft'))
        self.label_saldo_usuario.place(x=10, y=30)

        self.label_disponiveis = Label(self.janela_saque, text='Notas disponíveis:', font=('Minecraft', 10))
        self.label_disponiveis.place(x=10, y=70)

        self.label_valor_sacar = Label(self.janela_saque, text='Sacar:', font=('Minecraft'))
        self.label_valor_sacar.place(x=300, y=100)
        self.entada_valor_sacar = Entry(self.janela_saque, width=10, font=('Minecraft'))
        self.entada_valor_sacar.place(x=385, y=100)

        self.botao_sacar = Button(self.janela_saque, text='Sacar', font=('Minecraft', 10), command=self.sacar)
        self.botao_sacar.place(x=300, y=140)

        self.botao_voltar = Button(self.janela_saque, text='<- Voltar', font=('Minecraft', 10), command=self.voltar)
        self.botao_voltar.place(x=300, y=380)

        self.listas_notas = {
            'nota200': int(self.caixa.nota200), 'nota100': int(self.caixa.nota100),
            'nota50': int(self.caixa.nota50), 'nota20': int(self.caixa.nota20),
            'nota10': int(self.caixa.nota10), 'nota5': int(self.caixa.nota5),
            'nota2': int(self.caixa.nota2), 'moeda1': int(self.caixa.moeda1)
        }

        self.nova_listas_notas = {
            'nota200': 0, 'nota100': 0, 'nota50': 0, 'nota20': 0,
            'nota10': 0, 'nota5': 0, 'nota2': 0, 'moeda1': 0
        }

        self.labalandentry(200, 1, self.listas_notas['nota200'])
        self.labalandentry(100, 2, self.listas_notas['nota100'])
        self.labalandentry(50, 3, self.listas_notas['nota50'])
        self.labalandentry(20, 4, self.listas_notas['nota20'])
        self.labalandentry(10, 5, self.listas_notas['nota10'])
        self.labalandentry(5, 6, self.listas_notas['nota5'])
        self.labalandentry(2, 7, self.listas_notas['nota2'])
        self.labalandentry(1, 8, self.listas_notas['moeda1'])

        self.janela_saque.mainloop()

    def janelapossaque(self, valor_sacado):
        self.janela_pos_saque = Tk()
        self.janela_pos_saque.title("Saque finalizado com sucesso")
        self.janela_pos_saque.maxsize(360, 200)
        self.janela_pos_saque.minsize(360, 200)
        self.center_window(self.janela_pos_saque, 360, 200)

        self.botao_ok = Button(self.janela_pos_saque, text='OK', font=('Minecraft', 9), command=self.ok)
        self.botao_ok.place(x=360 / 2, y=150)

        self.label = Label(self.janela_pos_saque, text=f'Você sacou o valor de: {valor_sacado}', font=('Minecraft', 8))
        self.label.place(x=10, y=10)

    def labalandentry(self, valor, y, notaquant):
        label = Label(self.janela_saque, text=f"|{valor} R$|", font=('Minecraft'))
        label.place(x=10, y=60 + 40 * y)
        entrada = Entry(self.janela_saque, width=10, font=('Minecraft'))
        entrada.place(x=120, y=60 + 40 * y)
        entrada.insert('end', notaquant)

    def janela_salodo_insuficiente(self):
        self.janela_pos_saque = Tk()
        self.janela_pos_saque.title("Saque não concedido")
        self.janela_pos_saque.maxsize(360, 200)
        self.janela_pos_saque.minsize(360, 200)
        self.center_window(self.janela_pos_saque, 360, 200)

        self.botao_ok = Button(self.janela_pos_saque, text='OK', font=('Minecraft', 10), command=self.ok)
        self.botao_ok.place(x=360 / 2 - 10, y=150)

        self.label = Label(self.janela_pos_saque, text=f'Saldo insuficiente', font=('Minecraft', 12))
        self.label.place(x=10, y=10)

    def sacar(self):
        from JaneladoUsuario import JanelaDoUsuario
        valor_desejado = int(self.entada_valor_sacar.get())
        valor_sacado = 0
        if valor_desejado <= int(self.usuario_logado.valor):
            while True:
                if valor_desejado >= 200 and self.listas_notas['nota200'] > 0:
                    valor_desejado -= 200
                    valor_sacado += 200
