import tkinter


window = tkinter.Tk()
window.title("My first Tic Tac Toe ")

#tableau du jeu
leTab = [["", "", ""], ["", "", ""], ["", "", ""]]


lePlayer = "X"

# Bouton réinitialiser
resetButton = tkinter.Button(window, text="Réinitialiser")
resetButton.grid(row=3, column=0, columnspan=3)

# Créer les boutons pour chaque case
lesButtons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tkinter.Button(window, text="", width=10, height=5,
                               command=lambda row=i, col=j: cell_click(row, col))
        button.grid(row=i, column=j)
        row.append(button)
    lesButtons.append(row)

# Lancer du jeu
window.mainloop()

#window.title('Anas s GUI V3')
# label=tkinter.Label(window,text="Ma fst GUI window perso")
# label= tkinter.Label(window,text="Je use tkinter library",background="blue").pack()

# #clicable button
# bt=tkinter.Button(text="Cliiiiick euh").pack()
# window.geometry("300x200+10+10")

# #user input
# txt=tkinter.Entry(width=20).pack()

# #big text box
# textBox=tkinter.Text()
# textBox.pack()