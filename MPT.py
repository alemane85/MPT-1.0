import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import MyCsv

"""
Questa ti serve
path=filedialog.askopenfilename(initialdir = "/",title = "Open file")
"""
class Program:
    def __init__(self,name="New App",version="0.0",iconbitmap=0):
        self.name=name
        self.version=version
        maxwidth="1200"
        maxheight="900"
        self.window= tk.Tk()
        #self.window.state('zoomed')
        self.window.resizable(False, False)
        if iconbitmap:
            self.window.iconbitmap(iconbitmap)
        self.window.geometry(f"{maxwidth}x{maxheight}")
        #.geometry("window width x window height + position right + position down")

        self.file=MyCsv.MyCsvFile()
        self.init_menubar()
        self.init_optmenu()
        self.init_frame()
        #self.init_tabs()

    def init_menubar(self):
        self.menubar = tk.Menu(self.window)
        self.window.config(menu=self.menubar)

    def init_tabs(self):
        self.tabs = ttk.Notebook(self.window)

    def init_optmenu(self):
        self.optmenu_var=tk.StringVar()
        self.opt_frame=tk.Frame(self.window, width=780, height=25,bg="red")
        self.opt_frame.grid(pady=5, padx=10)
        self.opt_frame.grid(column=0,row=0,columnspan=12)
        self.opt_frame.grid_propagate(False)
        self.opt = ttk.Combobox(self.opt_frame, textvariable=self.optmenu_var)
        self.opt["state"]="readonly"
        self.opt.config(width=89)
        self.opt.grid(column=0)
        #self.opt.grid(pady=10, padx=10)


    def init_frame(self):
        self.frame=tk.Frame(self.window, width=800, height=400, bg="black")
        self.frame.grid(row=20, column=0)
        self.frame.grid_propagate(False)
        self.entry_var=[]

        self.entry_var.append(tk.StringVar())
        self.l1=ttk.Label(self.frame, text="Nome Programma").grid(row=5, column=0)
        self.e1=ttk.Entry(self.frame, width=30, textvariable=self.entry_var[0]).grid(row=5, column=1)

        self.entry_var.append(tk.StringVar())
        self.l2=ttk.Label(self.frame, text="Velocità Piano").grid(row=6, column=0)
        self.e1=ttk.Entry(self.frame, width=30, textvariable=self.entry_var[1]).grid(row=6, column=1)



    def draw_window(self):
        self.window.title(f"{self.name} v. {self.version} - {self.file.name}")

    def draw_menubar(self):
        # FILE MENU
        self.fmenu = tk.Menu(self.menubar, tearoff=0)
        self.fmenu.add_command(label="Nuovo", command=self.new_file)
        self.fmenu.add_command(label="Apri", command=self.load_file)
        self.fmenu.add_command(label="Salva", command=self.save_file)
        self.fmenu.add_command(label="Salva con nome", command=self.saveas_file)
        self.fmenu.add_separator()
        self.fmenu.add_command(label="Esci", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.fmenu)
        # ? MENU
        self.amenu = tk.Menu(self.menubar, tearoff=0)
        self.amenu.add_command(label="Informazioni", command=self.Info)
        self.menubar.add_cascade(label="?", menu=self.amenu)

    def draw_optmenu(self):
        row_names=[]
        for row in self.file.rows:
            row_names.append(row[0])
        self.opt["values"]=row_names
        print("var row_names=")
        print(row_names)
        self.opt.current(0)

        #if self.optmenu_var_id:
        #    self.optmenu_var.trace_vdelete("w", self.optmenu_var_id)
        #nomi=[]
        #i=0
        #self.opt["menu"].delete(0,"end")
        #for thisrecipe in self.file.recipe:
        #    nomi.append(thisrecipe[1])
        #    self.opt["menu"].add_command(label=nomi[i],command=lambda value=nomi[i]: self.optmenu_var.set(value))
        #    i+=1
        #self.optmenu_var.set(nomi[0])
        #self.current_recipe=self.file.recipe[0]

    def draw_tabs(self):
        #PULISCE LE TABS PER RICREARLE
        for item in self.tabs.winfo_children():
            item.destroy()
        #CREA UNA TAB PER OGNI RICETTA
        self.tabs.pack(pady=10, expand=True)
        self.tab=[]
        self.value=[]
        i=0
        for thisrecipe in self.file.recipe:
            self.tab.append(ttk.Frame(self.tabs, width=600, height=600))
            self.tabs.add(self.tab[i], text=thisrecipe[0])
            self.value.append(tk.StringVar())
            self.value[i].set(thisrecipe[0])
            #print(self.value[i].get())
            self.l1=ttk.Label(self.tab[i], text="Nome Programma").grid(column=0, row=1, sticky=tk.W)
            self.e1=ttk.Entry(self.tab[i], width=30, textvariable=self.value[i]).grid(column=1, row=1, sticky=tk.W)
            self.l2=ttk.Label(self.tab[i], text=thisrecipe[2]).grid(column=0, row=2, sticky=tk.W)
            i+=1
            #keyword = ttk.Entry(tab, width=30, text=thisrecipe[1]).grid(column=1, row=0, sticky=tk.W)
            #keyword.focus()
        newtab = ttk.Frame(self.tabs, width=600, height=600)  # second page
        self.tabs.add(newtab, text="*")

    def update_frame(self,*args):
        selection=self.optmenu_var.get()
        #print(selection)
        for row in self.file.rows:
            if selection == row[0]:
                self.row=row
                print("update_frame row=")
                print(self.row)
                break
        self.draw_frame()
        # disegnare fram con self.row a base
    def draw_frame(self):
        i=1
        for thisentry in self.entry_var:
            thisentry.set(f"{self.row[i]}")
            i+=1

    def draw_body(self):
        self.draw_optmenu()
        self.update_frame()
        self.opt.bind("<<ComboboxSelected>>", self.update_frame)
        #self.optmenu_var_id=self.optmenu_var.trace("w", self.update_frame)
        #print(self.optmenu_var_id)
        #self.draw_tabs()
        #labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
        #labelTest.pack(side="top")
        #labelTest.configure(text="The selected item is {}".format(self.variable.get()))
        #variable.trace("w", callback)

    def Info(self):
        messagebox.showinfo("Informazioni", "Modifica Programmi Taglierina 1.0\nCreato da Manenti Alessio")

    def new_file(self):
        self.file.reset()
        self.file.path=""
        self.file.name="New File"
        self.file.fields=['"NOME"', '"Val1"', '"Val2"', '"Val3"', '"Val4"',
                 '"Val5"', '"Val6"', '"Val7"', '"Val8"', '"Val9"',
                 '"Val10"', '"Val11"', '"Val16"', '"Val17"', '"Val18"',
                 '"Val19"', '"Val20"', '"Val21"', '"Val22"', '"Val23"',
                 '"Val24"', '"Val25"']
        self.file.rows=[['Nuovo Programma di taglio', '', '', '', '', '',
                '', '', '', '', '', '',
                '', '', '', '', '', '',
                '', '', '', '']]
        self.row=self.file.rows[0]
        self.error=0
        self.draw_window()
        self.draw_body()

    def load_file(self):
        path=filedialog.askopenfilename(initialdir = "/",title = "Open file")
        puppet_file=MyCsv.MyCsvFile()
        puppet_file.copy_empty(self.file)
        if not puppet_file.load(path):
            messagebox.showerror("File o percorso non validi", "Impossibile aprire il file selezionato.\nFile non compatibile/danneggiato o percorso errato.")
        else:
            self.file.copy_all(puppet_file)
            self.draw_window()
            self.draw_body()
        print(self.file)

    def save_file():
        pass
    def saveas_file():
        pass

    def start(self):
        self.window.mainloop()

    def quit(self):
        self.window.quit()



program=Program(name="MPT",version="1.1",iconbitmap="mpt_icon.ico")
program.new_file()
program.draw_menubar()
program.start()
