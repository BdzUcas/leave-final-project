import os
import tkinter as tk
from PIL import Image, ImageTk
from treat_trios import treat_trios
from arcade import arcade as run_arcade

#Beginging scene is game(Elevatorhall,1)
def game(Scene_Value):
    root = tk.Tk()
    root.title("IDK MAN")


    root.configure(background="light blue")
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry(f"{w}x{h}")

    images_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Images"))
    def load_img(filename):
        return ImageTk.PhotoImage(Image.open(os.path.join(images_dir, filename)))

    #Images

    itemframe = load_img("ItemFrame.png.png")
    Selitemframe = load_img("SlectedItemFrame.png.png")
    elevatorhall = load_img("ElevatorHall.png.png")
    main10 = load_img("Mainfloor10.png.png")
    garden = load_img("Floating_Garden.png.png")
    oj = load_img("OJ Carton.png.png")
    dolla2 = load_img("2_Dolla.png.png")
    dolla10 = load_img("10dolla.png.png")
    kidsection = load_img("ActualyJustAGarbageTrashScene.png.png")
    arcade = load_img("Arcaderoom.png.png")
    boost = load_img("BorangeBoost.png.png")
    infodesk = load_img("HelpDesk.png.png")
    candystore = load_img("NewKandyStore.png.png")
    toystore = load_img("Toy store.png.png")
    downarrow = load_img("DownArrow.png.png")
    uparrow = load_img("UpArrow.png.png")
    rightarrow = load_img("RightArrow.png.png")
    leftarrow = load_img("LeftArrow.png.png")
    bobbypin = load_img("Bobbypin.png.png")
    dialoguebox = load_img("Dialog box.png.png")
    dialouginteraction = load_img("Dialog.png.png")
    stairs = load_img("Stairs.png.png")
    candy_arcade = load_img("Candy arcade.png.png")
    toycarsimage = load_img("Box o cars.png.png")
    candyticket = load_img("Candy ticket.png.png")
    candypin = load_img("Kandy_Pin.png.png")
    brokenpin = load_img("BrokenBobbyPin.png.png")
    snobbypin = load_img("Bobbypin.png.png")
    arcadescene = load_img("Arcaderoom.png.png")
    arcade_RPS = load_img("arcade Machination(RPS).png")
    arcade_brick = load_img("arcade Machination(Brick).png")
    arcade_card = load_img("arcade Machination(Card).png")
    food_court = load_img("Food court.png.png")
    Boorage_boost = load_img("BorangeBoost.png.png")
    fish_Station = load_img("FishStore.png.png")



    """




    Testimage1 = Image.open("Images/Test1background.png.png")
    Testimage1 = ImageTk.PhotoImage(Testimage1)

    Testimage2 = Image.open("Images/Test2Background.png.png")
    Testimage2 = ImageTk.PhotoImage(Testimage2)

    oj = Image.open("Images/Test_Item.png.png")
    oj = ImageTk.PhotoImage(oj)
    """
    root.backgroundlabel = tk.Label(root,)
    root.backgroundlabel.place(relx=.5, rely=0.0, anchor="n")

    root.currency = 5
    root.currecytag = tk.Label(root, text=f"Current cash:{root.currency}", font=("Arial", 20), bg="tan")
    root.currecytag.place(relx=.15, rely=0.73, anchor="n")

    #button.pack(pady=40)
    root.passed_Sleceted_item = "Empty"
    root.Temporary_Items = []


    #Diffrent items
    root.Item_Selected = "None"
    root.testItemBool = 0
    root.boobypinbool = False
    root.dollars2bool = False
    root.stairsavailible = False
    root.rps_won = False
    root.breaker_won = False
    root.match_won = False

    #The main part
    #itemframe_btn = tk.Button(root, image=itemframe)
    #itemframe_btn.place(relx=.5, rely=0.90, anchor="n")
    def kill():
        try:
            root.nametag.place_forget()
        except:
            pass
        try:
            root.Dialogue.place_forget()
        except:
            pass
        try:
            root.nextbutton.place_forget()
        except:
            pass
        try:
            root.button1.place_forget()
        except:
            pass
        try:
            root.button2.place_forget()
        except:
            pass
        try:
            root.button3.place_forget()
        except:
            pass
        try:
            root.item.place_forget()
        except:
            pass
    def dialog(Interaction_Num,persontalking,currentscene):
        scene(dialoguebox,0)
        root.nametag = tk.Label(root, text=persontalking, font=("Arial", 70), bg="tan")
        root.nametag.place(relx=.5, rely=0.3, anchor="n")
        try:
            root.Dialogue.place_forget()
        except:
            pass
        try:
            root.nextbutton.place_forget()
        except:
            pass
        try:
            root.button1.place_forget()
        except:
            pass
        try:
            root.button2.place_forget()
        except:
            pass
        try:
            root.button3.place_forget()
        except:
            pass
        if Interaction_Num == 1:
            #Introduction to the candy store owner
            root.Dialogue = tk.Label(root, text="Welcome!", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="Goodbye.", command=lambda: dialog(0,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
            root.button1 = tk.Button(root, text="I need to get down to floor 9…", command=lambda: dialog(2,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
            root.button2 = tk.Button(root, text="Who are you?", command=lambda: dialog(3,persontalking,currentscene))
            root.button2.place(relx=.4, rely=0.65, anchor="n")
            root.button3 = tk.Button(root, text="What are your thoughts on cats?", command=lambda: dialog(4,persontalking,currentscene))
            root.button3.place(relx=.3, rely=0.65, anchor="n")
        if Interaction_Num == 2:
            root.Dialogue = tk.Label(root, text=f"Oh! Well, this store spans floors 9 and 10\nso I can let you use our back stairs\nbut where are your parents? And why can't you go down?", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="None of your business.", command=lambda: dialog(0,persontalking,currentscene))
            root.button1.place(relx=.6, rely=0.65, anchor="n")
            root.button2 = tk.Button(root, text="Don't worry, I just need to get something for my parents. The elevator is broken by the way.", command=lambda: dialog(5,persontalking,currentscene))
            root.button2.place(relx=.4, rely=0.65, anchor="n")
        if Interaction_Num == 3:
            root.Dialogue = tk.Label(root, text="Well, i'm the owner of this store of course!", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="I need to get down to floor 9…", command=lambda: dialog(2,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
            root.nextbutton = tk.Button(root, text="Goodbye.", command=lambda: dialog(0,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
        if Interaction_Num == 4:
            root.Dialogue = tk.Label(root, text="Eh, they're fine.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="I need to get down to floor 9…", command=lambda: dialog(2,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
            root.nextbutton = tk.Button(root, text="Goodbye.", command=lambda: dialog(0,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
        if Interaction_Num == 5:
            tempbool = False
            root.Dialogue = tk.Label(root, text=f"If you say so. Now… I did lose the key…\nso if you have something we can lockpick it with, then i can let you down.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            for x in root.Temporary_Items:
                if x[0] == "Bobbypin":
                        tempbool = True
                if x[0] == "sbobbypinlabel":
                    tempbool = True

            if tempbool == True:
                root.button1 = tk.Button(root, text="I have this bobby pin!", command=lambda: dialog(6,persontalking,currentscene))
                root.button1.place(relx=.3, rely=0.65, anchor="n")
            
            root.button2 = tk.Button(root, text="Let me go look for something.", command=lambda: dialog(0,persontalking,currentscene))
            root.button2.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 6:
            tempbool = False
            tempbool2 = False
            for x in root.Temporary_Items:
                if x[0] == "Bobbypin":
                    tempbool = True
                    itemframe_Deletion("Bobbypin",root.Testitem)
                    root.Temporary_Items.append(["Brokenbooby",brokenpin])
                    Inventoryframes(root.Temporary_Items)
                if x[0] == "sbobbypinlabel":
                    tempbool2 = True
            if tempbool2 == True:        
                root.Dialogue = tk.Label(root, text="Perfect! There we go!", font=("Arial", 40), bg="tan")
                root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
                root.nextbutton = tk.Button(root, text="Goodbye.", command=lambda: dialog(0,persontalking,currentscene))
                root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
                root.stairsavailible = True        
            elif tempbool == True:        
                root.Dialogue = tk.Label(root, text="It seems I broke the bobby pin.\n If only you could get me a diffrent one, it might work.", font=("Arial", 40), bg="tan")
                root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
                root.nextbutton = tk.Button(root, text="Goodbye.", command=lambda: dialog(0,persontalking,currentscene))
                root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
                #root.stairsavailible = True
        if Interaction_Num == 7:
            root.Dialogue = tk.Label(root, text="Hey!", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="Goodbye.", command=lambda: dialog(0,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
            root.button1 = tk.Button(root, text="Are you looking for something?", command=lambda: dialog(9,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
            root.button2 = tk.Button(root, text="What is your name?", command=lambda: dialog(8,persontalking,currentscene))
            root.button2.place(relx=.4, rely=0.65, anchor="n")
        if Interaction_Num == 8:
            persontalking = "James"
            root.Dialogue = tk.Label(root, text="James. What's your name?", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="Dave.", command=lambda: dialog(7,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 9:
            tempbool = False
            root.Dialogue = tk.Label(root, text="I lost my cars…", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            for x in root.Temporary_Items:
                if x[0] == "Toycars":
                    tempbool = True
            if tempbool == False:
                root.nextbutton = tk.Button(root, text="Can't you just get new ones?", command=lambda: dialog(10,persontalking,currentscene))
                root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
            else:
                root.button1 = tk.Button(root, text="I have a toy car set. Want it?", command=lambda: dialog(16,persontalking,currentscene))
                root.button1.place(relx=.5, rely=0.65, anchor="n")
                root.nextbutton = tk.Button(root, text="Can't you just get new ones?", command=lambda: dialog(10,persontalking,currentscene))
                root.nextbutton.place(relx=.6, rely=0.65, anchor="n")
        if Interaction_Num == 10:
            root.Dialogue = tk.Label(root, text="Dad won't let me get any!!", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="Oh. That kinda sucks.", command=lambda: dialog(11,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 11:
            root.Dialogue = tk.Label(root, text="Say, if you find any, will you give them to me?", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="What do I get in return?", command=lambda: dialog(12,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 12:
            root.Dialogue = tk.Label(root, text="Hmm… I'll give you this\n Treat Trios ticket!", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text=" Like… for the arcade on floor 9?", command=lambda: dialog(13,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 13:
            root.Dialogue = tk.Label(root, text="Nah. It's for that video game in the candy store.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="Oh. Well, fine… I'll take it.", command=lambda: dialog(7,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 14:
            root.Dialogue = tk.Label(root, text="Hello, are you ready to make a purchase?\n We have toy cars on sale for only $7", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="Goodbye.", command=lambda: dialog(0,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
            if root.currency >= 7:
                root.button1 = tk.Button(root, text="Sure. I'll take it.", command=lambda: dialog(15,persontalking,currentscene))
                root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 15:
            root.currency -= 7
            root.currecytag.configure(text=f"Current cash:{root.currency}")
            root.Temporary_Items.append(["Toycars",toycarsimage])
            Inventoryframes(root.Temporary_Items)
            dialog(0,persontalking,currentscene)
        if Interaction_Num == 16:
            
            root.Dialogue = tk.Label(root, text="Oh-ho! You really got one for me?", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")

            root.button1 = tk.Button(root, text="Do you want it or not?", command=lambda: dialog(17,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")

        if Interaction_Num == 17:
            kill()
            kill()
            kill()
            kill()
            kill()
            kill()
            kill()
            kill()
            dialog(18,persontalking,currentscene)
        if Interaction_Num == 18:
            root.Dialogue = tk.Label(root, text="Oh, have this in return.\n (He gives you the ticket)", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="Uh, bye…", command=lambda: dialog(19,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 19:
            itemframe_Deletion("Toycars",root.Toycars)
            root.Temporary_Items.append(["CandyTicket",candyticket])
            Inventoryframes(root.Temporary_Items)
            dialog(0,persontalking,currentscene)
        if Interaction_Num == 20:
            root.Dialogue = tk.Label(root, text="What do you want?", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="Goodbye.", command=lambda: dialog(0,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
            root.button1 = tk.Button(root, text="What are you eating?", command=lambda: dialog(22,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
            root.button2 = tk.Button(root, text="What is your name?", command=lambda: dialog(21,persontalking,currentscene))
            root.button2.place(relx=.4, rely=0.65, anchor="n")
        if Interaction_Num == 21:
            persontalking = "Lila"
            root.Dialogue = tk.Label(root, text="Lila. Yours?", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="Dave.", command=lambda: dialog(20,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 22:
            root.Dialogue = tk.Label(root, text="Umm, a lollipop.\n Why?", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="Did you get it from the Candy Store?", command=lambda: dialog(23,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 23:
            root.Dialogue = tk.Label(root, text="Yeah\n You know what?\nI kind of wanted to play that game they have in there.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="That crap?? Why that, of all games??", command=lambda: dialog(24,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 24:
            root.Dialogue = tk.Label(root, text="I meant I wanted the pin, but you can only get it from playing the game.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="Uh-huh, okay. Why can't you play the game then?", command=lambda: dialog(25,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 25:
            root.Dialogue = tk.Label(root, text="I don't have a ticket.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")

            tempbool = False
            for x in root.Temporary_Items:
                if x[0] == "CandyPin":
                    tempbool = True
            if tempbool == False:
                root.nextbutton = tk.Button(root, text="I'll see if I can get one for you.", command=lambda: dialog(26,persontalking,currentscene))
                root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
            else:
                root.nextbutton = tk.Button(root, text="I'll see if I can get one for you.", command=lambda: dialog(26,persontalking,currentscene))
                root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
                root.button1 = tk.Button(root, text="I have the pin you wanted.", command=lambda: dialog(29,persontalking,currentscene))
                root.button1.place(relx=.3, rely=0.65, anchor="n")
        if Interaction_Num == 26:
            root.Dialogue = tk.Label(root, text="Can't you just play it for me?", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="What am I, your personal servant?", command=lambda: dialog(27,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 27:
            root.Dialogue = tk.Label(root, text="I'll give you this if you do!\n (She points to her bobby pin.)", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="What am I going to do with it?", command=lambda: dialog(28,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 28:
            root.Dialogue = tk.Label(root, text="Maybe pick a lock? \n I heard you can do it with a bobby pin.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="Okay, fine.", command=lambda: dialog(0,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 29:
            root.Dialogue = tk.Label(root, text="Oh, you really did get it…\nThank you!\nWell, fine… I'll give you my bobby pin, then.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            
            root.nextbutton = tk.Button(root, text="Okay, fine.", command=lambda: dialog(30,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 30:
            try:
                itemframe_Deletion("Bobbypin",root.Testitem)
            except:
                pass
            itemframe_Deletion("CandyPin",root.CandyPin)
            root.Temporary_Items.append(["sbobbypinlabel",snobbypin])
            print(root.Temporary_Items)
            Inventoryframes(root.Temporary_Items)
            dialog(0,persontalking,currentscene)

        if Interaction_Num == 31:
            root.Dialogue = tk.Label(root, text="Um… hello there.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="Goodbye", command=lambda: dialog(0,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
            root.button1 = tk.Button(root, text="Are you waiting for something?", command=lambda: dialog(32,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 32:
            root.Dialogue = tk.Label(root, text="I have to go get my food from Fresh Filet \n but I don’t feel like it.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="I can help.", command=lambda: dialog(34,persontalking,currentscene))
            root.nextbutton.place(relx=.65, rely=0.65, anchor="n")
            root.button1 = tk.Button(root, text="“just get it its not that hard", command=lambda: dialog(33,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 33:
            root.Dialogue = tk.Label(root, text="It kinda is…", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="Fine. I’ll do it for you, lazy. What do I get in return?", command=lambda: dialog(34,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 34:
            root.Dialogue = tk.Label(root, text="I will give you $10…and maybe anything else you need?", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="Well, I do need to get down to floor 1.", command=lambda: dialog(35,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 35:
            root.Dialogue = tk.Label(root, text="Oh…well I can tell you where the elevators are…but you have to help me first…!", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="Alright alright. What’s your order number?", command=lambda: dialog(36,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 36:
            root.Dialogue = tk.Label(root, text="Um, it’s Order 166.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="Leave", command=lambda: dialog(0,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 0:
            scene(currentscene[0],currentscene[1])
    def itemframe_Deletion(Item_type,Item_Name=None):
        for x in list(root.Temporary_Items):
            if x[0] == Item_type:
                root.Temporary_Items.remove(x)
                if Item_Name is not None:
                    try:
                        Item_Name.place_forget()
                    except Exception:
                        pass
                break

    def item_selection(item_Type,Item_Name):
        #if item_Type == "None":
            #root.Item_Selected = item_Type
            #Item_Name.configure(image=Selitemframe)
        #else:
            #root.empty.configure(image=itemframe)
        if root.passed_Sleceted_item == item_Type:
            if item_Type == "Test":
                Item_Name.configure(image=oj)
            item_Type = "None"

        elif item_Type == "Test":
            root.Item_Selected = item_Type
            Item_Name.configure(image=Selitemframe)
            #itemframe_Deletion("Test",root.Testitem)
        root.passed_Sleceted_item = item_Type

    def Inventoryframes(Inventory):
        for widget in getattr(root, "inventory_widgets", []):
            try:
                widget.place_forget()
                widget.destroy()
            except Exception:
                pass
        root.inventory_widgets = []
        root.InventoryCount = 0
        for x in Inventory:
            root.InventoryCount += 0.1
            if x[0] == "Bobbypin":
                button = tk.Button(root, image=x[1], command=lambda item_type=x[0], btn=button: item_selection(item_type, btn))
                button.place(relx=root.InventoryCount, rely=0.8, anchor="n")
                root.Testitem = button
                root.inventory_widgets.append(button)
            if x[0] == "sbobbypinlabel":
                button = tk.Button(root, image=x[1], command=lambda item_type=x[0], btn=button: item_selection(item_type, btn))
                button.place(relx=root.InventoryCount, rely=0.8, anchor="n")
                root.sbobbypinlabel = button
                root.inventory_widgets.append(button)
            if x[0] == "Brokenbooby":
                button = tk.Button(root, image=x[1], command=lambda item_type=x[0], btn=button: item_selection(item_type, btn))
                button.place(relx=root.InventoryCount, rely=0.8, anchor="n")
                root.Testitem = button
                root.inventory_widgets.append(button)
            if x[0] == "Toycars":
                button = tk.Button(root, image=x[1], command=lambda item_type=x[0], btn=button: item_selection(item_type, btn))
                button.place(relx=root.InventoryCount, rely=0.8, anchor="n")
                root.Toycars = button
                root.inventory_widgets.append(button)
            if x[0] == "CandyTicket":
                button = tk.Button(root, image=x[1], command=lambda item_type=x[0], btn=button: item_selection(item_type, btn))
                button.place(relx=root.InventoryCount, rely=0.8, anchor="n")
                root.CandyTicket = button
                root.inventory_widgets.append(button)
            if x[0] == "CandyPin":
                button = tk.Button(root, image=x[1], command=lambda item_type=x[0], btn=button: item_selection(item_type, btn))
                button.place(relx=root.InventoryCount, rely=0.8, anchor="n")
                root.CandyPin = button
                root.inventory_widgets.append(button)
    def item(ItemName):
        if ItemName == "Bobbypin":
            root.boobypinbool = True
            root.item.place_forget()
            #Hey I Do Not know what we are really doing for the item logic so just replace this with the function for item storage
            root.Temporary_Items.append(["Bobbypin",bobbypin])
            Inventoryframes(root.Temporary_Items)
        if ItemName == "RPS":
            root.rps_won,root.breaker_won,root.match_won = run_arcade(root.rps_won,root.breaker_won,root.match_won)
        if ItemName == "Brick":
            root.rps_won,root.breaker_won,root.match_won = run_arcade(root.rps_won,root.breaker_won,root.match_won)
        if ItemName == "Match":
            root.rps_won,root.breaker_won,root.match_won = run_arcade(root.rps_won,root.breaker_won,root.match_won)
        if ItemName == "2dollars":
            root.dollars2bool = True
            root.item.place_forget()
            #Hey I Do Not know what we are really doing for the item logic so just replace this with the function for item storage
            root.currency += 2
            root.currecytag.configure(text=f"Current cash:{root.currency}")
            Inventoryframes(root.Temporary_Items)
        if ItemName == "candystoredialogue":
            dialog(1,"CandyStore Owner",[candystore,5])
        if ItemName == "toystoredialogue":
            dialog(14,"toy store worker",[toystore,7])
        if ItemName == "candy_arcade":
            for x in root.Temporary_Items:
                if x[0] == "CandyTicket":
                    root.item.place_forget()
                    try:
                        treat_trios()

                        itemframe_Deletion("CandyTicket",root.CandyTicket)
                        root.Temporary_Items.append(["CandyPin",candypin])
                    except:
                        itemframe_Deletion("CandyTicket",root.CandyTicket)
                        root.Temporary_Items.append(["CandyPin",candypin])
                    itemframe_Deletion("CandyTicket",root.CandyTicket)
                    root.item = tk.Button(root, image=candy_arcade, command=lambda: item("candy_arcade"))
                    root.item.place(relx=.75, rely=0.2,anchor="n")
                    Inventoryframes(root.Temporary_Items)
        if ItemName == "Kid1Dialogue":
            dialog(7,"Kid 1",[kidsection,4])
        if ItemName == "Kid2Dialogue":
            dialog(20,"Kid 2",[kidsection,4])
        if ItemName == "Shydudetalk":
            dialog(31,"Shy guy",[food_court,10])


    def SceneButtons(SceneData):
        try:
            root.FrsButton.place_forget()
        except:
                pass
        try:
            root.secButton.place_forget()
        except:
                pass
        try:
            root.thirdButton.place_forget()
        except:
                pass
        try:
            root.fourthbutton.place_forget()
        except:
                pass
        try:
            root.fithbutton.place_forget()
        except:
                pass
        if SceneData == 1:
            root.FrsButton = tk.Button(root, image=uparrow, command=lambda:scene(main10,2))
            root.FrsButton.place(relx=.61, rely=0.5,anchor="n")
        if SceneData == 2:
            root.FrsButton = tk.Button(root, image=downarrow, command=lambda:scene(elevatorhall,1))
            root.FrsButton.place(relx=.5, rely=0.65,anchor="n")

            root.secButton = tk.Button(root, image=rightarrow, command=lambda:scene(garden,3))
            root.secButton.place(relx=.95, rely=0.5,anchor="n")

            root.thirdButton = tk.Button(root, image=leftarrow, command=lambda:scene(kidsection,4))
            root.thirdButton.place(relx=.05, rely=0.5,anchor="n")

            root.fourthbutton = tk.Button(root, image=uparrow, command=lambda:scene(candystore,5))
            root.fourthbutton.place(relx=.7, rely=0.45,anchor="n")

            root.fithbutton = tk.Button(root, image=uparrow, command=lambda:scene(infodesk,6))
            root.fithbutton.place(relx=.25, rely=0.45,anchor="n")
        if SceneData == 3:
            root.secButton = tk.Button(root, image=leftarrow, command=lambda:scene(main10,2))
            root.secButton.place(relx=.05, rely=0.5,anchor="n")
        if SceneData == 4:
            root.secButton = tk.Button(root, image=rightarrow, command=lambda:scene(main10,2))
            root.secButton.place(relx=.95, rely=0.5,anchor="n")

            root.fourthbutton = tk.Button(root, image=uparrow, command=lambda:scene(toystore,7))
            root.fourthbutton.place(relx=.8, rely=0.45,anchor="n")


        if SceneData == 5:
            root.FrsButton = tk.Button(root, image=downarrow, command=lambda:scene(main10,2))
            root.FrsButton.place(relx=.5, rely=0.65,anchor="n")
            if root.stairsavailible == True:
                root.secButton = tk.Button(root, image=uparrow, command=lambda:scene(stairs,8))
                root.secButton.place(relx=.4, rely=0.2,anchor="n")
        if SceneData == 6:
            root.FrsButton = tk.Button(root, image=downarrow, command=lambda:scene(main10,2))
            root.FrsButton.place(relx=.5, rely=0.65,anchor="n")
        if SceneData == 7:
            root.fourthbutton = tk.Button(root, image=uparrow, command=lambda:scene(kidsection,4))
            root.fourthbutton.place(relx=.8, rely=0.45,anchor="n")
        if SceneData == 8:
            root.FrsButton = tk.Button(root, image=downarrow, command=lambda:scene(candystore,5))
            root.FrsButton.place(relx=.5, rely=0.65,anchor="n")
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(stairs,9))
            root.secButton.place(relx=.7, rely=0.4,anchor="n")
        if SceneData == 9:
            root.fourthbutton = tk.Button(root, image=uparrow, command=lambda:scene(stairs,8))
            root.fourthbutton.place(relx=.8, rely=0.45,anchor="n")
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(food_court,10))
            root.secButton.place(relx=.5, rely=0.65,anchor="n")
        if SceneData == 10:
            root.fourthbutton = tk.Button(root, image=uparrow, command=lambda:scene(fish_Station,11))
            root.fourthbutton.place(relx=.45, rely=0.2,anchor="n")
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(stairs,9))
            root.secButton.place(relx=.5, rely=0.65,anchor="n")
            root.FrsButton = tk.Button(root, image=uparrow, command=lambda:scene(Boorage_boost,12))
            root.FrsButton.place(relx=.2, rely=0.45,anchor="n")
        if SceneData == 11:
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(food_court,10))
            root.secButton.place(relx=.5, rely=0.65,anchor="n")
        if SceneData == 12:
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(food_court,10))
            root.secButton.place(relx=.5, rely=0.65,anchor="n")
        if SceneData == 15:
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(stairs,9))
            root.secButton.place(relx=.5, rely=0.65,anchor="n")

           
            #root.frsButton.place(relx=.02, rely=0.5,anchor="n")
    def SceneItems(SceneData):

        try:
            root.item.place_forget()
        except:
            pass
        try:
            root.Dailog.place_forget()
        except:
            pass
        
        if SceneData == 1:
            if root.boobypinbool == False:
                root.item = tk.Button(root, image=bobbypin, command=lambda: item("Bobbypin"))
                root.item.place(relx=.5, rely=0.1,anchor="n")
        if SceneData == 3:
            if root.dollars2bool == False:
                root.item = tk.Button(root, image=dolla2, command=lambda: item("2dollars"))
                root.item.place(relx=.8, rely=0.55,anchor="n")
        if SceneData == 5:
            root.Dailog = tk.Button(root, image=dialouginteraction, command=lambda: item("candystoredialogue"))
            root.Dailog.place(relx=.25, rely=0.1,anchor="n")
            root.item = tk.Button(root, image=candy_arcade, command=lambda: item("candy_arcade"))
            root.item.place(relx=.75, rely=0.2,anchor="n")
        if SceneData == 4:
            root.Dailog = tk.Button(root, image=dialouginteraction, command=lambda: item("Kid1Dialogue"))
            root.Dailog.place(relx=.31, rely=0.25,anchor="n")
            root.item = tk.Button(root, image=dialouginteraction, command=lambda: item("Kid2Dialogue"))
            root.item.place(relx=.43, rely=0.25,anchor="n")
        if SceneData == 7:
            root.Dailog = tk.Button(root, image=dialouginteraction, command=lambda: item("toystoredialogue"))
            root.Dailog.place(relx=.25, rely=0.1,anchor="n")
        if SceneData == 10:
            root.Dailog = tk.Button(root, image=dialouginteraction, command=lambda: item("Shydudetalk"))
            root.Dailog.place(relx=.93, rely=0.1,anchor="n")
        if SceneData == 15:
            root.item = tk.Button(root, image=arcade_RPS, command=lambda: item("RPS"))
            root.item.place(relx=.43, rely=0.25,anchor="n")
            root.item2 = tk.Button(root, image=arcade_brick, command=lambda: item("Brick"))
            root.item2.place(relx=.53, rely=0.25,anchor="n")
            root.item3 = tk.Button(root, image=arcade_card, command=lambda: item("Match"))
            root.item3.place(relx=.63, rely=0.25,anchor="n")
        
            
    def scene(background,SceneData):
        
        kill()
        root.backgroundlabel.configure(image=background)
        SceneButtons(SceneData)
        SceneItems(SceneData)


    #Test scene Data
    if Scene_Value == 1:
        scene(elevatorhall,Scene_Value)
    elif Scene_Value == 2:
        scene(main10,Scene_Value)
    elif Scene_Value == 3:
        scene(garden,Scene_Value)
    elif Scene_Value == 4:
        scene(kidsection,Scene_Value)
    elif Scene_Value == 5:
        scene(candystore,Scene_Value)
    elif Scene_Value == 6:
        scene(infodesk,Scene_Value)
    elif Scene_Value == 7:
        scene(toystore,Scene_Value)
    elif Scene_Value == 8:
        scene(stairs,Scene_Value)
    elif Scene_Value == 9:
        scene(stairs,Scene_Value)
    elif Scene_Value == 12:
        scene(arcadescene,Scene_Value)
    root.mainloop()



if __name__ == "__main__":
    game(1)
