from tkinter import Tk, Label, Button
from JanelaDeSaque import JanelaDeSaque 
from JanelaDeDeposito import JanelaDeDeposito  

class JanelaDoUsuario:
    def __init__(self, usuario_logado,janela):
        self.usuario_logado = usuario_logado
        self.nome_usuario = self.usuario_logado.nome
        self.saldo_usuario = self.usuario_logado.valor

        self.janela = janela
        self.janela.title("Janela do usuário")
        self.janela.maxsize(550, 300)
        self.janela.minsize(550, 300)
        self.center_window(self.janela, 550, 200)

        self.label_boasvindas = Label(janela, text=f"Bem vindo à Janela do usuário {self.nome_usuario}", font=("Minecraft", 15))
        self.label_boasvindas.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.label_saldo = Label(janela, text=f"Seu saldo: {self.saldo_usuario}", font=("Minecraft", 10))
        self.label_saldo.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.label_operacao = Label(janela, text="Gostaria de fazer um saque ou um depósito?", font=("Minecraft", 10))
        self.label_operacao.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.botao_sacar = Button(janela, text="Sacar", command=self.ir_janela_de_saque, font=("Minecraft", 10))
        self.botao_sacar.place(x=50, y=200)

        self.botao_depositar = Button(janela, text="Depositar", command=self.ir_janela_de_deposito, font=("Minecraft", 10))
        self.botao_depositar.place(x=150, y=200)

        self.botao_sair = Button(janela, text="Sair", command=self.sair, font=("Minecraft", 10))
        self.botao_sair.place(x=300, y=200)

        self.janela.mainloop()
    
    def show(self):
        self.janela.mainloop()
    
    def ir_janela_de_saque(self):
        self.janela.destroy()
        janela_de_saque = Tk()
        janela_De_saque = JanelaDeSaque(janela_de_saque,self.usuario_logado)
        janela_De_saque.show()

    def ir_janela_de_deposito(self):
        self.janela.destroy()
        JanelaDeDeposito(self.usuario_logado)

    def sair(self):
        self.janela.destroy()
        from JanelaInicial import JanelaInicial
        janela_inicial = Tk()
        janela_Inicial = JanelaInicial(janela_inicial)
        janela_Inicial.show()

    @staticmethod
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)

        window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

# Para utilizar a classe, você pode instanciá-la assim:
# janela_do_usuario = JanelaDoUsuario(usuario_logado)
