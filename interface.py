import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("Exemple de fenêtre Tkinter")

# Création d'un champ de saisie (entry)
entry = tk.Entry(root, width=30)
entry.pack()

# Création d'un bouton avec une fonction associée
def button1_action():
    print("Vous avez appuyé sur le bouton 1 !")
button1 = tk.Button(root, text="Bouton 1", command=button1_action)
button1.pack()

# Création d'un autre bouton avec une autre fonction associée
def button2_action():
    texte = entry.get()  # récupère le texte saisi dans le champ de saisie
    print(f"Vous avez appuyé sur le bouton 2 et saisi : {texte}")
button2 = tk.Button(root, text="Bouton 2", command=button2_action)
button2.pack()

# Création d'un troisième bouton
button3 = tk.Button(root, text="Bouton 3")
button3.pack()

root.mainloop()
