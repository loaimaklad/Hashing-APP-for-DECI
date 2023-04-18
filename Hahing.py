#app is made by loai khalid by tkinter/python !-- Loay Copyright 2022 - 2023
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def rootgui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("800x700+294+68")
        top.resizable(0,0)
        top.title("MyNewApp")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.029, relheight=0.21, relwidth=1.01)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#0cdbff")
        self.Frame1.configure(highlightbackground="#0cdbff")
        self.Frame1.configure(highlightcolor="#0cdbff")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.272, rely=0.34, height=60, width=333)
        self.Label1.configure(activeforeground="")
        self.Label1.configure(background="#0cdbff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial} -size 24")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Hashing APP BY Loai''')
        
        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.188, rely=0.314, height=40, relwidth=0.593)
        self.Entry1.configure(background="white")
        self.Entry1.configure(borderwidth="0")
        self.Entry1.configure(cursor="arrow")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Arial} -size 24")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.225, rely=0.586, height=51, width=396)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Arial} -size 24")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Encrypted data :''')

        
        self.Label4 = tk.Entry(top)
        self.Label4.place(relx=0.225, rely=0.790, height=51, width=396)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Arial} -size 24")
        self.Label4.configure(foreground="#000000")
        #self.Label4.bind("<Foucs-In>",self.Label4.configure(state="disabled"))
        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.238, rely=0.229, height=42, width=368)
        self.Label2.configure(background="#a7a7a7")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial} -size 24")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Enter Data to Encrypt :''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.788, rely=0.314, height=34, width=117)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        
        self.Button1.configure(compound='bottom')
        self.Button1.configure(cursor="arrow")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(overrelief="groove")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="groove")
        def save(d):
        	x=open("data.txt",'x+')
        	x.write(d)
        	

        self.Button1.configure(text='''Encrypt''')
        self.button3 = tk.Button(top)
        self.button3.place(relx=0.738,rely=0.78799)
        self.button3.configure(relief="groove",bg="lightgray")
        self.button3.configure(text="Save as txt !",height=2)
        
        ##wanted def-funcs !
        def loay(**kwargs):
            global y ,codepoints
            y = self.Entry1.get()
            codepoints = []
            for x in y:
                s1 = ord(x)+80*2009
                codepoints.append(str(s1))
            self.Label4.delete(0,'end')
            codepoints=' '.join(codepoints)
            self.Label4.insert(0,codepoints)


    #Set button when get binded ..
        self.Button1.configure(command=loay)
        top.bind("<Return>",lambda a :loay())
        global codepoints
        self.button3.configure(command=lambda : save(codepoints))

rootgui()
