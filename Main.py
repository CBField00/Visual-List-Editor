from tkinter import *
import Trace

Object_List = []
Last_Index = []
Tracer = Trace.Trace()

def Start():
    global root

    root = Tk()
    root.attributes("-toolwindow", True)
    root.title("List Editor")
    root.geometry("640x480")
    Tracer.Trace("New Main Window [root] Created")
    Button_Frame = Frame(root)
    Button_Frame.pack()

    New_Item = Button(Button_Frame, text="Add New Item", bg="Green", fg="white", width=15, height=3, command=Add_New_Item_Front)
    New_Item_At_Index = Button(Button_Frame, text="New Item at Index", bg="Blue", fg="white", width=15, height=3, command=Add_At_Index_Front)

    Delete_Item = Button(Button_Frame, text="Delete Item", bg="Red", fg="white", width=15, height=3, command=Remove_From_End)
    Delete_Index_Item = Button(Button_Frame, text="Delete By Index", bg="blue", fg="white", width=15, height=3, command=Remove_By_Index)
    Clear = Button(Button_Frame, text="Clear All List", bg="Yellow", fg="Black", width=15, height=3, command=Clear_List)

    EndTrace = Trace._EndTrace()
    EndTrace._EndTrace(Button_Frame, 2, 3, 15, 3, "red", "white")


    New_Item.grid(row=1, column=1, padx=2, pady=3)
    New_Item_At_Index.grid(row=1, column=2, padx=2, pady=3)

    Delete_Item.grid(row=2, column=1, padx=2, pady=3)
    Delete_Index_Item.grid(row=2, column=2, padx=2, pady=3)
    Clear.grid(row=1, column=3, padx=2, pady=3)

    Tracer.Trace("All Buttons and Frames Created and Drawn")
    List_View()

    root.mainloop()


def List_View():
    global List_Frame

    List_Frame = Frame(root)
    List_Frame.pack()

    x = 0
    y = 0

    Tracer.Trace(f"x: {x}, y: {y}")

    try:
        L_Index = Last_Index[-1]
        print(f"Last Index: {L_Index}")
        Tracer.Trace("Attempted Last Index Collection")

    except(IndexError):
        print("Expected IndexError")
        Tracer.Trace("Index Error Raised, and handled")

    for i in range(len(Object_List)):

        if x == 10:
            y += 1
            x = 0
        l = Label(List_Frame, text=Object_List[i], relief=SUNKEN, bg="white", fg="black", width = 10)
        if i == L_Index:
            l.config(bg="blue", fg="white")
            Tracer.Trace("Last Index Graphically Identified")

        l.grid(row=y, column=x, padx=1, pady=1)
        x += 1

def Add_New_Item_Front():
    global New_Item_Entry

    New_Item = Toplevel()
    New_Item.title("Add New Entity")

    New_Item_Entry = Entry(New_Item)
    New_Item_Entry.grid(row=1, column=1)
    Add_Button = Button(New_Item, text="Add", bg="Green", fg="White", width=15, command=Add_Item_Back)
    Add_Button.grid(row=2, column=1)
    Tracer.Trace("New Window [Entity Creation] Created")
    New_Item.mainloop()

def Add_Item_Back():
    if len(New_Item_Entry.get()) != 0:
        List_Frame.destroy()
        Object_List.append(New_Item_Entry.get())
        Last_Index.append(len(Object_List) - 1)
        Tracer.Trace(f"New Entity Added to List: {New_Item_Entry.get()}")
        List_View()
    else:
        print("NOPE!")
        Tracer.Trace("Entity Isnt Valid, Skipping")

def Add_At_Index_Front():
    global New_Index_Entry, Index, New_Index

    New_Index = Toplevel()

    New_Index_Entry = Entry(New_Index)
    Index = Scale(New_Index, from_=0, to=len(Object_List), orient=HORIZONTAL)
    Add_Index = Button(New_Index, text="Add", bg="Green", fg="White", command=Add_At_Index_Back)

    New_Index_Entry.grid(row=1, column=1)
    Index.grid(row=2, column=1, columnspan=2)
    Add_Index.grid(row=3, column=1)
    Tracer.Trace("New Window [Inserting @ Index] Created")
    New_Index.mainloop()

def Add_At_Index_Back():

    if len(New_Index_Entry.get()) > 0:

        Object_List.insert(Index.get(), New_Index_Entry.get())
        Tracer.Trace(f"New Entity{New_Index_Entry.get()} at Index {Index.get()}")
        Last_Index.append(Index.get())
        New_Index.destroy()
        List_Frame.destroy()
        List_View()
    else:
        print("Not Long Enough")
        Tracer.Trace("Index Entry Invalid")

def Remove_From_End():
    Tracer.Trace(f"End Object Removed: {Object_List[len(Object_List) - 1]}")
    Object_List.remove(Object_List[len(Object_List) - 1])
    List_Frame.destroy()
    List_View()


def Remove_By_Index():
    global remove_Index, r, r_Index

    r_Index = Toplevel()

    r = Scale(r_Index, from_=0, to=len(Object_List) - 1, orient=HORIZONTAL)
    remove_Index = Button(r_Index, text="Remove", bg="Red", fg="White", command=Remove_By_Index_Back)

    r.grid(row=2, column=1, columnspan=2)
    remove_Index.grid(row=3, column=1)
    Tracer.Trace("Remove By Index Window Created")
    r_Index.mainloop()

def Remove_By_Index_Back():
    Tracer.Trace(f"Object Removed at Index{r.get()}: {Object_List[r.get()]}")
    Object_List.pop(r.get())
    r_Index.destroy()
    List_Frame.destroy()
    List_View()

def Clear_List():
    for i in range(len(Object_List)):
        Object_List.pop(0)
    Tracer.Trace("List Cleared")
    List_Frame.destroy()
    List_View()

Start()