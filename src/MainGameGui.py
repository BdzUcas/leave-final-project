import tkinter as tk
from PIL import Image, ImageTk
from treat_trios import treat_trios
from arcade import arcade as run_arcade
from data import undictify, dictify

#This is a list of all the attributes of root that should be saved. For example: 'dollars2bool'
export_fields = ['currency','Temporary_Items','Item_Selected','testItemBool','boobypinbool','dollars2bool','stairsavailible','orderrecipt','orderdone','CanFloor9','canel','rps_won','breaker_won','match_won','passed_Sleceted_item','arcade_death','scenenumber']
item_images = {'Brokenbooby':'Images/BrokenBobbyPin.png.png','Toycars':'Images/Box o cars.png.png','CandyTicket':'Images/Candy ticket.png.png','sbobbypinlabel':'Images/Bobbypin.png.png','Bobbypin':'Images/Bobbypin.png.png','candypin':'Kandy_Pin.png.png','bunny':'Images/Rabbit_Plush.png.png','Fish_order':'Images/Fish_Order.png.png'}

#Beginging scene is game(Elevatorhall,1)
def game(Scene_Value,data={}):

    
    if not data:
        root = root_setup()
    elif data == {'arcade_death': False}:
        root = root_setup()
    else:
        root = undictify([data])[0]
    root.title("Game")
    root.configure(background="light blue")
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry(f"{w}x{h}")

    #root.scenenumber = int(Scene_Value)
    #Images

    itemframe = Image.open("Images/ItemFrame.png.png")
    itemframe = ImageTk.PhotoImage(itemframe)

    Selitemframe = Image.open("Images/SlectedItemFrame.png.png")
    Selitemframe = ImageTk.PhotoImage(Selitemframe)

    elevatorhall = Image.open("Images/ElevatorHallOutOfOrder.png")
    elevatorhallfixed = Image.open("Images/ElevatorHall.png.png")
    #it is a root property so it can be changed inside a function (when the elevators are fixed)
    if root.canel:
        root.elevatorhall = ImageTk.PhotoImage(elevatorhallfixed)
    else:
        root.elevatorhall = ImageTk.PhotoImage(elevatorhall)

    

    testscene= Image.open("Images/Test1background.png.png")
    testscene = ImageTk.PhotoImage(testscene)

    main10 = Image.open("Images/Mainfloor10.png.png")
    main10 = ImageTk.PhotoImage(main10)

    garden = Image.open("Images/Floating_Garden.png.png")
    garden = ImageTk.PhotoImage(garden)

    oj = Image.open("Images/OJ Carton.png.png")
    oj = ImageTk.PhotoImage(oj)

    dolla2 = Image.open("Images/2_Dolla.png.png")
    dolla2 = ImageTk.PhotoImage(dolla2)

    dolla10 = Image.open("Images/10dolla.png.png")
    dolla10 = ImageTk.PhotoImage(dolla10)

    kidsection = Image.open("Images/ActualyJustAGarbageTrashScene.png.png")
    kidsection = ImageTk.PhotoImage(kidsection)

    arcade = Image.open("Images/Arcaderoom.png.png")
    arcade = ImageTk.PhotoImage(arcade)

    boost = Image.open("Images/BorangeBoost.png.png")
    boost = ImageTk.PhotoImage(boost)

    infodesk = Image.open("Images/HelpDesk.png.png")
    infodesk = ImageTk.PhotoImage(infodesk)

    candystore = Image.open("Images/NewKandyStore.png.png")
    candystore = ImageTk.PhotoImage(candystore)

    toystore = Image.open("Images/Toy store.png.png")
    toystore = ImageTk.PhotoImage(toystore)

    downarrow = Image.open("Images/DownArrow.png.png")
    downarrow = ImageTk.PhotoImage(downarrow)

    uparrow = Image.open("Images/UpArrow.png.png")
    uparrow = ImageTk.PhotoImage(uparrow)

    rightarrow = Image.open("Images/RightArrow.png.png")
    rightarrow = ImageTk.PhotoImage(rightarrow)

    leftarrow = Image.open("Images/LeftArrow.png.png")
    leftarrow = ImageTk.PhotoImage(leftarrow)

    bobbypin = Image.open("Images/Bobbypin.png.png")
    bobbypin = ImageTk.PhotoImage(bobbypin)

    dialoguebox = Image.open("Images/Dialog box.png.png")
    dialoguebox = ImageTk.PhotoImage(dialoguebox)

    dialouginteraction = Image.open("Images/Dialog.png.png")
    dialouginteraction = ImageTk.PhotoImage(dialouginteraction)

    stairs10 = Image.open("Images/Stairs_floor10.png")
    stairs10 = ImageTk.PhotoImage(stairs10)

    stairs9 = Image.open("Images/Stairs_floor9.png")
    stairs9 = ImageTk.PhotoImage(stairs9)

    candy_arcade = Image.open("Images/Candy arcade.png.png")
    candy_arcade = ImageTk.PhotoImage(candy_arcade)

    toycarsimage = Image.open("Images/Box o cars.png.png")
    toycarsimage = ImageTk.PhotoImage(toycarsimage)

    candyticket = Image.open("Images/Candy ticket.png.png")
    candyticket = ImageTk.PhotoImage(candyticket)

    candypin = Image.open("Images/Kandy_Pin.png.png")
    candypin = ImageTk.PhotoImage(candypin)

    brokenpin = Image.open("Images/BrokenBobbyPin.png.png")
    brokenpin = ImageTk.PhotoImage(brokenpin)

    snobbypin = Image.open("Images/Bobbypin.png.png")
    snobbypin = ImageTk.PhotoImage(snobbypin)

    arcadescene = Image.open("Images/Arcaderoom.png.png")
    arcadescene = ImageTk.PhotoImage(arcadescene)

    arcade_RPS =  Image.open("Images/arcade Machination(RPS).png")
    arcade_RPS = ImageTk.PhotoImage(arcade_RPS)

    arcade_brick =  Image.open("Images/arcade Machination(Brick).png")
    arcade_brick = ImageTk.PhotoImage(arcade_brick)

    arcade_card =  Image.open("Images/arcade Machination(Card).png")
    arcade_card = ImageTk.PhotoImage(arcade_card)

    food_court = Image.open("Images/Food court.png.png")
    food_court = ImageTk.PhotoImage(food_court)

    Boorage_boost = Image.open("Images/BorangeBoost.png.png")
    Boorage_boost = ImageTk.PhotoImage(Boorage_boost)

    fish_Station = Image.open("Images/FishStore.png.png")
    fish_Station = ImageTk.PhotoImage(fish_Station)

    floor9 = Image.open("Images/main area of arcade floor.png")
    floor9canel = Image.open("Images/floor9_no_security.png")
    if root.canel:
        root.floor9 = ImageTk.PhotoImage(floor9canel)
    else:
        root.floor9 = ImageTk.PhotoImage(floor9)

    bunnyplush = Image.open("Images/Rabbit_Plush.png.png")
    bunnyplush = ImageTk.PhotoImage(bunnyplush)

    exitdoor = Image.open("Images/Exitdoors.png.png")
    exitdoor = ImageTk.PhotoImage(exitdoor)

    arcadestaff = Image.open("Images/arcade staff.png")
    arcadestaff = ImageTk.PhotoImage(arcadestaff)

    fishorder = Image.open("Images/Fish_Order.png.png")
    fishorder = ImageTk.PhotoImage(fishorder)



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

    
    root.currecytag = tk.Label(root, text=f"Current cash:{root.currency}", font=("Arial", 20), bg="tan")
    root.currecytag.place(relx=.15, rely=0.73, anchor="n")

    #button.pack(pady=40)
    root.passed_Sleceted_item = "Empty"
    


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
    def goto_candystore_from_stairs():
        root.entered_candy_from_stairs = True
        scene(candystore,5)

    def exit_candy_store():
        if root.entered_candy_from_stairs:
            root.entered_candy_from_stairs = False
            scene(food_court,10)
        else:
            scene(main10,2)

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
                itemframe_Deletion("sbobbypinlabel",root.sbobbypinlabel)
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
            root.Temporary_Items.append(["sbobbypinlabel",bobbypin])
            Inventoryframes(root.Temporary_Items)
            dialog(0,persontalking,currentscene)

        if Interaction_Num == 31:
            if root.orderdone == False:
                root.Dialogue = tk.Label(root, text="Um…hello there.", font=("Arial", 40), bg="tan")
                root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
                root.nextbutton = tk.Button(root, text="Goodbye.", command=lambda: dialog(0,persontalking,currentscene))
                root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
                root.button1 = tk.Button(root, text="Are you waiting for someone?", command=lambda: dialog(32,persontalking,currentscene))
                root.button1.place(relx=.5, rely=0.65, anchor="n")
            else:
                root.Dialogue = tk.Label(root, text="Oh…thanks.\nHere's the $10 as promised.", font=("Arial", 40), bg="tan")
                root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
                root.currency += 10
                root.elevator_unlocked = True
                root.nextbutton = tk.Button(root, text="You said you would show me the way to the elevators too.", command=lambda: dialog(40,persontalking,currentscene))
                root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
        if Interaction_Num == 32:
            root.Dialogue = tk.Label(root, text="I have to go get my food from Filet-o-Fish, \n but I don't feel like it.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.nextbutton = tk.Button(root, text="I can help.", command=lambda: dialog(34,persontalking,currentscene))
            root.nextbutton.place(relx=.65, rely=0.65, anchor="n")
            root.button1 = tk.Button(root, text="It's not that hard. Just walk over there and ask for your order.", command=lambda: dialog(33,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 33:
            root.Dialogue = tk.Label(root, text="That's kinda hard.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="Fine. I'll do it for you, lazy. What do I get in return?", command=lambda: dialog(34,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 34:
            root.Dialogue = tk.Label(root, text="I will give you $10… and maybe anything else you need?", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="Well, if there is any way you could get me to floor 1 that would be great.", command=lambda: dialog(35,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 35:
            root.Dialogue = tk.Label(root, text="Oh…well I can tell you where the elevators are…but you have to help me first!", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="Alright, alright. What's your order number?", command=lambda: dialog(36,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 36:
            root.Dialogue = tk.Label(root, text="I believe it is 166.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.orderrecipt = True
            root.button1 = tk.Button(root, text="Goodbye.", command=lambda: dialog(0,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 37:
            root.Dialogue = tk.Label(root, text="Hey kid! You got an order number?", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            if root.orderrecipt == False:
                root.button1 = tk.Button(root, text="No sir.", command=lambda: dialog(0,persontalking,currentscene))
                root.button1.place(relx=.5, rely=0.65, anchor="n")
            else:
                root.button1 = tk.Button(root, text="Order 166 please.", command=lambda: dialog(38,persontalking,currentscene))
                root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 38:
            root.Dialogue = tk.Label(root, text="Okay, here you go.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="Thank you.", command=lambda: dialog(39,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 39:
            root.orderdone = True
            dialog(0,persontalking,currentscene)
            root.Temporary_Items.append(["Fish_order",fishorder])
            Inventoryframes(root.Temporary_Items)

        if Interaction_Num == 40:
            root.Dialogue = tk.Label(root, text="Right…ok. Go to the right and face the info desk.\n The elevator should be on the right.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="Thank you.", command=lambda: dialog(41,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 41:
            root.currency += 10
            itemframe_Deletion("fish_order",root.fish)
            root.CanFloor9 = True
            dialog(0,persontalking,currentscene)
        if Interaction_Num == 42:
            root.Dialogue = tk.Label(root, text="Oh, hello again.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
            root.button1 = tk.Button(root, text="Why are you down here?", command=lambda: dialog(43,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 43:
            root.Dialogue = tk.Label(root, text=f"This girl got lost. She got separated from her parents\n and she doesn't have any contact information on them.\n We've sent out several announcements but no one has come.\n How did you get down here?”", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            root.button1 = tk.Button(root, text=" Are the elevators working now?", command=lambda: dialog(44,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 44:
            root.Dialogue = tk.Label(root, text=f"Nope. I'm the one supposed to be supervising it for some reason,\nbut I have to watch over her so we can't start fixing it.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            root.button1 = tk.Button(root, text="Why are you the one supervising it?", command=lambda: dialog(45,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 45:
            root.Dialogue = tk.Label(root, text=f"I have no idea.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            root.button1 = tk.Button(root, text="Alright. Bye!", command=lambda: dialog(0,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 46:
            root.Dialogue = tk.Label(root, text=f"I have no idea.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            root.button1 = tk.Button(root, text="Alright. Bye!", command=lambda: dialog(0,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 47:
            root.Dialogue = tk.Label(root, text=f".......", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            root.button1 = tk.Button(root, text="Are you looking for something?", command=lambda: dialog(48,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 48:
            root.Dialogue = tk.Label(root, text=f"...I lost my plush bunny…", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            root.button1 = tk.Button(root, text="oh", command=lambda: dialog(49,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 49:
            tempbool = False
            root.Dialogue = tk.Label(root, text=f"We did see a similar one in the arcade…\nbut mister officer wants us to stay here…", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            for x in root.Temporary_Items:
                if x[0] == "bunny":
                    tempbool = True
            if tempbool == True:
                root.nextbutton = tk.Button(root, text="Give rabbit plush", command=lambda: dialog(54,persontalking,currentscene))
                root.nextbutton.place(relx=.65, rely=0.65, anchor="n")
            root.button1 = tk.Button(root, text="I don't know, I guess I could grab it for you.", command=lambda: dialog(50,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 50:
            root.Dialogue = tk.Label(root, text=f"You can??", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            root.button1 = tk.Button(root, text="Yea sure since my whole time here has been sidequest simulator", command=lambda: dialog(0,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 51:
            root.Dialogue = tk.Label(root, text=f"Welcome to the arcade! how may I help you?", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            if root.rps_won == True and root.breaker_won == True and root.match_won == True:
                root.button1 = tk.Button(root, text="Can I have that bunny plush?", command=lambda: dialog(52,persontalking,currentscene))
                root.button1.place(relx=.5, rely=0.65, anchor="n")
            else:
                root.button1 = tk.Button(root, text="Can I have that bunny plush?", command=lambda: dialog(53,persontalking,currentscene))
                root.button1.place(relx=.5, rely=0.65, anchor="n")
            root.nextbutton = tk.Button(root, text="Nothing, thank you", command=lambda: dialog(0,persontalking,currentscene))
            root.nextbutton.place(relx=.6, rely=0.65, anchor="n")
        if Interaction_Num == 52:
            root.Dialogue = tk.Label(root, text=f"Yes, here you go", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            root.rps_won = False
            root.breaker_won = False
            root.match_won = False
            root.Temporary_Items.append(["bunny",bunnyplush])
            Inventoryframes(root.Temporary_Items)
            root.button1 = tk.Button(root, text="Thank you", command=lambda: dialog(0,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")
        if Interaction_Num == 53:
            root.Dialogue = tk.Label(root, text=f"Oh, sorry. You need three tickets for that.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            root.button1 = tk.Button(root, text="Okay, i'll get those", command=lambda: dialog(0,persontalking,currentscene))
            root.button1.place(relx=.5, rely=0.65, anchor="n")

        if Interaction_Num == 54:
            root.Dialogue = tk.Label(root, text=f"Thank you!! I love it!", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            itemframe_Deletion("bunny",root.bunny)
            root.nextbutton = tk.Button(root, text="You're welcome, I guess", command=lambda: dialog(55,'Security',currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")

        if Interaction_Num == 55:
            root.Dialogue = tk.Label(root, text=f"That'll keep her busy.\nI can go supervise the elevator fixing now.", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            root.canel = True
            root.elevatorhall = ImageTk.PhotoImage(elevatorhallfixed)
            root.floor9 = ImageTk.PhotoImage(floor9canel)
            root.nextbutton = tk.Button(root, text="Oh good.", command=lambda: dialog(0,"Sad girl",[root.floor9,13]))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")
            
        if Interaction_Num == 56:
            root.Dialogue = tk.Label(root, text=f"It's so cute! Thank you!", font=("Arial", 40), bg="tan")
            root.Dialogue.place(relx=.5, rely=0.4, anchor="n")
            root.nextbutton = tk.Button(root, text="I'm glad you like it!", command=lambda: dialog(0,persontalking,currentscene))
            root.nextbutton.place(relx=.5, rely=0.65, anchor="n")

        if Interaction_Num == 0:
            scene(currentscene[0],currentscene[1])
    def itemframe_Deletion(Item_type,Item_Name):
        for x in root.Temporary_Items:
            if x[0] == Item_type:
                root.Temporary_Items.pop(root.Temporary_Items.index(x))
                Item_Name.place_forget()
                
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
        #root.empty = tk.Button(root,image=itemframe, command=lambda:item_selection("None",root.empty))
        #root.empty.place(relx=0.1, rely=0.85,anchor="n")
        root.InventoryCount = 0
        for x in Inventory:
            root.InventoryCount += 0.1
            if x[0] == "Bobbypin":
                root.Testitem = tk.Button(root,image=x[1],command=lambda:item_selection(x[0],root.Testitem))
                root.Testitem.place(relx=root.InventoryCount, rely=0.8,anchor="n")
            if x[0] == "sbobbypinlabel":
                root.sbobbypinlabel = tk.Button(root,image=x[1],command=lambda:item_selection(x[0],root.Testitem))
                root.sbobbypinlabel.place(relx=root.InventoryCount, rely=0.8,anchor="n")
            if x[0] == "Brokenbooby":
                root.Testitem = tk.Button(root,image=x[1],command=lambda:item_selection(x[0],root.Testitem))
                root.Testitem.place(relx=root.InventoryCount, rely=0.8,anchor="n")
            if x[0] == "Toycars":
                root.Toycars = tk.Button(root,image=x[1],command=lambda:item_selection(x[0],root.Testitem))
                root.Toycars.place(relx=root.InventoryCount, rely=0.8,anchor="n")
            if x[0] == "CandyTicket":
                root.CandyTicket = tk.Button(root,image=x[1],command=lambda:item_selection(x[0],root.Testitem))
                root.CandyTicket.place(relx=root.InventoryCount, rely=0.8,anchor="n")
            if x[0] == "CandyPin":
                root.CandyPin = tk.Button(root,image=x[1],command=lambda:item_selection(x[0],root.Testitem))
                root.CandyPin.place(relx=root.InventoryCount, rely=0.8,anchor="n")
            if x[0] == "bunny":
                root.bunny = tk.Button(root,image=x[1],command=lambda:item_selection(x[0],root.Testitem))
                root.bunny.place(relx=root.InventoryCount, rely=0.8,anchor="n")
            if x[0] == "Fish_order":
                root.fish = tk.Button(root,image=x[1],command=lambda:item_selection(x[0],root.Testitem))
                root.fish.place(relx=root.InventoryCount, rely=0.8,anchor="n")
    def item(ItemName):
        if ItemName == "Bobbypin":
            root.boobypinbool = True
            root.item.place_forget()
            #Hey I Do Not know what we are really doing for the item logic so just replace this with the function for item storage
            root.Temporary_Items.append(["Bobbypin",bobbypin])
            Inventoryframes(root.Temporary_Items)
        elif ItemName == "RPS" or ItemName == "Brick" or ItemName == "Match":
            root.arcade_death = True
            root.destroy()
            root.rps_won,root.breaker_won,root.match_won = run_arcade(root.rps_won,root.breaker_won,root.match_won)
        if ItemName == "2dollars":
            root.dollars2bool = True
            root.item.place_forget()
            #Hey I Do Not know what we are really doing for the item logic so just replace this with the function for item storage
            root.currency += 2
            root.currecytag.configure(text=f"Current cash:{root.currency}")
            Inventoryframes(root.Temporary_Items)
        elif ItemName == "candystoredialogue":
            dialog(1,"CandyStore Owner",[candystore,5])
        elif ItemName == "toystoredialogue":
            dialog(14,"toy store worker",[toystore,7])
        elif ItemName == "candy_arcade":
            for x in root.Temporary_Items:
                if x[0] == "CandyTicket":
                    root.item.place_forget()
                    won = treat_trios()
                    if won:
                        itemframe_Deletion("CandyTicket",root.CandyTicket)
                        root.Temporary_Items.append(["CandyPin",candypin])
                    else:
                        itemframe_Deletion("CandyTicket",root.CandyTicket)
                        root.Temporary_Items.append(["CandyPin",candypin])
                    root.item = tk.Button(root, image=candy_arcade, command=lambda: item("candy_arcade"))
                    root.item.place(relx=.75, rely=0.2,anchor="n")
                    Inventoryframes(root.Temporary_Items)
        elif ItemName == "Kid1Dialogue":
            dialog(7,"Kid 1",[kidsection,4])
        elif ItemName == "Kid2Dialogue":
            dialog(20,"Kid 2",[kidsection,4])
        elif ItemName == "Shydudetalk":
            dialog(31,"Shy guy",[food_court,10])
        elif ItemName == "fish":
            dialog(37,"Fish store worker",[fish_Station,11])
        elif ItemName == "Security":
            dialog(42,"Security",[root.floor9,13])
        elif ItemName == "Sad":
            dialog(47,"Sad girl",[root.floor9,13])
        elif ItemName == "Happy":
            dialog(56,"Happy girl",[root.floor9,13])
        elif ItemName == "Aguy":
            dialog(51,"Arcade worker",[arcadestaff,17])


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
            if root.elevator_unlocked:
                pass
        if SceneData == 2:
            root.FrsButton = tk.Button(root, image=downarrow, command=lambda:scene(root.elevatorhall,1))
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
            root.FrsButton = tk.Button(root, image=downarrow, command=exit_candy_store)
            root.FrsButton.place(relx=.5, rely=0.65,anchor="n")
            if root.stairsavailible == True:
                root.secButton = tk.Button(root, image=uparrow, command=lambda:scene(stairs10,8))
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
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(stairs9,9))
            root.secButton.place(relx=.7, rely=0.4,anchor="n")
        if SceneData == 9:
            root.secButton = tk.Button(root, image=downarrow, command=goto_candystore_from_stairs)
            root.secButton.place(relx=.5, rely=0.65,anchor="n")
        if SceneData == 10:
            root.fourthbutton = tk.Button(root, image=uparrow, command=lambda:scene(fish_Station,11))
            root.fourthbutton.place(relx=.45, rely=0.2,anchor="n")
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(stairs9,9))
            root.secButton.place(relx=.5, rely=0.65,anchor="n")
            root.FrsButton = tk.Button(root, image=uparrow, command=lambda:scene(Boorage_boost,12))
            root.FrsButton.place(relx=.15, rely=0.45,anchor="n")
            if root.CanFloor9 == True:
                root.thirdButton = tk.Button(root, image=rightarrow, command=lambda:scene(root.floor9,13))
                root.thirdButton.place(relx=.95, rely=0.5,anchor="n")
        if SceneData == 11:
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(food_court,10))
            root.secButton.place(relx=.5, rely=0.65,anchor="n")
        if SceneData == 12:
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(food_court,10))
            root.secButton.place(relx=.5, rely=0.65,anchor="n")
        if SceneData == 13:
            root.fourthbutton = tk.Button(root, image=uparrow, command=lambda:scene(arcadescene,16))
            root.fourthbutton.place(relx=.68, rely=0.46,anchor="n")
            root.secButton = tk.Button(root, image=uparrow, command=lambda:scene(infodesk,14))
            root.secButton.place(relx=.115, rely=0.46,anchor="n")
            root.FrsButton = tk.Button(root, image=downarrow, command=lambda:scene(food_court,10))
            root.FrsButton.place(relx=.5, rely=0.65,anchor="n")
        if SceneData == 14:
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(root.floor9,13))
            root.secButton.place(relx=.5, rely=0.65,anchor="n")
            root.fourthbutton = tk.Button(root, image=uparrow, command=lambda:scene(root.elevatorhall,15))
            root.fourthbutton.place(relx=.65, rely=0.2,anchor="n")
        if SceneData == 15:
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(infodesk,14))
            root.secButton.place(relx=.5, rely=0.65,anchor="n")
            if root.canel == True:
                root.fourthbutton = tk.Button(root, image=uparrow, command=lambda:scene(exitdoor,18))
                root.fourthbutton.place(relx=.32, rely=0.49,anchor="n")
        if SceneData == 16:
            root.secButton = tk.Button(root, image=downarrow, command=lambda:scene(root.floor9,13))
            root.secButton.place(relx=.5, rely=0.65,anchor="n")
            root.thirdButton = tk.Button(root, image=rightarrow, command=lambda:scene(arcadestaff,17))
            root.thirdButton.place(relx=.95, rely=0.5,anchor="n")
        if SceneData == 17:
            
            root.FrsButton = tk.Button(root, image=leftarrow, command=lambda:scene(arcade,16))
            root.FrsButton.place(relx=.15, rely=0.5,anchor="n")
        if SceneData == 18:
            pass
        #this is what ever you would want to do to end the game
        

           
            #root.frsButton.place(relx=.02, rely=0.5,anchor="n")
    def SceneItems(SceneData):

        try:
            root.item.place_forget()
        except:
            pass
        try:
            root.item2.place_forget()
        except:
            pass
        try:
            root.item3.place_forget()
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
            pass
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
        if SceneData == 11:
            root.Dailog = tk.Button(root, image=dialouginteraction, command=lambda: item("fish"))
            root.Dailog.place(relx=.55, rely=0.1,anchor="n")
        if SceneData == 13:
            if root.canel:
                root.item = tk.Button(root, image=dialouginteraction, command=lambda: item("Happy"))
                root.item.place(relx=.50, rely=0.245,anchor="n")
            else:
                root.Dailog = tk.Button(root, image=dialouginteraction, command=lambda: item("Security"))
                root.Dailog.place(relx=.41, rely=0.14,anchor="n")
                root.item = tk.Button(root, image=dialouginteraction, command=lambda: item("Sad"))
                root.item.place(relx=.50, rely=0.245,anchor="n")
        if SceneData == 16:
            root.item = tk.Button(root, image=arcade_RPS, command=lambda: item("RPS"))
            root.item.place(relx=.43, rely=0.25,anchor="n")
            root.item2 = tk.Button(root, image=arcade_brick, command=lambda: item("Brick"))
            root.item2.place(relx=.53, rely=0.25,anchor="n")
            root.item3 = tk.Button(root, image=arcade_card, command=lambda: item("Match"))
            root.item3.place(relx=.63, rely=0.25,anchor="n")
        if SceneData == 17:
            root.Dailog = tk.Button(root, image=dialouginteraction, command=lambda: item("Aguy"))
            root.Dailog.place(relx=.55, rely=0.1,anchor="n")
        
            
    def scene(background,SceneData):
        root.scenenumber = SceneData
        kill()
        root.backgroundlabel.configure(image=background)
        SceneButtons(SceneData)
        SceneItems(SceneData)

    for i in root.Temporary_Items:
        if len(i) == 1:
            i.append(ImageTk.PhotoImage(Image.open(item_images[i[0]])))
    Inventoryframes(root.Temporary_Items)
    
    scene_images = {
        1: root.elevatorhall,
        2: main10,
        3: garden,
        4: kidsection,
        5: candystore,
        6: infodesk,
        7: toystore,
        8: stairs10,
        9: stairs9,
        10: food_court,
        11: fish_Station,
        12: Boorage_boost,
        13: root.floor9,
        14: infodesk,
        15: root.elevatorhall,
        16: arcade,
        17: arcadestaff,
        18: exitdoor
    }
    scene(scene_images[root.scenenumber],root.scenenumber)
    
    root.mainloop()

    #this bit returns a dictionary with the fields listed in export_fields
    root_dictionary = root.__dict__
    export_data = {}
    for key in export_fields:
        export_data[key] = root_dictionary[key]
    export_data['classtype'] = 'Tk'
    export_data['Temporary_Items'] = [[i[0]] for i in export_data['Temporary_Items']]
    return export_data

#you must get new roots from this function and not from Tk()
def root_setup():
    root = tk.Tk()
    root.currency = 5
    root.Temporary_Items = []
    root.Item_Selected = "None"
    root.testItemBool = 0
    root.boobypinbool = False
    root.dollars2bool = False
    root.stairsavailible = False
    root.orderrecipt = False
    root.orderdone = False
    root.CanFloor9 = False
    root.canel = False
    root.rps_won = False
    root.breaker_won = False
    root.match_won = False
    root.arcade_death = False
    root.scenenumber = 1
    return root

def launch_game(data):
    while True:
        firsttime = False
        data['arcade_death'] = False
        try: 
            data['scenenubmer']
        except:
            firsttime = True
        if firsttime:
            data = game(1,data)
        else:
            data = game(data['scenenumber'],data)
        if not data['arcade_death']:
            break
    
    return data
#data = game(1,root_setup())