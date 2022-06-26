import tkinter as tk

root = tk.Tk()
root.title("App One")
root.geometry("500x500")
root.resizable(False, False)
root.config(bg='#232323')

nome = 'pippo'
cognome = 'pippone'
#funzioni
def mostra_messaggio(nome):    
    print("clicck" + nome)

#struttura 

label_titolo = tk.Label(root, text="titolo", font=("Microsoft YaHei", 16), bg="#232323", fg="white")
label_titolo.grid(row=1, column=0, pady=20, padx=50 )

label_subtitolo = tk.Label(root, text="SubTitolo", font=("Microsoft YaHei", 16), bg="#232323", fg="white")
label_subtitolo.grid(row=2, column=0, pady=0, padx=50 )

#input 
input_testo = tk.Entry(root, font=("Microsoft YaHei", 10), bd=3, width=100)
input_testo.grid(row=4, column=0, pady=10)

#area bottoni
button_click = tk.Button(root, text="click", font=("Times New Romans", 12), bg="#eb8034", fg="black", bd=3, width=15, command=mostra_messaggio(f"{nome}"))
button_click.grid(row=3, column=0, pady=10)


root.mainloop() 