import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from wordlister import WordList

word_list = WordList("word-data")

root = tk.Tk()
root.title("Resolutor Letreco")
root.geometry("300x200")
root.minsize(300, 200)
root.maxsize(300, 200)

# WORDS LIST
left_frame = ttk.Frame(root, padding=10)
scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL)
list_box = tk.Listbox(left_frame, yscrollcommand=scrollbar.set)

list_box.insert(tk.END, *word_list.words)
scrollbar.config(command=list_box.yview)

list_box.pack(side=tk.LEFT, fill=tk.Y)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
left_frame.pack(side=tk.LEFT, fill=tk.Y, expand=False)
# WORDS LIST


# FILTER OPTIONS
def update():
    list_box.delete(0, tk.END)
    list_box.insert(tk.END, *word_list.words)
    root.update()

def remove_let():
    letters = entry_widgt.get().split()
    word_list.remove_letters(letters)
    update()

def include_lt():
    letters = entry_widgt.get().split()
    word_list.include_letters(letters)
    update()

def place_lett():
    letters = list(map(lambda x: x.split(","), entry_widgt.get().split(" ")))
    try:
        word_list.place_letters(letters)
        update()
    except ValueError:
        messagebox.showerror("Sintaxe incorreta", "Para posicionar letras use a sintaxe\"letra1,posicao1 letra2,posicao2 ...\"")

def remove_pos():
    letters = list(map(lambda x: x.split(","), entry_widgt.get().split(" ")))
    try:
        word_list.remove_positions(letters)
        update()
    except ValueError:
        messagebox.showerror("Sintaxe incorreta", "Para posicionar letras use a sintaxe\"letra1,posicao1 letra2,posicao2 ...\"")

def undo():
    word_list.undo_last_filter()
    update()

def reset_list():
    word_list.restore_list()
    update()

right_frame = ttk.Frame(root, padding=10)
right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
entry_widgt = ttk.Entry(right_frame)
entry_widgt.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

ttk.Button(right_frame, text="Remover Letras",    command=remove_let).pack(side=tk.TOP, fill=tk.X, expand=True)
ttk.Button(right_frame, text="Incluir Letras",    command=include_lt).pack(side=tk.TOP, fill=tk.X, expand=True)
ttk.Button(right_frame, text="Posicionar Letras", command=place_lett).pack(side=tk.TOP, fill=tk.X, expand=True)
ttk.Button(right_frame, text="Remover Posição",   command=remove_pos).pack(side=tk.TOP, fill=tk.X, expand=True)
ttk.Button(right_frame, text="Restaurar Lista",   command=reset_list).pack(side=tk.TOP, fill=tk.X, expand=True)
# FILTER OPTIONS

root.mainloop()
