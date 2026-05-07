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
root.testItemBool = 0
root.Item_Selected = "None"

#The main part
#itemframe_btn = tk.Button(root, image=itemframe)
#itemframe_btn.place(relx=.5, rely=0.90, anchor="n")
def dialog(Interaction_Num,persontalking):
    pass
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
        if x[0] == "Test":
            root.Testitem = tk.Button(root,image=x[1],command=lambda:item_selection(x[0],root.Testitem))
            root.Testitem.place(relx=root.InventoryCount, rely=0.75,anchor="n")
def item(ItemName):
    if ItemName == "Test":
        root.testItemBool += 1
        root.item.place_forget()
        #Hey I Do Not know what we are really doing for the item logic so just replace this with the function for item storage
        root.Temporary_Items.append(["Test",oj])
        Inventoryframes(root.Temporary_Items)

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
        root.FrsButton = tk.Button(root, image=itemframe, command=lambda:scene(main10,2))
        root.FrsButton.place(relx=.61, rely=0.5,anchor="n")
    if SceneData == 2:
        root.FrsButton = tk.Button(root, image=itemframe, command=lambda:scene(elevatorhall,1))
        root.FrsButton.place(relx=.5, rely=0.65,anchor="n")

        root.secButton = tk.Button(root, image=itemframe, command=lambda:scene(garden,3))
        root.secButton.place(relx=.95, rely=0.5,anchor="n")

        root.thirdButton = tk.Button(root, image=itemframe, command=lambda:scene(kidsection,4))
        root.thirdButton.place(relx=.05, rely=0.5,anchor="n")

        root.fourthbutton = tk.Button(root, image=itemframe, command=lambda:scene(candystore,5))
        root.fourthbutton.place(relx=.7, rely=0.45,anchor="n")

        root.fithbutton = tk.Button(root, image=itemframe, command=lambda:scene(infodesk,6))
        root.fithbutton.place(relx=.25, rely=0.45,anchor="n")
    if SceneData == 3:
        root.secButton = tk.Button(root, image=itemframe, command=lambda:scene(main10,2))
        root.secButton.place(relx=.05, rely=0.5,anchor="n")
    if SceneData == 4:
        root.secButton = tk.Button(root, image=itemframe, command=lambda:scene(main10,2))
        root.secButton.place(relx=.95, rely=0.5,anchor="n")

        root.fourthbutton = tk.Button(root, image=itemframe, command=lambda:scene(toystore,7))
        root.fourthbutton.place(relx=.8, rely=0.45,anchor="n")
    if SceneData == 5:
        root.FrsButton = tk.Button(root, image=itemframe, command=lambda:scene(main10,2))
        root.FrsButton.place(relx=.5, rely=0.65,anchor="n")
    if SceneData == 6:
        root.FrsButton = tk.Button(root, image=itemframe, command=lambda:scene(main10,2))
        root.FrsButton.place(relx=.5, rely=0.65,anchor="n")
    if SceneData == 7:
        root.fourthbutton = tk.Button(root, image=itemframe, command=lambda:scene(kidsection,4))
        root.fourthbutton.place(relx=.8, rely=0.45,anchor="n")
        #root.frsButton.place(relx=.02, rely=0.5,anchor="n")
def SceneItems(SceneData):

    try:
        root.item.place_forget()
    except:
        pass
    if SceneData == 1:
        if root.testItemBool != 1:
            root.item = tk.Button(root, image=oj, command=lambda: item("Test"))
            root.item.place(relx=.5, rely=0.1,anchor="n")
        
def scene(background,SceneData):
    root.backgroundlabel.configure(image=background)
    SceneButtons(SceneData)
    SceneItems(SceneData)


#Test scene Data
scene(elevatorhall,1)
root.mainloop()