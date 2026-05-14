import os
import tkinter as tk
from gui import *
from rock_paper_scissors import *
from arcade_games import block_break, match_cards
def arcade(parent, rps_beaten, block_break_beaten, matching_beaten):
    images_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Images"))
    while True:
        arcade_window = tk.Toplevel(parent)
        arcade_window.geometry("1200x1100")
        arcade_window.resizable(False,False)
        arcade_window.title('Arcade')
        arcade_window.transient(parent)
        arcade_window.grab_set()

        arcade_game_image = tk.PhotoImage(master=arcade_window, file=os.path.join(images_dir, "arcade_game.png"))
        arcade_game = tk.Label(arcade_window,image=arcade_game_image)
        arcade_game.pack()
        
        title = tk.Label(arcade_window,text="Choose a Game",font=('Helvetica',32),background="#FFFFFF")
        title.pack()
        title.place(relx=0.5,rely=0.2,anchor=tk.CENTER)
        result = Result()

        rps_img = tk.PhotoImage(master=arcade_window, file=os.path.join(images_dir, "rock.png"))
        rps = image_button(arcade_window,"rock paper scissors",rps_img,result)
        rps.pack()
        rps.place(relx=0.25,rely=0.455,anchor=tk.CENTER)

        block_breaker_img = tk.PhotoImage(master=arcade_window, file=os.path.join(images_dir, "block_break.png"))
        block_breaker = image_button(arcade_window,'block breaker',block_breaker_img,result)
        block_breaker.pack()
        block_breaker.place(relx=0.5,rely=0.455,anchor=tk.CENTER)

        matching_img = tk.PhotoImage(master=arcade_window, file=os.path.join(images_dir, "matching_card.png"))
        matching = image_button(arcade_window,'matching',matching_img,result)
        matching.pack()
        matching.place(relx=0.75,rely=0.455,anchor=tk.CENTER)

        exit_img = tk.PhotoImage(master=arcade_window, file=os.path.join(images_dir, "exit.png"))
        exit_button = tk.Button(arcade_window, image=exit_img, command=lambda: (setattr(result, 'result', 'exit'), arcade_window.destroy()))
        exit_button.pack()
        exit_button.place(relx=0.5,rely=0.705,anchor=tk.CENTER)

        ticket_img = tk.PhotoImage(master=arcade_window, file=os.path.join(images_dir, "ticket.png"))
        rps_ticket = tk.Label(arcade_window,image=ticket_img,background="#ed1c24")
        block_break_ticket = tk.Label(arcade_window,image=ticket_img,background="#ed1c24")
        matching_ticket = tk.Label(arcade_window,image=ticket_img,background="#ed1c24")
        if rps_beaten:
            rps_ticket.pack()
            rps_ticket.place(relx=0.7,rely=0.95,anchor=tk.CENTER)
        if block_break_beaten:
            block_break_ticket.pack()
            block_break_ticket.place(relx=0.8,rely=0.95,anchor=tk.CENTER)
        if matching_beaten:
            matching_ticket.pack()
            matching_ticket.place(relx=0.9,rely=0.95,anchor=tk.CENTER)

        arcade_window.wait_window()
        if not result.result:
            return rps_beaten, block_break_beaten, matching_beaten

        match result.result:
            case 'rock paper scissors':
                if rock_paper_scissors(parent):
                    rps_beaten = True
            case 'block breaker':
                gui(['BLOCK BREAK','As soon as the game starts, click on the screen','Then, use the arrow keys to move the paddle','Try to break all the blocks.','[Got it!'])
                game_root = tk.Toplevel(parent)
                if block_break(game_root):
                    block_break_beaten = True
            case 'matching':
                game_root = tk.Toplevel(parent)
                if match_cards(game_root):
                    matching_beaten = True
            case 'exit':
                return rps_beaten, block_break_beaten, matching_beaten