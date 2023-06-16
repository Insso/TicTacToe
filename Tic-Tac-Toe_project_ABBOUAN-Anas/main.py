import tkinter
from tkinter import messagebox #meilleurs moyen d'affiche une nouvelle window pour des message

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

# check-up pour savoir si un joueur a gg
"""À chaque fois qu'une case est cliqué
   on vérifie si le joueur actuel a gagné"""
def checkWin(player):
    for i in range(3):
        if leTab[i][0] == leTab[i][1] == leTab[i][2] == player or leTab[0][i] == leTab[1][i] == leTab[2][i] == player:
            return True
    if leTab[0][0] == leTab[1][1] == leTab[2][2] == player or leTab[0][2] == leTab[1][1] == leTab[2][0] == player:
        return True
    return False


# des boutons cliquable pour chaque case
lesButtons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tkinter.Button(window, text="", width=15, height=5, command=lambda row=i, col=j: clique(row, col))
        button.grid(row=i, column=j)
        row.append(button)
    lesButtons.append(row)

#ma dernière fct après jpeux m'amuser a add des options
"""basique hein
   j'ai surtout du ajouter une classe en faisant import from
   pour ajouter messagebox"""
def clique(row, col):
    global lePlayer

    # on check si la case est remplie
    if leTab[row][col] != "":
        return

    # on ajoute le symbole du joueur ds la case
    leTab[row][col] = lePlayer
    lesButtons[row][col].config(text=lePlayer)

    # on check si le current joueur a gg
    if checkWin(lePlayer):
        messagebox.showinfo("Tic Tac Toe", f"Le joueur {lePlayer} a gagné!")
        resetTheGame()
    else:
        #sinon chgt de joueur
        lePlayer = "O" if lePlayer == "X" else "X"

# Begin !
window.mainloop()