import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,commondialog,messagebox,filedialog
import os
win = tk.Tk()
win.title("Texteditor")
win.geometry("1300x700")
############################### Menubar #######################################
main_menu = tk.Menu()
file_menu = tk.Menu(main_menu,tearoff=False)
#$$$$$$$$$$$$$$$$$$$$$$-----------------File menu----------------
file_name = ''
def new_file(event=None):
    global file_name
    file_name = ''
    text_editor.delete(1.0,tk.END)

file_menu.add_command(label="New",compound=tk.LEFT,accelerator="Ctrl+N",command=new_file)
win.bind('<Control n>',new_file)
#openfile 
def open_file(event=None):
    global file_name
    file_name = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select file",filetype=(('Text file','*.txt'),('all file','*.*')))
    try:    
        with open(file_name,'r') as fr:
             text_editor.delete(1.0,tk.END)
             text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        tk.showwarning(title="warning",message="file is not found")
    except:
        tk.showerror(title="error",message="error")
    win.title(os.path.basename(file_name) ) 

file_menu.add_command(label="open",compound=tk.LEFT,accelerator="Ctrl+O",command=open_file)
win.bind('<Control o>',open_file)
#savefile
def save_file(event=None):
    global file_name
    try:
        if file_name:
            content = str(text_editor.get(1.0,tk.END))
            with open(file_name,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            file_name = filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetype=(('Text file','*.txt'),('all file','*.*')))
            content2 = str(text_editor.get(1.0,tk.END))
            file_name.write(content2)
            file_name.close()
    except:
        return
file_menu.add_command(label="Save",accelerator="Ctrl+S",command=save_file)
win.bind('<Control s>',save_file)
#save as
def save_as():
    global file_name
    file_name = filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetype=(('Text file','*.txt'),('all file','*.*')))
    content2 = str(text_editor.get(1.0,tk.END))
    file_name.write(content2)
    file_name.close()

file_menu.add_command(label="Save As",accelerator="Ctrl+Alt+S",command=save_as)
file_menu.add_separator()
#exit
def Exit():
    global change_char,file_name
    if change_char:
        msb = messagebox.askyesnocancel(title="exit",message="save file or not")
        if msb is True: 
            if file_name:
                content = str(text_editor.get(1.0,tk.END))
                with open(file_name,'w',encoding='utf-8') as fw:
                    fw.write(content)
                win.destroy()
            else:
                file_name = filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetype=(('Text file','*.txt'),('all file','*.*')))
                content2 = str(text_editor.get(1.0,tk.END))
                file_name.write(content2)
                file_name.close()
                win.destroy()
        if msb is False:
             win.destroy()
    else:
        win.destroy()

file_menu.add_command(label="Exit",accelerator="Ctrl+Q",command=Exit)
win.bind('<Control q>',Exit)
############### end #########################
edit_menu = tk.Menu(main_menu,tearoff=False)
########Edit menu-------------------
edit_menu.add_command(label="Copy",compound="left",accelerator="Ctrl+C",command=lambda:text_editor.event_generate('<Control c>'))
edit_menu.add_command(label="Cut",accelerator="Ctrl+X",command=lambda:text_editor.event_generate('<Control x>'))
edit_menu.add_command(label="Paste",accelerator="Ctrl+V",command=lambda:text_editor.event_generate('<Control v>'))
edit_menu.add_separator()
edit_menu.add_command(label="Clear",accelerator="Ctrl+Alt+C",command=lambda:text_editor.delete(1.0,tk.END))
############### end #########################
view_menu = tk.Menu(main_menu,tearoff=False)
#########view menu--------------
text_bar = tk.Label(win)

text_bar.pack(side=tk.TOP,fill=tk.X)
    
tool_check = tk.IntVar()   
view_menu.add_checkbutton(label="Toolbar",variable=tool_check)
############### end #########################
color_theme_menu = tk.Menu(main_menu,tearoff=False)
def change_theme():
    if check.get():
       text_editor.configure(bg="#666666")
    else:
        text_editor.configure(bg="#ffffff")
check = tk.IntVar()
color_theme_menu.add_checkbutton(label="dark theme",variable=check,command=change_theme)
main_menu.add_cascade(label="File",menu=file_menu)
main_menu.add_cascade(label="Edit",menu=edit_menu)
main_menu.add_cascade(label="View",menu=view_menu)
main_menu.add_cascade(label="Theme",menu=color_theme_menu)
#&&&&&&&&&&&&&&&&&&&&&&&&****TOOLBAR*****&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
font_list = tuple(tk.font.families())
font_family = tk.StringVar()
font_box = ttk.Combobox(text_bar,width="30",textvariable=font_family,state="readonly")
font_box['values'] = font_list
font_box.current(font_list.index('Arial'))
font_box.grid(row=0,column=0,padx=5)
#&
font_size_list = tuple(range(8,72))
font_size = tk.IntVar()
font_size_box = ttk.Combobox(text_bar,textvariable=font_size,state="readonly")
font_size_box['values'] = font_size_list
font_size_box.current(4)
font_size_box.grid(row=0,column=1,padx=5)
#&
bold_text = tk.StringVar()
bold_icon = tk.PhotoImage(file="image/bold.png")
bold_button = tk.Button(text_bar,image=bold_icon,textvariable=bold_text)
bold_button.grid(row=0,column=2,padx=5)
bold_button.configure(fg="#0000ff")
#&
color_text = tk.StringVar()
color_icon = tk.PhotoImage(file="image/color.png")
color_button = tk.Button(text_bar,image=color_icon,textvariable=color_text)
color_button.grid(row=0,column=3,padx=5)
#************************** End Menubar ***************************************
text_editor = tk.Text(win)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar = ttk.Scrollbar(win)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
text_editor.configure(padx=15)
#******************* font change ***********
select_font_family = "Arial"
select_font_size = 12
def change_font_family(win):
    global select_font_family
    select_font_family = font_family.get()
    text_editor.configure(font=(select_font_family,select_font_size ))

def change_font_size(win):
     global select_font_size
     select_font_size = font_size.get()
     text_editor.configure(font=(select_font_family,select_font_size ))
font_size_box.bind("<<ComboboxSelected>>",change_font_size)
font_box.bind("<<ComboboxSelected>>",change_font_family)
text_editor.configure(font=(select_font_family,select_font_size ))
######################*****************************************
def bold_text_change(event=None):
  #  {'family': 'Arial', 'size': 12, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property['weight']=='normal':
       text_editor.configure(font=(select_font_family,select_font_size,'bold'))
    if text_property['weight']=='bold':
       text_editor.configure(font=(select_font_family,select_font_size,'normal'))

bold_button.configure(command=bold_text_change)
#$$$$$$$$$$$$$$$$$$
def change_color(event=None):
    color = colorchooser.askcolor()
    text_editor.configure(fg=color[1])
    print(color[1])
color_button.configure(command=change_color)
#-----------------------status bar---------------->       
status_bar = tk.Label(win,text="status:",justify='center')
status_bar.pack(side=tk.BOTTOM,fill=tk.X)
change_char = False
def status(even=None):
    global change_char
    if text_editor.edit_modified():
        change_char = True
        char = len(text_editor.get(1.0,"end-1c"))
        word = len(text_editor.get(1.0,"end-1c").split())
        status_bar.configure(text=f"characters: {char}        words: {word}")
        text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",status)
win.configure(menu=main_menu)
win.mainloop()
