import random
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import random
import time

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

ai_win = {"ko", "op", "pk"}
human_win = {"ok", "po", "kp"}
ai_tipp = ""
human_tipp = ""
aitippp = "ismeretlen"



"""
ko_img = Image.open("ko_button.jpg").resize((100, 160))
ko_foto = ImageTk.PhotoImage(ko_img)
papir_img = Image.open("papir_button.jpg").resize((100, 160))
papir_foto = ImageTk.PhotoImage(papir_img)
ollo_img = Image.open("ollo_button.jpg").resize((100, 160))
ollo_foto = ImageTk.PhotoImage(ollo_img)
"""

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def whowin(eredmeny):
    if eredmeny in ai_win:
        ai.score += 1
        print("Ezt a menetet a CPU nyerte!")
        return
    elif eredmeny in human_win:
        human.score += 1
        print("Ezt a menetet {} nyerte!".format(human.name))
        return
    else:
        print("Ez döntetlen lett.")
        return

#uresphoto = ImageTk.PhotoImage(file=r"ures_button100.jpg")

def h_tipp(human_tipp):
    global uresphoto
    ai_tipp = random.choice(["k", "p", "o"])
    #uresfoto()
    kepvaltas(ai_tipp)
    """
    if ai_tipp == "k":
        ai_tippp = "kő"
        aiphotoNew = ImageTk.PhotoImage(file=r"ko_button100.jpg")
        mi_Label.configure(image=aiphotoNew)
        mi_Label.image = aiphotoNew
    elif ai_tipp == "p":
        ai_tippp = "papír"
        aiphotoNew = ImageTk.PhotoImage(file=r"papir_button100.jpg")
        mi_Label.configure(image=aiphotoNew)
        mi_Label.image = aiphotoNew
    else:
        ai_tippp = "olló"
        aiphotoNew = ImageTk.PhotoImage(file=r"ollo_button100.jpg")
        mi_Label.configure(image=aiphotoNew)
        mi_Label.image = aiphotoNew
    """
    #aitippp.set(ai_tippp)
    eredmeny = ai_tipp + human_tipp
    whowin(eredmeny)
    print(human.score)
    humanscore.set(human.score)
    print(ai.score)
    aiscore.set(ai.score)
    return eredmeny

def create_game():
    pass

"""
def uresfoto():
    aiphotoNew = ImageTk.PhotoImage(file=r"ures_button100.jpg")
    mi_Label.configure(image=aiphotoNew)
    mi_Label.image = aiphotoNew
    print("üresfotó")
    time.sleep(2)
    return
"""

def kepvaltas(ai_tipp):
    time.sleep(0.7)
    if ai_tipp == "k":
        aiphotoNew = ImageTk.PhotoImage(file=r"ko_button100.jpg")
        mi_Label.configure(image=aiphotoNew)
        mi_Label.image = aiphotoNew
    elif ai_tipp == "p":
        aiphotoNew = ImageTk.PhotoImage(file=r"papir_button100.jpg")
        mi_Label.configure(image=aiphotoNew)
        mi_Label.image = aiphotoNew
    else:
        aiphotoNew = ImageTk.PhotoImage(file=r"ollo_button100.jpg")
        mi_Label.configure(image=aiphotoNew)
        mi_Label.image = aiphotoNew
    return



def gamer_name_enter(event):
    mianeved_ablak.after_idle(root.attributes, '-topmost', False)
    mianeved_ablak.destroy()
    mianeved_ablak.update()
    root.lift()
    root.attributes('-topmost', True)


def gamer_name():
    mianeved_ablak.after_idle(root.attributes, '-topmost', False)
    mianeved_ablak.destroy()
    mianeved_ablak.update()
    root.lift()
    root.attributes('-topmost', True)


def confirm_quit():
    root.destroy()


def show_game_info():
    pass

root = tk.Tk()
root.title("Kő - Papír - Olló by atty")
root.option_add("*tearOff", False)

root.geometry("600x400")
root.resizable(False, False)

player_name = tk.StringVar()
#player_name.set("attyhor")

ai = Player("CPU", 0)
human = Player(player_name, 0)

#main.pack(fill="both", expand=True, padx=1, pady=(4, 0))

"""
Menü
"""
menubar = tk.Menu(root)
root.config(menu=menubar)

game_menu = tk.Menu(menubar)
help_menu = tk.Menu(menubar)

menubar.add_cascade(menu=game_menu, label="Game")
menubar.add_cascade(menu=help_menu, label="Help ")


game_menu.add_command(label="Új játék", command=create_game, accelerator="Ctrl+N")
game_menu.add_command(label="Név megadása", command=gamer_name, accelerator="Ctrl+O")
game_menu.add_command(label="Kilépés", command=confirm_quit, accelerator="Ctrl+Q")

help_menu.add_command(label="Segítség", command=show_game_info)


#root.bind("<KeyPress>", lambda event: check_for_changes())
root.bind("<Control-n>", lambda event: create_game())
root.bind("<Control-o>", lambda event: gamer_name())

root.bind("<Control-q>", lambda event: confirm_quit())


"""
Névbekérő Toplevel
"""

mianeved_ablak = tk.Toplevel()
mianeved_ablak.title("Neved?")
mianeved_ablak.lift()
mianeved_ablak.attributes('-topmost',True)
mianevedLabel = tk.Label(mianeved_ablak, text="Kérem a neved:")
mianevedLabel.pack(side="left")
neved_input = tk.Entry(mianeved_ablak, textvariable=player_name)
neved_input.pack(side="left")
neved_input.focus_set()
mianeved_ablak.bind('<Return>', gamer_name_enter)
mianeved_ablak.bind('<KP_Enter>', gamer_name_enter)
nevedokgomb = tk.Button(mianeved_ablak, text="OK", command=gamer_name)
nevedokgomb.pack(side="right")


"""
fő képernyő
"""



name_frame = ttk.Frame(root, padding=(20, 30, 20, 0))
name_frame.pack(fill="both")


playerLabel = tk.Label(name_frame, textvariable="{}".format(player_name))
playerLabel.config(font=("", 14, "bold"), fg="green")
playerLabel.pack(side="left", fill="x", expand=True, padx=(10, 10))
cpuLabel = tk.Label(name_frame, text="CPU")
cpuLabel.config(font=("", 14, "bold"), anchor="e", justify="left", fg="red")
cpuLabel.pack(side="left", fill="x", expand=True, padx=(10, 10))

buttons_frame = ttk.Frame(root, padding=(20, 10))
buttons_frame.pack(fill="both")

aitippp = tk.StringVar()
aitippp.set("semmi")


kophoto = ImageTk.PhotoImage(file=r"ko_button100.jpg")
papirphoto = ImageTk.PhotoImage(file=r"papir_button100.jpg")
ollophoto = ImageTk.PhotoImage(file=r"ollo_button100.jpg")
aiphoto = ImageTk.PhotoImage(file=r"ures_button100.jpg")


ko_button = tk.Button(buttons_frame, image=kophoto, command=lambda: h_tipp("k"))
ko_button.pack(side="left")
papir_button = tk.Button(buttons_frame, image=papirphoto, command=lambda: h_tipp("p"))
papir_button.pack(side="left")
ollo_button = tk.Button(buttons_frame, image=ollophoto, command=lambda: h_tipp("o"))
ollo_button.pack(side="left")
mi_Label = tk.Label(buttons_frame, image=aiphoto)
#mi_Label = tk.Label(buttons_frame, textvariable=aitippp)
mi_Label.pack(side="right")

eredmenyLabel = tk.Label(root, text="XY Nyert!")
eredmenyLabel.pack(fill="both")

allas_frame = ttk.Frame(root, padding=(20, 10))
allas_frame.pack(fill="both")

humanscore = tk.StringVar()
humanscore.set(human.score)
print(human.score)
aiscore = tk.StringVar()
aiscore.set(ai.score)
print(ai.score)


humanLabel = tk.Label(allas_frame, textvariable=humanscore)
humanLabel.pack(side="left", expand=True)

aiLabel = tk.Label(allas_frame, textvariable=aiscore)
aiLabel.pack(side="right", expand=True)



root.mainloop()