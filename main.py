import json
import tkinter as win
from tkinter import Tk, Label, Menu
import os

escopo_global='programas/criador de listas/'
functions = locals()

with open(escopo_global+'listas.json', 'r') as file_json:
    dados=json.load(file_json)

class Application(win.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.master.state("zoomed")
        self.master.title("listador")
        self.master.configure(bg='black')
        # self.master.iconphoto(False, win.PhotoImage(file=escopo_global+''))
        self.barra_ferramentas=Menu(self.master)
        self.master.config(menu=self.barra_ferramentas)
        self.pack()
        self.layout()
    
    def menuBtns(self, nome, botoes):
        self.menuBar=Menu(self.barra_ferramentas,
            tearoff=0, relief=win.FLAT, activeborderwidth=0, border=8, 
            bg='#252525', fg='white',activebackground='#004c99', activeforeground='white'
        )
        self.barra_ferramentas.add_cascade(label=nome ,menu=self.menuBar)
        count_menuBtn=0
        while count_menuBtn < len(botoes):
            self.menuBar.add_command(label=botoes[count_menuBtn][0], command=functions[botoes[count_menuBtn][1]])
            count_menuBtn+=1

    def layout(self):
        self.menuBtns('documentos',[['novo' ,'sobre'], ['abrir','sobre'], ['salvar' ,'sobre'], ['copiar novo', 'sobre']])
        self.menuBtns('geral', [['configurações', 'sobre'], ['sobre', 'sobre'], ['listas', 'sobre']])
        self.lista=win.Frame(bg='#494949', padx=15, pady=15)
        self.outra_parte=win.Frame(bg='#393939', height=self.lista.winfo_screenheight())
    
        self.entrada=win.StringVar()
        self.novo_item=win.Entry(self.lista, bg='#292929', fg='white', textvariable=self.entrada)
        self.add_btn=win.Button(self.lista, text='add', bg='red', fg='white', command=lambda:self.add_item(self ,self.entrada.get()))
        self.add_btn.pack()
        # self.add_btn.bind('<Button-1>', add_item(self.entrada.get()))
        self.novo_item.pack()
        self.itens=win.Frame()
        self.itens.pack()
        self.carregar_itens()
        
        self.lista.pack(side='left', fill='y')
        self.outra_parte.pack(fill='both')

    def carregar_itens(self):
        count_dados=0
        while count_dados < len(dados["interresses"]):
            self.lbls=Label(self.itens, text=dados["interresses"][count_dados], fg='white', bg='#494949')
            self.lbls.pack(pady=2.2)
            count_dados+=1

    def add_item(self ,new_item ,event=False):
        dados["interresses"].append(new_item)
        with open(escopo_global+'listas.json', 'w') as json_file:
            json.dump(dados, json_file, indent=4)


def sobre(event=False):
    mini_janela=Tk()
    mini_janela.configure(bg='white')
    # tirar bordas
    mini_janela.overrideredirect(True)
    # mini_janela.protocol("WM_DELETE_WINDOW", mini_janela.destroy)
    largura=425
    altura=275
    x=(mini_janela.winfo_screenwidth()-largura)/2
    y=(mini_janela.winfo_screenheight()-altura)/2
    mini_janela.geometry("%dx%d+%d+%d"% (largura, altura, x, y))
    mini_janela.resizable(False,False)
    mini_janela_lbl=win.Label(mini_janela ,text='Alerta! Software proibido para uso', fg='#800500')
    btn_fechar=win.Button(mini_janela, text='x', command=mini_janela.destroy, bg='white', fg='black', borderwidth=0)
    mini_janela_lbl.grid(row=3 ,column=3)
    btn_fechar.grid(row=0 ,column=0)

janela=Tk()
app=Application(master=janela)
app.mainloop()


