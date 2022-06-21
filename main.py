# ========================= #
# Autor: Ihury Ferreira     #
# ========================= #
import time
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import END, messagebox as ms
from seguidor_cod import InstaCrud
from seguidor_inst import InstagramBot
from selenium.webdriver.common.by import By

class LoginPrinc:
    def __init__(self, win):
        self.crud = InstaCrud()
        self.master = win
        self.minhafont = font.Font(family="Bernard MT Condensed",size=16,weight="bold")
        self.minhafont2 = font.Font(family="Arial Black",size=16,weight="bold")
        
        self.loginTxt = tk.Label(win, text='Login:', bg='white', font=self.minhafont)
        self.loginTxt.place(x=0,y=5)

        self.login = tk.Entry(win,bd=2, bg='yellow',width=16,highlightthickness=2, font=self.minhafont2)
        self.login.place(x=67,y=5)

        self.senhaTxt = tk.Label(win,text='Senha:', bg='white', font=self.minhafont)
        self.senhaTxt.place(x=0,y=55)

        self.senha = tk.Entry(win,bd=2,width=16, bg='yellow',highlightthickness=2, font=self.minhafont2, show='*')
        self.senha.place(x=67,y=55)

        self.login.config(highlightbackground = "black", highlightcolor= "#46daeb")
        self.senha.config(highlightbackground = "black", highlightcolor= "#46daeb")

        self.btn = tk.Button(win, text='Entrar',bg='blue',fg='white', font=self.minhafont2, command=self.entrar)
        self.btn.place(x=65,y=120)

        self.sair = tk.Button(win, text='Sair',bg='red',fg='white', font=self.minhafont2, command=self.Sair)
        self.sair.place(x=185,y=120)

    def entrar(self):
        registro = self.crud.consultar()
        
        longinn = self.login.get()
        senhaaa = self.senha.get()

        cont = 0

        for item in registro:
            loginx = item[1]
            senhax = item[2]

            if longinn == loginx and senhaaa == senhax:
                ms.showinfo(title='Mensagem', message='Entrada Permitida')
                #destruido o texto
                self.loginTxt.destroy()
                self.senhaTxt.destroy()

                #destruido o entry
                self.login.destroy()
                self.senha.destroy()

                #destruido os botões
                self.btn.destroy()
                self.sair.destroy()

                super().__init__()

                # Adicionando texto de login intagram
                self.lab = tk.Label(self.master, text="Digite o Seu Login instagram:", bg='white', font=self.minhafont2)
                self.lab.place(x=0,y=5)

                # Adicionando o texto da senha do instagram
                self.lab2 = tk.Label(self.master, text="Digite a sua senha instagram:", bg='white', font=self.minhafont2)
                self.lab2.place(x=0,y=55)

                # Adicionando os Entry do login e senha
                self.logins = tk.Entry(self.master,bd=2, bg='yellow',width=19,relief="solid",highlightthickness=2, font=self.minhafont2)
                self.logins.place(x=342,y=5)

                self.senhains = tk.Entry(self.master,bd=2,width=19, bg='yellow',relief="solid",highlightthickness=2, font=self.minhafont2, show='*')
                self.senhains.place(x=347,y=55)

                # nomeTxt folower
                self.nameTxt = tk.Label(self.master, text="Digite o nome do influenciador Ex: Sony:", bg='white', font=self.minhafont2)
                self.nameTxt.place(x=0,y=118)

                # nomeEntry follower
                self.name = tk.Entry(self.master, bd=2,width=10, bg='yellow', relief="solid", highlightthickness=2, font=("Arial",16))
                self.name.place(x=472,y=118)

                # Adicionando cronometro
                # self.tempoText = tk.Label(self.master, text="Digite o tempo do encerramento do InstagranBot:", bg='white', font=self.minhafont2)
                # self.tempoText.place(x=0, y=158)

                # # Horatext
                # self.horatext = tk.Label(self.master, text="Hora", font=("Arial",17), bg='white')
                # self.horatext.place(x=3,y=200)

                # # HoraEntry
                # self.hour = StringVar()
                # self.hour.set("00")
                # self.hora = tk.Entry(self.master, width=3, font=("Arial",18,""),textvariable=self.hour, bg='yellow', bd=2, relief="solid")
                # self.hora.place(x=60, y=200)

                # # MinutoText
                # self.minutText = tk.Label(self.master, text="Minutos", font=("Arial",17), bg='white')
                # self.minutText.place(x=107,y=200)

                # # minutoEntry
                # self.min = StringVar()
                # self.min.set("00")
                # self.mininuto = tk.Entry(self.master, width=3, font=("Arial",18,""),textvariable=self.min, bg='yellow', bd=2, relief="solid")
                # self.mininuto.place(x=193,y=200)

                # # SecundosText
                # self.SecundosText = tk.Label(self.master, text="Secundos", font=("Arial",17), bg='white')
                # self.SecundosText.place(x=245,y=200)
                
                # # SecundosEntry
                # self.sec = StringVar()
                # self.sec.set("00")
                # self.secundos = tk.Entry(self.master, width=3, font=("Arial",18,""),textvariable=self.sec, bg='yellow', bd=2, relief="solid")
                # self.secundos.place(x=357,y=200)

                # ===================Caixa de Texto============
                self.frame = tk.Frame(self.master, bg="#85B777")
                self.frame.place(width=616, height=300, x=8,y=265)
                
                # ======= Style Barra =====
                style = ttk.Style()
                style.theme_use('clam')
                style.configure("Vertical.TScrollbar", gripcount=0,
                                background="#50acf2", darkcolor="#0c78c9", lightcolor="#91c5ed",
                                troughcolor="gray", bordercolor="#1322cf", arrowcolor="#090a0a")
                # ======= Barra lateral =====
                self.verscrlbar = ttk.Scrollbar(self.frame, orient="vertical")
                self.verscrlbar.pack(side = 'right', fill = 'y')
                
                # ======= Caixa de Texto =====
                self.caixa_de_texto = tk.Text(self.master, font=('Calibri',16), background="#91d3ed", 
                                                borderwidth = 6, 
                                                relief="solid", 
                                                selectbackground="#F5F799", 
                                                selectforeground="black", 
                                                wrap="word", 
                                                undo=True, 
                                                yscrollcommand = self.verscrlbar.set)
                
                self.caixa_de_texto.place(width=603,height=300,x=8,y=265)
                # ============ configura da barra lateral ===========
                self.verscrlbar.place(x=601, y=0, height=299)
                self.verscrlbar.configure(command = self.caixa_de_texto.yview)

                # Adicionando botão de entrada
                self.btn = tk.Button(self.master, text='Iniciar', bg='blue', fg='white', font=self.minhafont2, command=self.startCrud, highlightcolor="#d11406", highlightbackground="orange")
                # self.btn.place(x=427,y=200, width=100, height=35)
                self.btn.place(x=5,y=200, width=100, height=35)
                
                janela.geometry('634x570+380+55')
            else:
                print("Entrada Negada")
                ms.showerror(title='Erro ao Longar', message='Dados Invalidos...')

            cont = cont + 1
        
    def startCrud(self):
        email = self.logins.get()
        senha_insta = self.senhains.get()
        nome = self.name.get()
        
        self.master.update()
        self.insta = InstagramBot(email, senha_insta)
        time.sleep(5)

        self.insta.eliminando_botoes_indesejados()
        time.sleep(5)

        self.insta.pagina_da_pessoa(nome)
        time.sleep(5)

        self.curtir()

    def curtir(self):
        try:
            btn_curtir = self.insta.bot.find_element(by=By.XPATH, value="//button[@class='_acan _acap _acas']")
            btn_curtir.click()
            time.sleep(2)
            self.caixa_de_texto.insert(END, "curtiu\n")
        except Exception as e:
            print(f'erro: {e}')
            pass

        i = 1

        while (True):
            self.master.update()
            i+= 100
            self.insta.bot.execute_script(f'window.scrollTo(0,{i})')
            self.curtir()

    def Sair(self):
        self.master.destroy()

class Menu:
    def __init__(self, window):
        self.winn = window
        menubar = tk.Menu(self.winn)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Ajuda", command=self.ajuda)
        filemenu.add_separator()
        filemenu.add_command(label="Sobre", command=self.info)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="Cadastrar Usuário", command=self.cadastrar)
        menubar.add_cascade(label="Help", menu=filemenu)
        janela.config(menu=menubar)

    def cadastrar(self):
        vieCad = tk.Toplevel(self.winn)
        vieCad.title("Software Instagran")
        
        label1 = tk.Label(vieCad, text="Criar Login:")
        label2 = tk.Label(vieCad, text='Criar Senha:')

        label1.place(x=0,y=0)
        label2.place(x=0, y=45)

        self.entrada1 = tk.Entry(vieCad)
        self.entrada2 = tk.Entry(vieCad, show='*')

        self.entrada1.place(x=65, y=3, width=222)
        self.entrada2.place(x=67,y=47, width=222)

        btnconfirma = tk.Button(vieCad, text='Confirmar', command=self.salvarConta)
        btnconfirma.place(x=105, y=75)

        vieCad.geometry('296x110')
        vieCad.mainloop()

    def salvarConta(self):
            login = self.entrada1.get()
            senha = self.entrada2.get()
            
            crud = InstaCrud()

            if crud.cadastrar(login, senha) == True:
                
                crud.consultar_ultimo_id()

                ms.showinfo(title='Mensagem', message='Cadastro executado com sucesso!')

                self.entrada1.delete(0, tk.END)
                self.entrada2.delete(0, tk.END)

            else:
                ms.showerror(title="Mensagem", message="Erro no cadastro!")

                self.entrada1.focus_set()
                self.entrada2.focus_set()



    def ajuda(self):
        ajudaview = tk.Toplevel(self.winn)
        ajudaview.title("Software Instagran")
        ajudaview.geometry('485x230')

        minhafont = font.Font(family="Helvetica",size=18,weight="bold")

        img = tk.PhotoImage(file='C:/Users/Usuario/Desktop/aplication/instagran/imagem/logo.png')
        
        imagemLogo = tk.Label(ajudaview, image=img,height=120, bg='white')
        imagemLogo.place(x=90,y=0)

        text1 = tk.Label(ajudaview, text="Entre em Contato para eu poder te ajudar", bg='white', font=minhafont)
        text2 = tk.Label(ajudaview, text='Email:', bg='white', font=minhafont)
        text3 = tk.Label(ajudaview, text="ihuryferreira@icloud.com", bg='white', fg='blue', font=minhafont)
        text1.place(x=0,y=140)
        text2.place(x=0,y=180)
        text3.place(x=80,y=180)

        ajudaview.configure(background='white')
        ajudaview.mainloop()

    def info(self):
        self.mens = 'Name: Software Instagram Bot\nVersion: 1.0.0\nAutor: Ihury Ferreira\nDate: 14/06/2022'
        ms.showinfo(title='Sobre', message=self.mens)

janela = tk.Tk()
janela.title('Software Instagran')
janela.geometry('320x200+517+224')
janela.configure(background='white')
prin = LoginPrinc(janela)
mn = Menu(janela)
janela.mainloop()