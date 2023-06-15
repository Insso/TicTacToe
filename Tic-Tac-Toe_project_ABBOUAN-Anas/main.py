import tkinter


window = tkinter.Tk()
window.title("My first Tic Tac Toe ")

#tableau du jeu
leTab = [["", "", ""], ["", "", ""], ["", "", ""]]


lePlayer = "X"

# Bouton réinitialiser
resetButton = tkinter.Button(window, text="Réinitialiser")
resetButton.grid(row=3, column=0, columnspan=3)

# Fonction pour réinitialiser le jeu
"""La fonction ci-dessous utilise une var global 
   c'est plus simple pour moi d'avoir une main sur 
   qui a la main justement"""
def resetTheGame():
    global lePlayer

    # relance le tab
    for i in range(3):
        for j in range(3):
            leTab[i][j] = ""
            lesButtons[i][j].config(text="")

    lePlayer = "X" 

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