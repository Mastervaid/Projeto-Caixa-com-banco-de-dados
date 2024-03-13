from database import db, Usuario, Caixa
from tkinter import *
from peewee import DoesNotExist

usuario_logado = ''
caixa = ''
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

def sair(janela):
    janela.destroy()
    janela_inicial()
    usuario_logado = ''

def voltar(janela):
    janela.destroy()
    janela_do_usuario()

def janela_inicial():
    def ir_cadastro():
        janela.destroy()
        janela_de_cadastro()

    def logar():
        global usuario_logado
        try:
            usuario_logado = Usuario.get(Usuario.email == entry_email.get())
        except DoesNotExist:
            print("Erro", "Usuário não encontrado.")
        janela.destroy()
        janela_do_usuario()
    
    janela = Tk()
    janela.title("ThiThiBank")
    janela.maxsize(440,547)
    janela.minsize(440,547)
    center_window(janela, 440, 547)

    
    label_boasvindas =Label(janela,text="Bem vindo ao ThiThiBank",font=("Minecraft", 15))
    label_boasvindas.place(x=10,y=10)
    
    linha = Label(janela,text='__________________________________________________',font=('Minecraft',10))
    linha.place(x=-1,y=40)
    
    label_login = Label(janela,text="Faca seu login ou se cadastre:",font=("Minecraft", 10))
    label_login.place(x=10,y=120)

    label_email = Label(janela, text="Email:",font=("Minecraft", 10))
    label_email.place(x=10,y=172)
    entry_email = Entry(janela,width=15,font=("Minecraft",9))
    entry_email.place(x=90,y=175)

    label_senha = Label(janela, text="Senha:",font=("Minecraft", 10))
    label_senha.place(x=10,y=230)
    entry_senha = Entry(janela, show="*",width=15,font=("Minecraft",9))
    entry_senha.place(x=90,y=233)

    botao_login = Button(janela, text="Logar",command=logar,font=("Minecraft",9))
    botao_login.place(x=20, y=310)
    botao_cadast = Button(janela, text="Cadastrar",command=ir_cadastro,font=("Minecraft",9))
    botao_cadast.place(x=140, y=310)
        
    mainloop()

def janela_de_cadastro():
    def cadastrar_usuario():
        Usuario.create(nome=entry_nome.get(), email=entry_email.get(), senha=entry_senha.get(),valor="0")
    
    def ir_janela_inicial():
        janela.destroy()
        janela_inicial()
    
    janela = Tk()
    janela.title("janela de cadastro")
    janela.maxsize(440,547)
    janela.minsize(440,547)
    center_window(janela,440,547)

    label_txtc = Label(janela,text="Faca seu cadastro:",font=("Minecraft", 12))
    label_txtc.grid(row=0, column=0, padx=10, pady=10, sticky=W)    
    
    linha = Label(janela,text='__________________________________________________',font=('Minecraft',10))
    linha.place(x=-1,y=40)

    label_nome = Label(janela, text="Nome:",font=("Minecraft", 10))
    label_nome.place(x=20,y=100)
    entry_nome = Entry(janela,font=("Minecraft", 10))
    entry_nome.place(x=95,y=100)

    label_email = Label(janela, text="Email:",font=("Minecraft", 10))
    label_email.place(x=20,y=130)
    entry_email = Entry(janela,font=("Minecraft", 10))
    entry_email.place(x=95,y=130)

    label_senha = Label(janela, text="Senha:",font=("Minecraft", 10))
    label_senha.place(x=20,y=160)
    entry_senha = Entry(janela, show="*",font=("Minecraft", 10))
    entry_senha.place(x=95,y=160)

    botao_cadastrar = Button(janela, text="Cadastrar",command=cadastrar_usuario,font=("Minecraft", 10))
    botao_cadastrar.place(x=180, y=220)
    
    botao_login = Button(janela, text="Logar",command=ir_janela_inicial,font=("Minecraft", 10))
    botao_login.place(x=30, y=220)

    janela.mainloop()

def janela_do_usuario():
    def ir_janela_de_saque():
        janela.destroy()
        janela_saque()
    def ir_janela_de_deposito():
        janela.destroy()
        janela_deposito()

    global usuario_logado
    nome_usuario  = usuario_logado.nome
    email_usuario = usuario_logado.email
    saldo_usuario = usuario_logado.valor
    
    janela = Tk()
    janela.title("Janela do usuario")
    janela.maxsize(550,300)
    janela.minsize(550,300)
    center_window(janela,550,200)
    
    label_boasvindas = Label(janela,text=f"Bem vindo a Janela do usuario {nome_usuario}",font=("Minecraft", 15))
    label_boasvindas.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    label_sald = Label(janela,text=f"Seu saldo: {saldo_usuario}",font=("Minecraft", 10))
    label_sald.grid(row=1, column=0, padx=10, pady=10, sticky=W)

    label_boasvindas = Label(janela,text=f"Gosataria de fazer um saque ou um deposito?",font=("Minecraft", 10))
    label_boasvindas.grid(row=2, column=0, padx=10, pady=10, sticky=W)

    botao_sacar = Button(janela, text="Sacar",command=ir_janela_de_saque,font=("Minecraft", 10))
    botao_sacar.place(x=50, y=200)

    botao_depositar = Button(janela, text="Depositar",command=ir_janela_de_deposito,font=("Minecraft", 10))
    botao_depositar.place(x=150, y=200)

    botao_sair = Button(janela, text="Sair",command=lambda: sair(janela),font=("Minecraft", 10))
    botao_sair.place(x=300, y=200)
    
    mainloop()

def janela_deposito():
    valor_total = 0
    notas = []
    caixa = Caixa.get(Caixa.id == 1)
    def aumentar(entrada,valor):
        global valor_total
        notas.append(str(valor))
        print(notas)
        
        if valor == 200:
            listas_notas['nota200'] += 1
        if valor == 100:
            listas_notas['nota100'] += 1
        if valor == 50:
            listas_notas['nota50'] += 1
        if valor == 20:
            listas_notas['nota20'] += 1
        if valor == 10:
            listas_notas['nota10'] += 1
        if valor == 5:
            listas_notas['nota5'] += 1
        if valor == 2:
            listas_notas['nota2'] += 1
        if valor == 1:
            listas_notas['moeda1'] += 1

        valor_total_atual = int(entrytotal.get())
        novo_valor_atual = valor_total_atual + valor
        entrytotal.delete(0, END)
        entrytotal.insert(END, novo_valor_atual)
        
        valor_atual = int(entrada.get())  
        novo_valor = valor_atual + 1 
        entrada.delete(0, END) 
        entrada.insert(END, novo_valor)

    def abaixar(entrada,valor):
        global valor_total
        notas.remove(str(valor))
        print(notas)
        valor_atual = int(entrada.get())  
        novo_valor = valor_atual - 1 
        
        if valor == 200 and listas_notas['nota200'] > 0:
            listas_notas['nota200'] -= 1
        if valor == 100 and listas_notas['nota100'] > 0:
            listas_notas['nota100'] -= 1
        if valor == 50 and listas_notas['nota50'] > 0:
            listas_notas['nota50'] -= 1
        if valor == 20 and listas_notas['nota20'] > 0:
             listas_notas['nota20'] -= 1
        if valor == 10 and listas_notas['nota10'] > 0:
            listas_notas['nota10'] -= 1
        if valor == 5 and listas_notas['nota5'] > 0:
            listas_notas['nota5'] -= 1
        if valor == 2 and listas_notas['nota2'] > 0:
            listas_notas['nota2'] -= 1
        if valor == 1 and listas_notas['moeda1'] > 0:
            listas_notas['moeda1'] -= 1
        
        if novo_valor >= 0:
            entrada.delete(0, END) 
            entrada.insert(END, novo_valor)        
        
        valor_total_atual = int(entrytotal.get())
        if valor_atual > 0:
            novo_valor_atual = valor_total_atual - valor
        if novo_valor_atual >= 0:
            entrytotal.delete(0, END)
            entrytotal.insert(END, novo_valor_atual)
    
    
    def depositar():
        def janela_posdeposito():
            def ok():
                janela_depositar.destroy()
                janela_pos_deposito.destroy()
                janela_do_usuario()

            janela_pos_deposito = Tk()
            janela_pos_deposito.title("Deposito finalizado com sucesso")
            janela_pos_deposito.maxsize(360,200)
            janela_pos_deposito.minsize(360,200)
            center_window(janela_pos_deposito,360,200)

            botaook = Button(janela_pos_deposito,text='ok',font=('Minecraft',9),command=ok)
            botaook.place(x=360/2,y=150)

            label = Label(janela_pos_deposito,text=f'Voce depositou o valor de: {entrytotal.get()}',font=('Minecraft',8))
            label.place(x=10,y=10)



        caixa_atual = int(usuario_logado.valor)
        total = int(entrytotal.get())
        novo_caixa = caixa_atual + total
        usuario_logado.valor = novo_caixa
        usuario_logado.save()

        v1 = int(caixa.nota200)
        nv1 = v1 + listas_notas["nota200"]
        caixa.nota200 = nv1
        
        v2 = int(caixa.nota100)
        nv2 = v2 + listas_notas['nota100']
        caixa.nota100 = nv2

        v2 = int(caixa.nota50)
        nv2 = v2 + listas_notas['nota50']
        caixa.nota50 = nv2
        
        v2 = int(caixa.nota20)
        nv2 = v2 + listas_notas['nota20']
        caixa.nota20 = nv2
        
        v2 = int(caixa.nota10)
        nv2 = v2 + listas_notas['nota10']
        caixa.nota10 = nv2
        
        v2 = int(caixa.nota5)
        nv2 = v2 + listas_notas['nota5']
        caixa.nota5 = nv2
        
        v2 = int(caixa.nota2)
        nv2 = v2 + listas_notas['nota2']
        caixa.nota2 = nv2
        
        v2 = int(caixa.moeda1)
        nv2 = v2 + listas_notas['moeda1']
        caixa.moeda1 = nv2
        caixa.save()
        janela_posdeposito()

    def botao_cmentrada(y,valor,entrada):
        global entradas
        texto = f"+|{valor} R$|"
        botao_sacar = Button(janela_depositar, text=f"{texto:>{10}}",font=('Minecraft',9), command=lambda: aumentar(entrada,valor))
        botao_sacar.place(x=10, y=50*y)
        entrada = Entry(janela_depositar, width=10,font=('Minecraft',9))
        entrada.place(x=110, y=5+50*y)
        entrada.insert(END, 0)
        
        botao_sacar = Button(janela_depositar, text='-',font=('Minecraft',9), command=lambda: abaixar(entrada,valor))
        botao_sacar.place(x=210, y=50*y)  
    
    
    janela_depositar = Tk()
    janela_depositar.title("Janela de deposito")
    janela_depositar.maxsize(550,450)
    janela_depositar.minsize(550,450)
    center_window(janela_depositar,550,450)
    
    label =Label(janela_depositar,text=f"Adicione as notas que voce deseja depositar",font=('Minecraft',9))
    label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    labelentry = Label(janela_depositar, text="Valor adicionado: ",font=('Minecraft',9))
    labelentry.place(x=280,y=50)
    entrytotal = Entry(janela_depositar,width=9,font=('Minecraft',9))
    entrytotal.place(x=440,y=50)
    entrytotal.insert(END, valor_total)

    #Boitões e entradas   
    botao_depositar = Button(janela_depositar,text='Depositar',font=('Minecraft',9),command=depositar)
    botao_depositar.place(x=300,y=100)

    botao_voltar = Button(janela_depositar,text='<-Voltar',font=('Minecraft',10), command=lambda:voltar(janela_depositar))
    botao_voltar.place(x=300,y=380)
    
    listas_notas = {}
    listas_notas['nota200'] = 0
    listas_notas['nota100'] = 0
    listas_notas['nota50']  = 0
    listas_notas['nota20']  = 0
    listas_notas['nota10']  = 0
    listas_notas['nota5']  = 0
    listas_notas['nota2']   = 0
    listas_notas['moeda1']  = 0

    entrada200 = 200
    botao_cmentrada(1,200,entrada200)
    entrada100 = 100
    botao_cmentrada(2,100,entrada100)
    entrada50 = 50
    botao_cmentrada(3,50,entrada50)
    entrada20 = 20
    botao_cmentrada(4,20,entrada20)
    entrada10 = 10
    botao_cmentrada(5,10,entrada10)
    entrada5 = 5
    botao_cmentrada(6,5,entrada5)
    entrada2 = 2
    botao_cmentrada(7,2,entrada2)
    entrada1 = 1
    botao_cmentrada(8,1,entrada1)

def janela_saque():
    caixa = Caixa.get(Caixa.id == 1)
    
    def janelapossaque(valor_sacado):
        def ok():
            janela_saque.destroy()
            janela_pos_saque.destroy()
            janela_do_usuario()

        janela_pos_saque = Tk()
        janela_pos_saque.title("Saque finalizado com sucesso")
        janela_pos_saque.maxsize(360,200)
        janela_pos_saque.minsize(360,200)
        center_window(janela_pos_saque,360,200)

        botaook = Button(janela_pos_saque,text='ok',font=('Minecraft',9),command=ok)
        botaook.place(x=360/2,y=150)

        label = Label(janela_pos_saque,text=f'Voce sacou o valor de: {valor_sacado}',font=('Minecraft',8))
        label.place(x=10,y=10)
    
    def labalandentry(valor,y,entrada,notaquant):
        global entradas
        label = Label(janela_saque, text=f"|{valor} R$|",font=('Minecraft'))
        label.place(x=10, y=60+40*y)
        entrada = Entry(janela_saque, width=10,font=('Minecraft'))
        entrada.place(x=120, y=60+40*y)
        entrada.insert(END, notaquant)
    
    def janela_salodo_insuficiente():
        def ok():
            janela_saque.destroy()
            janela_pos_saque.destroy()
            janela_do_usuario()

        janela_pos_saque = Tk()
        janela_pos_saque.title("Saque não concedido")
        janela_pos_saque.maxsize(360,200)
        janela_pos_saque.minsize(360,200)
        center_window(janela_pos_saque,360,200)

        botaook = Button(janela_pos_saque,text='ok',font=('Minecraft',10),command=ok)
        botaook.place(x=360/2-10,y=150)

        label = Label(janela_pos_saque,text=f'Saldo insuficiente',font=('Minecraft',12))
        label.place(x=10,y=10)
        

    def sacar():
        valor_desejado = int(entada_valor_sacar.get())
        valor_sacado = 0
        if valor_desejado <= int(usuario_logado.valor):
            while True:
                if valor_desejado >= 200 and listas_notas['nota200'] > 0:
                    valor_desejado -= 200
                    valor_sacado += 200
                    listas_notas['nota200'] -= 1
                    nova_listas_notas['nota200'] += 1
                    continue
                elif valor_desejado >= 100 and listas_notas['nota100'] > 0:
                    valor_desejado -= 100
                    valor_sacado += 100
                    listas_notas['nota100'] -= 1
                    nova_listas_notas['nota100'] += 1
                    continue
                elif valor_desejado >= 50 and listas_notas['nota50'] > 0:
                    valor_desejado -= 50
                    valor_sacado += 50
                    listas_notas['nota50'] -= 1
                    nova_listas_notas['nota50'] += 1
                    continue
                elif valor_desejado >= 20 and listas_notas['nota20'] > 0:
                    valor_desejado -= 20
                    valor_sacado += 20
                    listas_notas['nota20'] -= 1
                    nova_listas_notas['nota20'] += 1
                    continue
                elif valor_desejado >= 10 and listas_notas['nota10'] > 0:
                    valor_desejado -= 10
                    valor_sacado += 10
                    listas_notas['nota10'] -= 1
                    nova_listas_notas['nota10'] += 1
                    continue
                elif valor_desejado >= 5 and listas_notas['nota5'] > 0:
                    valor_desejado -= 5
                    valor_sacado += 5
                    listas_notas['nota5'] -= 1
                    nova_listas_notas['nota5'] += 1
                    continue
                elif valor_desejado >= 2 and listas_notas['nota2'] > 0:
                    valor_desejado -= 2
                    valor_sacado += 2
                    listas_notas['nota2'] -= 1
                    nova_listas_notas['nota2'] += 1
                    continue
                elif valor_desejado >= 1 and listas_notas['moeda1'] > 0:
                    valor_desejado -= 1
                    valor_sacado += 1
                    listas_notas['moeda1'] -= 1
                    nova_listas_notas['moeda1'] += 1
                    continue
                else:
                    break    
            
            saldo_velho = int(usuario_logado.valor)
            novo_saldo = saldo_velho - valor_sacado
            usuario_logado.valor = novo_saldo
            
            caixa.nota200 = listas_notas['nota200']
            caixa.nota100 = listas_notas['nota100']
            caixa.nota50  = listas_notas['nota50']
            caixa.nota20  = listas_notas['nota20']
            caixa.nota10  = listas_notas['nota10']
            caixa.nota5   = listas_notas['nota5']
            caixa.nota2   = listas_notas['nota2']
            caixa.moeda1  = listas_notas['moeda1']
            caixa.save()
            
            for chave in listas_notas:
                listas_notas[chave] = nova_listas_notas[chave]
            
            print(listas_notas)
            print(f'Valor sacado: {valor_sacado}')

            janelapossaque(valor_sacado)
        else:
            janela_salodo_insuficiente()
        
    janela_saque = Tk()
    janela_saque.title("Janela de saque")
    janela_saque.maxsize(560,547)
    janela_saque.minsize(560,547)
    center_window(janela_saque,560,547)

    saldo_usuario = int(usuario_logado.valor)
    nome_usuario = str(usuario_logado.nome)
    
    label_nome_Usuario = Label(janela_saque,text=f'Usuario: {nome_usuario}',font=('Minecraft')) 
    label_nome_Usuario.place(x=10,y=1)

    label_Saldo_Usuario = Label(janela_saque,text=f'Saldo: {saldo_usuario}',font=('Minecraft')) 
    label_Saldo_Usuario.place(x=10,y=30)

    label_diponiveis = Label(janela_saque,text='Notas disponiveis:',font=('Minecraft',10))
    label_diponiveis.place(x=10,y=70)
    
    label_valor_sacar = Label(janela_saque,text='Sacar:',font=('Minecraft'))
    label_valor_sacar.place(x=300,y=100)
    entada_valor_sacar = Entry(janela_saque,width=10,font=('Minecraft'))
    entada_valor_sacar.place(x=385,y=100)
     
    botao_sacar = Button(janela_saque,text='Sacar',font=('Minecraft',10), command=sacar)
    botao_sacar.place(x=300,y=140)

    botao_voltar = Button(janela_saque,text='<-Voltar',font=('Minecraft',10), command=lambda:voltar(janela_saque))
    botao_voltar.place(x=300,y=380)

    listas_notas = {}
    listas_notas['nota200'] =  int(caixa.nota200)
    listas_notas['nota100'] =  int(caixa.nota100)
    listas_notas['nota50']  =  int(caixa.nota50)
    listas_notas['nota20']  =  int(caixa.nota20)
    listas_notas['nota10']  =  int(caixa.nota10)
    listas_notas['nota5']   =  int(caixa.nota5)
    listas_notas['nota2']   =  int(caixa.nota2)
    listas_notas['moeda1']  =  int(caixa.moeda1)

    nova_listas_notas = {}
    nova_listas_notas['nota200'] = 0
    nova_listas_notas['nota100'] = 0 
    nova_listas_notas['nota50']  = 0 
    nova_listas_notas['nota20']  = 0 
    nova_listas_notas['nota10']  = 0 
    nova_listas_notas['nota5']   = 0 
    nova_listas_notas['nota2']   = 0 
    nova_listas_notas['moeda1']  = 0
   
    entrada200 = 0
    labalandentry(200,1,entrada200,listas_notas['nota200'])
    entrada100 = 0
    labalandentry(100,2,entrada100,listas_notas['nota100'])
    entrada50 = 0
    labalandentry(50,3,entrada50,listas_notas['nota50'])
    entrada20 = 0
    labalandentry(20,4,entrada20,listas_notas['nota20'])
    entrada10 = 0
    labalandentry(10,5,entrada10,listas_notas['nota10'])
    entrada5 = 0
    labalandentry(5,6,entrada5,listas_notas['nota5'])
    entrada2 = 0
    labalandentry(2,7,entrada2,listas_notas['nota2'])
    entrada1 = 0
    labalandentry(1,8,entrada1,listas_notas['moeda1'])
