import poke_api2
from tkinter import *
from tkinter import ttk
import os
import ctypes
import image_lib


# Get the path of the script and its parent directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
image_cashe_dir = os.path.join(script_dir, 'images')

#make image cashe folder if it doesnt exist
if not os.path.isdir (image_cashe_dir):
    os.makedirs(image_cashe_dir)


root = Tk()
root.title('Pokemon Image Viewer')

# Set the window icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('comp593.PokeImageViewer')
icon_path = os.path.join(script_dir, 'Poke-Ball.ico')
root.iconbitmap(icon_path)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Print paths to see what they are
print(script_path, script_dir, icon_path, sep='\n')

#create fram
frm = ttk.Frame(root)
frm.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)

#add image to fame
img_poke = PhotoImage(file=os.path.join(script_dir, 'Pokemon-Logo.png'))
lbl_poke_image = ttk.Label(frm, image=img_poke)
lbl_poke_image.grid(padx=10, pady=10)

#pulldown list
poke_name_list = sorted(poke_api2.get_poke_names())
cbox_poke_names = ttk.Combobox(frm, values=poke_name_list, state='readonly')
cbox_poke_names.set("Select a Pokemon")
cbox_poke_names.grid(padx=10, pady=10)

def handle_poke_sel(event):

    poke_name = cbox_poke_names.get()
    global image_path
    image_path = poke_api2.download_artwork(poke_name, image_cashe_dir)

    if image_path is not None:
        img_poke['file'] = image_path
        btn_set_desktop.state(['!disabled'])
    
cbox_poke_names.bind('<<ComboboxSelected>>', handle_poke_sel)

def btn_desktop_bg():
    image_lib.set_desktop_background_image(image_path)

    return


btn_set_desktop = ttk.Button(frm, text='Set as Background', command=btn_desktop_bg, state=DISABLED)
btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)

#b.state(disable)


root.mainloop()