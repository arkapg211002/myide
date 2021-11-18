#ARKAPRATIM GHOSH MyIDE
from tkinter import *
from tkinter.filedialog import *
import subprocess
ide=Tk()
ide.title('MyIDE')
#ide.geometry("1500x700")
#ide.maxsize(1500,700)
filepath=''
def setfilepath(path):
    global filepath
    filepath=path
def Run():
    if filepath=='':
        saveprompt=Toplevel()
        text=Label(saveprompt,text='PLEASE SAVE YOUR CODE')
        text.pack()
        return
    command=f'python {filepath}'#current filepath
    process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)#execute
    output,error=process.communicate()
    ideoutput.insert('1.0',output)
    ideoutput.insert('1.0',error)
def saveAs():
    if filepath=='':
        path=asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path=filepath
    with open(path,'w') as file:
        code=edit.get('1.0',END)
        file.write(code)
        setfilepath(path)
def Open():
    path=askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path,'r') as file:
        code=file.read()
        edit.delete('1.0',END)
        edit.insert('1.0',code)
        setfilepath(path)
menu=Menu(ide)
#ACTION
run=Menu(menu,tearoff=0)
run.add_command(label='RUN',command=Run)
menu.add_cascade(label='ACTION',menu=run)
#FILE MENU
File=Menu(menu,tearoff=0)
File.add_command(label='OPEN',command=Open)
File.add_command(label='SAVE',command=saveAs)
File.add_command(label='SAVE AS',command=saveAs)
File.add_command(label='Exit',command=exit)
menu.add_cascade(label='FILE',menu=File)
ide.config(menu=menu)
edit=Text(height=20,bg='#263238',fg="#B0BEC5",font="bookmanoldstyle 15 bold")
edit.pack(fill=X)
ideoutput=Text(height=30,bg='#263238',fg='#B0BEC5',)
ideoutput.pack(fill=X)
ide.mainloop()

