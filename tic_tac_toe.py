from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)


clicked = True
count = 0
play_again = ""

def disable_all_buttons():
    global play_again
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    play_again = Button(root, text="Play Again", command=reset)
    play_again.grid(row=3, column=1)

def checkifwon():
    winner = False
    if b1['text'] == "X" and b2['text'] == "X" and b3['text'] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! X Won!")
        disable_all_buttons()

    elif b1['text'] == "X" and b4['text'] == "X" and b7['text'] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! X Won!")
        disable_all_buttons()

    elif b4['text'] == "X" and b5['text'] == "X" and b6['text'] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! X Won!")
        disable_all_buttons()

    elif b7['text'] == "X" and b8['text'] == "X" and b9['text'] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! X Won!")
        disable_all_buttons()

    elif b2['text'] == "X" and b5['text'] == "X" and b8['text'] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! X Won!")
        disable_all_buttons()

    elif b3['text'] == "X" and b6['text'] == "X" and b9['text'] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! X Won!")
        disable_all_buttons()

    elif b1['text'] == "X" and b5['text'] == "X" and b9['text'] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! X Won!")
        disable_all_buttons()

    elif b3['text'] == "X" and b5['text'] == "X" and b7['text'] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! X Won!")
        disable_all_buttons()

    # Check if O's Won

    elif b1['text'] == "O" and b2['text'] == "O" and b3['text'] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! O Won!")
        disable_all_buttons()

    elif b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! O Won!")
        disable_all_buttons()

    elif b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! O Won!")
        disable_all_buttons()

    elif b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! O Won!")
        disable_all_buttons()

    elif b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! O Won!")
        disable_all_buttons()

    elif b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! O Won!")
        disable_all_buttons()

    elif b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! O Won!")
        disable_all_buttons()

    elif b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! O Won!")
        disable_all_buttons()
    
    if count == 9 and winner == False:
        messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!\nNo one Wins!")
        disable_all_buttons()



def b_click(b):
    global count, clicked
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()

    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showwarning("Tic-Tac-Toe", "Hey! This box has already been selected.\nPlease pick another box...")

b1 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b1))
b1.grid(row=0, column=0)
b2 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b2))
b2.grid(row=0, column=1)
b3 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b3))
b3.grid(row=0, column=2)

b4 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b4))
b4.grid(row=1, column=0)
b5 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b5))
b5.grid(row=1, column=1)
b6 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b6))
b6.grid(row=1, column=2)

b7 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b7))
b7.grid(row=2, column=0)
b8 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b8))
b8.grid(row=2, column=1)
b9 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b9))
b9.grid(row=2, column=2)


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global count, clicked
    global play_again
    count = 0
    clicked = True
    b1 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b1))
    b1.grid(row=0, column=0)
    b2 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b2))
    b2.grid(row=0, column=1)
    b3 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b3))
    b3.grid(row=0, column=2)

    b4 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b4))
    b4.grid(row=1, column=0)
    b5 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b5))
    b5.grid(row=1, column=1)
    b6 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b6))
    b6.grid(row=1, column=2)

    b7 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b7))
    b7.grid(row=2, column=0)
    b8 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b8))
    b8.grid(row=2, column=1)
    b9 = Button(root, text=" ", font = ("Helvetica", 40), height=1, width=3, command=lambda:b_click(b9))
    b9.grid(row=2, column=2)

    play_again.grid_forget()
    



root.mainloop()