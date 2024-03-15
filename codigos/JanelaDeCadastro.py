from tkinter import Tk, Label, Entry, Button
from databaseUsuario import Usuario 

class JanelaDeCadastro:
    def __init__(self,janela):
        self.janela = janela
        self.janela.title("Janela de Cadastro")
        self.janela.maxsize(440, 547)
        self.janela.minsize(440, 547)
        self.center_window(self.janela, 440, 547)

        self.label_txtc = Label(janela, text="Faça seu cadastro:", font=("Minecraft", 12))
        self.label_txtc.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.linha = Label(janela, text='__________________________________________________', font=('Minecraft', 10))
        self.linha.place(x=-1, y=40)

        self.label_nome = Label(janela, text="Nome:", font=("Minecraft", 10))
        self.label_nome.place(x=20, y=100)
        self.entry_nome = Entry(janela, font=("Minecraft", 10))
        self.entry_nome.place(x=95, y=100)

        self.label_email = Label(janela, text="Email:", font=("Minecraft", 10))
        self.label_email.place(x=20, y=130)
        self.entry_email = Entry(janela, font=("Minecraft", 10))
        self.entry_email.place(x=95, y=130)

        self.label_senha = Label(janela, text="Senha:", font=("Minecraft", 10))
        self.label_senha.place(x=20, y=160)
        self.entry_senha = Entry(janela, show="*", font=("Minecraft", 10))
        self.entry_senha.place(x=95, y=160)

        self.botao_cadastrar = Button(janela, text="Cadastrar", command=self.cadastrar_usuario, font=("Minecraft", 10))
        self.botao_cadastrar.place(x=180, y=220)

        self.botao_login = Button(janela, text="Logar", command=self.ir_janela_inicial, font=("Minecraft", 10))
        self.botao_login.place(x=30, y=220)

    def show(self):
        self.janela.mainloop()

    def cadastrar_usuario(self):
        Usuario.create(nome=self.entry_nome.get(), email=self.entry_email.get(), senha=self.entry_senha.get(), valor="0")

    def ir_janela_inicial(self):
        self.janela.destroy()

    @staticmethod
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)

        window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

# Para utilizar a classe, você pode instanciá-la assim:
# janela_cadastro = JanelaDeCadastro()
