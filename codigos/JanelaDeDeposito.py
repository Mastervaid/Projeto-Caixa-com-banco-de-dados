from tkinter import Tk, Label, Entry, Button
from databaseCaixa import Caixa 


class JanelaDeDeposito:
    def __init__(self, usuario_logado):
        self.usuario_logado = usuario_logado
        self.valor_total = 0
        self.notas = []
        self.caixa = Caixa.get(Caixa.id == 1)

        self.janela_depositar = Tk()
        self.janela_depositar.title("Janela de depósito")
        self.janela_depositar.maxsize(550, 450)
        self.janela_depositar.minsize(550, 450)
        self.center_window(self.janela_depositar, 550, 450)

        self.label = Label(self.janela_depositar, text="Adicione as notas que você deseja depositar", font=('Minecraft', 9))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.label_entry = Label(self.janela_depositar, text="Valor adicionado: ", font=('Minecraft', 9))
        self.label_entry.place(x=280, y=50)
        self.entry_total = Entry(self.janela_depositar, width=9, font=('Minecraft', 9))
        self.entry_total.place(x=440, y=50)
        self.entry_total.insert('end', self.valor_total)

        self.botao_depositar = Button(self.janela_depositar, text='Depositar', font=('Minecraft', 9), command=self.depositar)
        self.botao_depositar.place(x=300, y=100)

        self.botao_voltar = Button(self.janela_depositar, text='<- Voltar', font=('Minecraft', 10), command=self.voltar)
        self.botao_voltar.place(x=300, y=380)

        self.listas_notas = {'nota200': 0, 'nota100': 0, 'nota50': 0, 'nota20': 0, 'nota10': 0, 'nota5': 0, 'nota2': 0, 'moeda1': 0}
        entradas = [200, 100, 50, 20, 10, 5, 2, 1]
        for i, valor in enumerate(entradas, start=1):
            self.botao_entrada(i, valor)

        self.janela_depositar.mainloop()

    def aumentar(self, entrada, valor):
        self.notas.append(str(valor))
        if valor in self.listas_notas:
            self.listas_notas[valor] += 1

        valor_total_atual = int(self.entry_total.get())
        novo_valor_atual = valor_total_atual + valor
        self.entry_total.delete(0, 'end')
        self.entry_total.insert('end', novo_valor_atual)

        valor_atual = int(entrada.get())
        novo_valor = valor_atual + 1
        entrada.delete(0, 'end')
        entrada.insert('end', novo_valor)

    def abaixar(self, entrada, valor):
        self.notas.remove(str(valor))
        if valor in self.listas_notas and self.listas_notas[valor] > 0:
            self.listas_notas[valor] -= 1

        valor_atual = int(entrada.get())
        novo_valor = valor_atual - 1
        if novo_valor >= 0:
            entrada.delete(0, 'end')
            entrada.insert('end', novo_valor)

        valor_total_atual = int(self.entry_total.get())
        novo_valor_atual = valor_total_atual - valor
        if novo_valor_atual >= 0:
            self.entry_total.delete(0, 'end')
            self.entry_total.insert('end', novo_valor_atual)

    def botao_entrada(self, y, valor):
        texto = f"+|{valor} R$|"
        botao_sacar = Button(self.janela_depositar, text=f"{texto:>{10}}", font=('Minecraft', 9),
                              command=lambda: self.aumentar(entrada, valor))
        botao_sacar.place(x=10, y=50*y)
        entrada = Entry(self.janela_depositar, width=10, font=('Minecraft', 9))
        entrada.place(x=110, y=5+50*y)
        entrada.insert('end', 0)

        botao_sacar = Button(self.janela_depositar, text='-', font=('Minecraft', 9),
                              command=lambda: self.abaixar(entrada, valor))
        botao_sacar.place(x=210, y=50*y)

    def depositar(self):
        caixa_atual = int(self.usuario_logado.valor)
        total = int(self.entry_total.get())
        novo_caixa = caixa_atual + total
        self.usuario_logado.valor = novo_caixa
        self.usuario_logado.save()

        for nota, quantidade in self.listas_notas.items():
            valor_atual = getattr(self.caixa, nota)
            setattr(self.caixa, nota, valor_atual + quantidade)
        
        self.caixa.save()
        self.janela_posdeposito()

    def janela_posdeposito(self):
        self.janela_depositar.destroy()
        self.janela_pos_deposito = Tk()
        self.janela_posdeposito.title("Depósito finalizado com sucesso")
        self.janela_posdeposito.maxsize(360, 200)
        self.janela_posdeposito.minsize(360, 200)
        self.center_window(self.janela_posdeposito, 360, 200)

        botao_ok = Button(self.janela_posdeposito, text='OK', font=('Minecraft', 9), command=self.ok)
        botao_ok.place(x=360/2, y=150)

        label = Label(self.janela_posdeposito, text=f'Você depositou o valor de: {self.entry_total.get()}', font=('Minecraft', 8))
        label.place(x=10, y=10)

        self.janela_posdeposito.mainloop()

    def ok(self):
        from JaneladoUsuario import JanelaDoUsuario 
        self.janela_posdeposito.destroy()
        JanelaDoUsuario(self.usuario_logado)

    def voltar(self):
        from JaneladoUsuario import JanelaDoUsuario 
        self.janela_depositar.destroy()
        JanelaDoUsuario(self.usuario_logado)

    @staticmethod
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)

        window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

# Para utilizar a classe, você pode instanciá-la assim:
# janela_deposito = JanelaDeDeposito(usuario_logado)
