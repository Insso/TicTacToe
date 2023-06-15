import tkinter
window = tkinter.Tk()
window.title('Anas s GUI V3')

label=tkinter.Label(window,text="Ma fst GUI window perso")
label= tkinter.Label(window,text="Je use tkinter library",background="blue").pack()

#clicable button
bt=tkinter.Button(text="Cliiiiick euh").pack()
window.geometry("300x200+10+10")

#user input
txt=tkinter.Entry(width=20).pack()

#big text box
textBox=tkinter.Text()
textBox.pack()





window.mainloop()