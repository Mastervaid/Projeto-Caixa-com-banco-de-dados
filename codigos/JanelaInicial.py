from tkinter import Tk, Label, Entry, Button
from peewee import DoesNotExist
from databaseUsuario import Usuario 

class JanelaInicial:
    def __init__(self,janela):
        self.janela = janela
        self.janela.title("ThiThiBank")
        self.janela.maxsize(440, 547)
        self.janela.minsize(440, 547)
        self.center_window(self.janela, 440, 547)

        self.label_boasvindas = Label(janela, text="Bem vindo ao ThiThiBank", font=("Minecraft", 15))
        self.label_boasvindas.place(x=10, y=10)

        self.linha = Label(janela, text='__________________________________________________', font=('Minecraft', 10))
        self.linha.place(x=-1, y=40)

        self.label_login = Label(janela, text="Faça seu login ou se cadastre:", font=("Minecraft", 10))
        self.label_login.place(x=10, y=120)

        self.label_email = Label(janela, text="Email:", font=("Minecraft", 10))
        self.label_email.place(x=10, y=172)
        self.entry_email = Entry(janela, width=15, font=("Minecraft", 9))
        self.entry_email.place(x=90, y=175)

        self.label_senha = Label(janela, text="Senha:", font=("Minecraft", 10))
        self.label_senha.place(x=10, y=230)
        self.entry_senha = Entry(janela, show="*", width=15, font=("Minecraft", 9))
        self.entry_senha.place(x=90, y=233)

        self.botao_login = Button(janela, text="Logar", command=self.logar, font=("Minecraft", 9))
        self.botao_login.place(x=20, y=310)
        self.botao_cadast = Button(janela, text="Cadastrar", command=self.ir_cadastro, font=("Minecraft", 9))
        self.botao_cadast.place(x=140, y=310)


    def show(self):
        self.janela.mainloop()
    
    def ir_cadastro(self):
        from JanelaDeCadastro import JanelaDeCadastro
        self.janela.destroy()
        if __name__ == "__main__":
            Janela_de_Cadastro = Tk() 
            Janela_De_Cadastro = JanelaDeCadastro(Janela_de_Cadastro)
            Janela_De_Cadastro.show()

    def logar(self):
        from JaneladoUsuario import JanelaDoUsuario 
        global usuario_logado
        try:
            usuario_logado = Usuario.get(Usuario.email == self.entry_email.get())
        except DoesNotExist:
            print("Erro", "Usuário não encontrado.")
        self.janela.destroy()
        if __name__ == "__main__":
            janela_usuario = Tk()
            Janela_Do_Usuario = JanelaDoUsuario(janela_usuario)
            Janela_Do_Usuario.show()

    @staticmethod
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)

        window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))



