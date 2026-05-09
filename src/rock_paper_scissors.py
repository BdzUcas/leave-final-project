#BZ 1st Rock Paper Scissors
import random as r
from gui import Result
from gui import gui
import tkinter as tk

def button_push(root: tk.Tk, return_val: str, result: Result):
    result.result = return_val
    root.destroy()

def image_button(root: tk.Tk, return_val: str, image: tk.PhotoImage, result: Result):
    button = tk.Button(root,image=image,command=lambda return_val=return_val: button_push(root,return_val,result))
    return button

def choice_gui():
    choice_gui = tk.Tk()
    choice_gui.geometry("1000x800")
    choice_gui.resizable(True,True)
    choice_gui.title('Rock Paper Scissors')
    title = tk.Label(choice_gui,text="Choose Your Weapon",font=("Helvetica",32))
    title.pack(pady=30)
    result = Result()

    rock_img = tk.PhotoImage(file="Images/rock.png")
    rock = image_button(choice_gui,"rock",rock_img,result)
    rock.pack()
    rock.place(relx=0.25,rely=0.5,anchor=tk.CENTER)

    paper_img = tk.PhotoImage(file="Images/paper.png")
    paper = image_button(choice_gui,'paper',paper_img,result)
    paper.pack()
    paper.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

    scissors_img = tk.PhotoImage(file="Images/scissors.png")
    scissors = image_button(choice_gui,'scissors',scissors_img,result)
    scissors.pack()
    scissors.place(relx=0.75,rely=0.5,anchor=tk.CENTER)

    choice_gui.mainloop()
    return result.result

def win_gui(choice: int, computer_choice: int, win_message: str, winner = False, bot_winner = False):
    if winner:
        win_message = win_message + '\nYou win!'
    if bot_winner:
        win_message = win_message + '\nThey win!'

    win_gui = tk.Tk()
    win_gui.geometry("1000x800")
    win_gui.resizable(True,True)
    win_gui.title('Rock Paper Scissors')
    title = tk.Label(win_gui,text="RESULTS",font=("Helvetica",32))
    title.pack(pady=30)

    rock = tk.PhotoImage(file="Images/rock.png")
    paper = tk.PhotoImage(file="Images/paper.png")
    scissors = tk.PhotoImage(file="Images/scissors.png")
    photo_map = {1:rock,2:paper,3:scissors}

    player_weapon = tk.Label(win_gui,image=photo_map[choice])
    player_weapon.pack()
    player_weapon.place(relx=0.25,rely=0.4,anchor=tk.CENTER)

    computer_weapon = tk.Label(win_gui,image=photo_map[computer_choice])
    computer_weapon.pack()
    computer_weapon.place(relx=0.75,rely=0.4,anchor=tk.CENTER)

    vs_image = tk.PhotoImage(file='Images/vs.png')
    vs = tk.Label(win_gui,image=vs_image)
    vs.pack()
    vs.place(relx=0.5,rely=0.4,anchor=tk.CENTER)

    win = tk.Label(win_gui,text=win_message,font=('Helvetica',28))
    win.pack()
    win.place(relx=0.5,rely=0.55,anchor=tk.CENTER)

    next_img = tk.PhotoImage(file="Images/continue.png")
    next = image_button(win_gui,'next',next_img,Result())
    next.pack()
    next.place(relx=0.5,rely=0.75,anchor=tk.CENTER)

    win_gui.mainloop()

def rock_paper_scissors():
    choices = ['There was an error!','rock','paper','scissors']
    choice_map = {'rock':1,'paper':2,'scissors':3}
    actions = ['There was an error!',' smashed ',' smothered ',' snipped ']
    score = 0
    bot_score = 0

    gui(['### ROCK PAPER SCISSORS ###','\n\n\n\n\n\n','Choose Rock, Paper, or Scissors each round to beat your opponent!','First to win 3 rounds wins!','\n\n','[LETS DO THIS!'],fontsize=15,width=1000,height=800)
    while True:
        try:
            choice = choice_map[choice_gui()]
        except:
            continue

        computer_choice = r.randint(1,3)


        if choice - 1 == computer_choice:
            win_message = f'Your {choices[choice]}{actions[choice]}their {choices[computer_choice]}!'
            score += 1
        elif computer_choice - 1 == choice:
            win_message = f'Their {choices[computer_choice]}{actions[computer_choice]}your {choices[choice]}!'
            bot_score += 1
        elif computer_choice == 1 and choice == 3:
            win_message = f'Their {choices[computer_choice]}{actions[computer_choice]}your {choices[choice]}!'
            bot_score += 1
        elif choice == 1 and computer_choice == 3:
            win_message = f'Your {choices[choice]}{actions[choice]}their {choices[computer_choice]}!'
            score += 1
        elif choice == computer_choice:
            win_message = 'It\'s a tie!'
        else:
            win_message = 'The game bugged out. What kind of arcade is this?'
        winner = score == 3
        bot_winner = bot_score == 3
        win_gui(choice, computer_choice, win_message, winner, bot_winner)
        if winner:
            return True
        elif bot_winner:
            return False
        
rock_paper_scissors()