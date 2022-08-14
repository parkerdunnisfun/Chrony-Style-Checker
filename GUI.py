# Import Module
from tkinter import *

from Checker import MarkedUp
from Date_converter import convert
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Chrony Style Converter")
# Set geometry(widthxheight)
root.geometry('1000x700')
 
# adding a label to the root window
checker_lbl = Label(root, text = "Insert text below to catch Chrony style errors\nGreen = Good\nRed = Bad\nYellow = Oxford Comma")
checker_lbl.grid()
converter_lbl = Label(root, text = "Convert date to Chrony style below (mm/dd/yyyy)")
converter_lbl.grid(column=1, row=0, padx=30)
 
# adding Entry Field
checker_text_box = Text(
    root,
    height=45,
    width=70,
    wrap=WORD
)
checker_text_box.grid(column=0, row=2)

converter_text_box = Text(
    root,
    height=1,
    width=20,
    wrap=WORD
)
converter_text_box.grid(column=1, row=2, sticky=N)

# function to display user text when button is clicked
def checker_clicked():
    for tag in checker_text_box.tag_names():
        checker_text_box.tag_remove(tag, "1.0", "end")
    mu =  MarkedUp(str(checker_text_box.get("1.0", "end")).strip())
    mu.clear()
    mu.u_reference_check()
    mu.oxford_comma_check()
    for x in mu.errors:
        start = "1." + str(x[0])
        end = "1." + str(x[1]+1)

        checker_text_box.tag_add("highlightred", start, end)
        checker_text_box.tag_config("highlightred", background="#FF7F7F",
                 foreground="black")
    for x in mu.good:
        start = "1." + str(x[0])
        end = "1." + str(x[1]+1)

        checker_text_box.tag_add("highlightgreen", start, end)
        checker_text_box.tag_config("highlightgreen", background="#90EE90",
                 foreground="black")
    for x in mu.warnings:
        start = "1." + str(x[0])
        end = "1." + str(x[1]+1)

        checker_text_box.tag_add("highlightyellow", start, end)
        checker_text_box.tag_config("highlightyellow", background="#FFFF00",
                 foreground="black")

def converter_clicked():
    date = convert(str(converter_text_box.get("1.0", "end")).strip())
    converter_text_box.delete(1.0, "end")
    converter_text_box.insert("end", date)
 
# button widget with red color text inside
checker_btn = Button(root, text = "Check" ,
             fg = "red", command=checker_clicked)
# Set Button Grid
checker_btn.grid(column=0, row=1)

# button widget with red color text inside
converter_btn = Button(root, text = "Convert" ,
             fg = "red", command=converter_clicked)
# Set Button Grid
converter_btn.grid(column=1, row=1)
 
# Execute Tkinter
root.mainloop()