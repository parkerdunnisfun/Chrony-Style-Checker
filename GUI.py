# Import Module
from tkinter import *

from Checker import MarkedUp
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Chrony Style Converter")
# Set geometry(widthxheight)
root.geometry('700x700')
 
# adding a label to the root window
lbl = Label(root, text = "Insert text below to catch Chrony style errors")
lbl.grid()
 
# adding Entry Field
text_box = Text(
    root,
    height=50,
    width=70,
    wrap=WORD
)
text_box.grid(column=0, row=1)

# function to display user text when button is clicked
def clicked():
    # DELETE: looking at tags
    for tag in text_box.tag_names():
        text_box.tag_remove(tag, "1.0", "end")
    mu =  MarkedUp(str(text_box.get("1.0", "end")).strip())
    mu.clear()
    mu.u_reference_check()
    for x in mu.errors:
        start = "1." + str(x[0])
        end = "1." + str(x[1]+1)

        text_box.tag_add("highlightred", start, end)
        text_box.tag_config("highlightred", background="#FF7F7F",
                 foreground="black")
    for x in mu.good:
        start = "1." + str(x[0])
        end = "1." + str(x[1]+1)

        text_box.tag_add("highlightgreen", start, end)
        text_box.tag_config("highlightgreen", background="#90EE90",
                 foreground="black")
 
# button widget with red color text inside
btn = Button(root, text = "Check" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=1)
 
# Execute Tkinter
root.mainloop()