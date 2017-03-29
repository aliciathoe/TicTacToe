from tkinter import *

TTT = Tk()

def Winner(event):
    print("You Win!")

def Loser(event):
    print("Wrong button :( Try again.")

b1 = Button(TTT, bg = "yellow", height = 2, width = 4, text = "1")
b1.bind("<Button-1>", Winner)
b1.grid(row = 1, column = 1)
b2 = Button(TTT,bg = "red", height = 2, width = 4, text = "2")
b2.bind("<Button-1>", Loser)
b2.grid(row = 1, column = 2)
b3 = Button(TTT, bg = "green", height = 2, width = 4,text = "3")
b3.bind("<Button-1>", Loser)
b3.grid(row = 1, column = 3)
b4 = Button(TTT, bg = "red", height = 2, width = 4,text = "4")
b4.bind("<Button-1>", Loser)
b4.grid(row = 2, column = 1 )
b5 = Button(TTT, bg = "green", height = 2, width = 4, text = "5")
b5.bind("<Button-1>", Loser)
b5.grid( row = 2, column = 2 )
b6 = Button(TTT, bg = "yellow", height = 2, width = 4, text = "6")
b6.bind("<Button-1>", Loser)
b6.grid( row = 2, column = 3)
b7 = Button(TTT, bg = "green", height = 2, width = 4, text = "7")
b7.bind("<Button-1>", Loser)
b7.grid(row = 3, column = 1)
b8 = Button(TTT, bg = "yellow", height = 2, width = 4, text = "8")
b8.bind("<Button-1>", Loser)
b8.grid(row = 3, column = 2)
b9 = Button(TTT, bg = "red", height = 2, width = 4, text = "9")
b9.bind("<Button-1>", Loser)
b9.grid(row = 3, column = 3)


TTT.wm_title("Tic Tac Toe")
TTT.mainloop()
