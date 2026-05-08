import tkinter as tk
from PIL import Image, ImageTk
import time
root = tk.Tk()
root.title("IDK MAN")


root.configure(background="light blue")
root.minsize(2600,1400)
root.maxsize(2600,1400)

#Images

itemframe = Image.open("Images/ItemFrame.png.png")
itemframe = ImageTk.PhotoImage(itemframe)

Selitemframe = Image.open("Images/SlectedItemFrame.png.png")
Selitemframe = ImageTk.PhotoImage(Selitemframe)

elevatorhall = Image.open("Images/ElevatorHall.png.png")
elevatorhall = ImageTk.PhotoImage(elevatorhall)

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

stairs = Image.open("Images/Stairs.png.png")
stairs = ImageTk.PhotoImage(stairs)

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

#button.pack(pady=20)
root.passed_Sleceted_item = "Empty"
root.Temporary_Items = []


#Diffrent items
root.Item_Selected = "None"
root.testItemBool = 0
root.boobypinbool = False
root.stairsavailible = False

#The main part
#itemframe_btn = tk.Button(root, image=itemframe)
#itemframe_btn.place(relx=.5, rely=0.90, anchor="n")
def dialog(Interaction_Num,persontalking,currentscene):
    scene(dialoguebox,0)
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
        root.Dialogue = tk.Label(root, text="Welcome!", font=("Arial", 20))
        root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
        root.nextbutton = tk.Button(root, text="Goodbye", command=lambda: dialog(0,persontalking,currentscene))
        root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
        root.button1 = tk.Button(root, text="I need to get down to floor 9…", command=lambda: dialog(2,persontalking,currentscene))
        root.button1.place(relx=.5, rely=0.65, anchor="n")
        root.button2 = tk.Button(root, text="Who are you?", command=lambda: dialog(3,persontalking,currentscene))
        root.button2.place(relx=.4, rely=0.65, anchor="n")
        root.button3 = tk.Button(root, text="What are your thoughts on cats?", command=lambda: dialog(4,persontalking,currentscene))
        root.button3.place(relx=.3, rely=0.65, anchor="n")
    if Interaction_Num == 2:
        root.Dialogue = tk.Label(root, text="Candy Staff: “Oh! Well, this store spans floor 9 and 10…so I can let you use our back stairs…but where are your parents? And why can’t you go down?”", font=("Arial", 20))
        root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
        root.button1 = tk.Button(root, text="None of your business.", command=lambda: dialog(0,persontalking,currentscene))
        root.button1.place(relx=.6, rely=0.65, anchor="n")
        root.button2 = tk.Button(root, text="Don’t worry, I just need to get something for my parents. The elevator is broken by the way.", command=lambda: dialog(5,persontalking,currentscene))
        root.button2.place(relx=.4, rely=0.65, anchor="n")
    if Interaction_Num == 3:
        root.Dialogue = tk.Label(root, text="“Well, the owner of this store of course!”", font=("Arial", 20))
        root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
        root.nextbutton = tk.Button(root, text="Goodbye", command=lambda: dialog(0,persontalking,currentscene))
        root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
    if Interaction_Num == 4:
        root.Dialogue = tk.Label(root, text="“Eh, they’re fine.”", font=("Arial", 20))
        root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
        root.nextbutton = tk.Button(root, text="Goodbye", command=lambda: dialog(0,persontalking,currentscene))
        root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
    if Interaction_Num == 5:
        root.Dialogue = tk.Label(root, text="If you say so. Now…I did lose the key…so if you have something we can lockpick with, then let’s use it.", font=("Arial", 20))
        root.Dialogue.place(relx=.5, rely=0.5, anchor="n")
        for x in root.Temporary_Items:
            if x[0] == "Bobbypin":
                root.button1 = tk.Button(root, text="Give Bobby pin", command=lambda: dialog(6,persontalking,currentscene))
                root.button1.place(relx=.3, rely=0.65, anchor="n")
        root.button2 = tk.Button(root, text="Let me go look for something", command=lambda: dialog(0,persontalking,currentscene))
        root.button2.place(relx=.5, rely=0.65, anchor="n")
    if Interaction_Num == 6:
        root.Dialogue = tk.Label(root, text="“The stairs are now availible”", font=("Arial", 20))
        root.nextbutton = tk.Button(root, text="Goodbye", command=lambda: dialog(0,persontalking,currentscene))
        root.nextbutton.place(relx=.5, rely=0.75, anchor="n")
        root.stairsavailible = True
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
            root.Testitem.place(relx=root.InventoryCount, rely=0.75,anchor="n")
def item(ItemName):
    if ItemName == "Bobbypin":
        root.boobypinbool = False
        root.item.place_forget()
        #Hey I Do Not know what we are really doing for the item logic so just replace this with the function for item storage
        root.Temporary_Items.append(["Bobbypin",bobbypin])
        Inventoryframes(root.Temporary_Items)
    if ItemName == "candystoredialogue":
        dialog(1,"CandyStoreOwner",[candystore,5])

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
            root.secButton.place(relx=.8, rely=0.2,anchor="n")
    if SceneData == 6:
        root.FrsButton = tk.Button(root, image=downarrow, command=lambda:scene(main10,2))
        root.FrsButton.place(relx=.5, rely=0.65,anchor="n")
    if SceneData == 7:
        root.fourthbutton = tk.Button(root, image=uparrow, command=lambda:scene(kidsection,4))
        root.fourthbutton.place(relx=.8, rely=0.45,anchor="n")
        #root.frsButton.place(relx=.02, rely=0.5,anchor="n")
def SceneItems(SceneData):

    try:
        root.item.place_forget()
    except:
        pass
    if SceneData == 1:
        if root.boobypinbool == False:
            root.item = tk.Button(root, image=bobbypin, command=lambda: item("Bobbypin"))
            root.item.place(relx=.5, rely=0.1,anchor="n")
    if SceneData == 5:
        root.item = tk.Button(root, image=dialouginteraction, command=lambda: item("candystoredialogue"))
        root.item.place(relx=.5, rely=0.1,anchor="n")
        
def scene(background,SceneData):
    root.backgroundlabel.configure(image=background)
    SceneButtons(SceneData)
    SceneItems(SceneData)


#Test scene Data
scene(elevatorhall,1)
root.mainloop()