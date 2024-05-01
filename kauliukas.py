from tkinter import *
import random
from datetime import datetime
from tkinter import messagebox

window = Tk()
history = []
history_window = None
info_window = None

def generate():
    selected_nums = [var1.get(), var2.get(),
                     var3.get(), var4.get(),
                     var5.get(), var6.get()]

    if not any(selected_nums):
        messagebox.showinfo("Pastaba!", "Pasirinkite su kuriais kauliukais žaisite. ")
        messagebox.showinfo("Pagalba", "Daugiau informacijos, paspauskite klavišą i ")
        return

    generated_numbers = [random.randint(1, 6) for i, val in enumerate(selected_nums) if val == 1]
    generated_numbers = [str(num) for num in generated_numbers]
    history.append((generated_numbers, datetime.now().strftime("%H:%M:%S")))
    show_result(generated_numbers)

def clear_result():
    for widget in window.winfo_children():
        if isinstance(widget, Label):
            if widget.winfo_y() > (window.winfo_height() / 2):
                widget.destroy()

def show_result(numbers):
    clear_result()
    result_str = " ".join(numbers)
    label2 = Label(window, text=result_str, font=("Verdana", 34))
    label2.grid(row=5, column=0, columnspan=15)

def show_history():
    global history_window
    def update_history():
        history_listbox.delete(0, END)
        history_listbox.configure(bg="grey")

        if not history:
            history_listbox.insert(END, "Istorija tuščia")
        else:
            for i, (generated_numbers, generation_time) in enumerate(history, start=1):
                result_str = "  ".join(generated_numbers)
                history_listbox.insert(END, f"{i}. Laikas:{generation_time} Rezultatas: {result_str}")
        history_listbox.yview_moveto(1.0)
        window.after(1000, update_history)

    if history_window is None or not history_window.winfo_exists():
        history_window = Toplevel(window)
        history_window.geometry("+550+100")
        history_window.iconbitmap(r'dice.ico')
        history_window.title("Ridenimo istorija")
        scrollbar = Scrollbar(history_window)
        scrollbar.pack(side=RIGHT, fill=Y)
        history_listbox = Listbox(history_window, yscrollcommand=scrollbar.set, font=("Verdana", 15), width=42, height=25)
        history_listbox.pack(side=LEFT)
        scrollbar.config(command=history_listbox.yview)
        update_history()

def show_info():
    global info_window
    if info_window is None or not info_window.winfo_exists():
        info_window = Toplevel(window)
        info_window.geometry("+200+500")
        info_window.iconbitmap(r'dice.ico')
        info_window.title("Informacija")
        info_listbox = Text(info_window, height=30, width=70)
        info_listbox.configure(bg="grey")
        info_listbox.pack(side=LEFT)
        info = """
         Informacija naudotojui:
     Programa sukurta ridenti kauliukus. Pasirenkami,
     konkretūs kauliukai (yra prietaringų žmonių,
     kuriem, toks pasirinkimas patiks) bei kauliukų kiekis.
     Ridenama - paspaudus mygtuką po pasirenkamais kauliukais
     arba klaviatūroje, paspaudus klavišą ENTER arba SPACE.
     Rezultatas rodomas apatinėje lango dalyje. Ridenti galima
     daug kartų. Kad nepasitaikytų sukčiavimo atvejų,
     yra sukurta ridenimų istorija. Ją rasite, paspaudę
     Daugiau > Istorija. Istorijoję, rasite laiką
     (valandas, minutes ir sekundes), kada buvo ridenama.
     Dviejų ridenimų, vienodu laiku, neįmanoma atlikti.
     Norint uždaryti programą, reikia paspausti Daugiau > Išėjimas,
     arba klaviatūroje klavišą ESC, arba iksiuką,
     esantį dešiniajam, viršutiniam kampe.

           Greitieji klavišai:
        ENTER - Ridenam pasirinktus kauliukus.
        SPACE - Ridenam pasirinktus kauliukus.
        i - Atidaromas, šis informacijos langas.
        ESC - Uždaro programą.

    """
    info_listbox.insert(END, info)

def clear_and_generate():
    clear_result()
    window.after(2000, generate)

def exit():
    window.destroy()

def on_return(event):
    clear_and_generate()

def on_space(event):
    clear_and_generate()

def close_program(event):
    window.destroy()

def e_info(event):
    show_info()

window.attributes('-topmost', True)
window.title("KAULIUKAS")
window.iconbitmap(r'dice.ico')
window.geometry("300x190")
window.resizable(width=False, height=False)
button_decoration = PhotoImage(file="button.png")
label_primary = Label(window, text="Pasirinkite, kurie kauliukai naudojami:", font=("Verdana", 11))
button = Button(window, image=button_decoration)
label_decoration = Label(window, width=42, height=5, relief="ridge")
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()

menu_bar = Menu(window)
window.config(menu=menu_bar)
menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Daugiau", menu=menu)
menu.add_command(label="Informacija", command=show_info)
menu.add_separator()
menu.add_command(label="Istorija", command=show_history)
menu.add_separator()
menu.add_command(label="Išėjimas", command=exit)

label_primary.grid(row=0, column=1, columnspan=11)
button.grid(row=4, column=0, columnspan=3, sticky=EW)
button.config(command=clear_and_generate)
label_decoration.grid(row=5, column=0, columnspan=15, sticky=E)

check1 = Checkbutton(window, text="I", variable=var1)
check1.grid(row=1, column=1)
check2 = Checkbutton(window, text="II", variable=var2)
check2.grid(row=1, column=2)
check3 = Checkbutton(window, text="III", variable=var3)
check3.grid(row=1, column=3)
check4 = Checkbutton(window, text="IV", variable=var4)
check4.grid(row=1, column=4)
check5 = Checkbutton(window, text="V", variable=var5)
check5.grid(row=1, column=5)
check6 = Checkbutton(window, text="VI", variable=var6)
check6.grid(row=1, column=6)

window.bind("<Return>", on_return)
window.bind("<space>", on_space)
window.bind("<Escape>", close_program)
window.bind("<i>", e_info)
window.mainloop()