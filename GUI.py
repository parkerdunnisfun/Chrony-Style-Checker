from ast import Delete
from tkinter import *

from Checker import MarkedUp
from Date_converter import convert
 
root = Tk()
 
root.title("Chrony Style Checker")
root.geometry('1000x700')
 
checker_lbl = Label(root, text = "Insert text below to catch Chrony style errors\nGreen = Good\nRed = Bad")
checker_lbl.grid()
converter_lbl = Label(root, text = "Convert date to Chrony style below (mm/dd/yyyy)\ne.g. 01/22/1979")
converter_lbl.grid(column=1, row=0, padx=30)

# University of Utah rule textbox
checker_text_box = Text(
    root,
    height=45,
    width=70,
    wrap=WORD
)
checker_text_box.grid(column=0, row=2)

# converting dates to Chrony style textbox
converter_text_box = Text(
    root,
    height=1,
    width=20,
    wrap=WORD
)
converter_text_box.grid(column=1, row=2, sticky=N)

def checker_clicked():
    """
    Called when "Check" button is clicked. Gathers and highlights Chrony style accuracies and errors.
    """
    # resetting previous (if any) highlights
    for tag in checker_text_box.tag_names():
        checker_text_box.tag_remove(tag, "1.0", "end")

    clean_text = str(checker_text_box.get("1.0", "end"))

    # reformatting text for highlighting purposes
    checker_text_box.delete("1.0", "end")
    clean_text_final = clean_text.replace("\n", " ")
    checker_text_box.insert("1.0", clean_text_final)

    # getting text's accuracies and errors
    mu =  MarkedUp(clean_text_final)
    mu.clear()
    mu.u_reference_check()

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

def converter_clicked():
    """
    Called when "Convert" button is clicked. Converts dates in mm/dd/yyyy format to Chrony style.
    """
    date = convert(str(converter_text_box.get("1.0", "end")).strip())
    converter_text_box.delete(1.0, "end")
    converter_text_box.insert("end", date)
 
checker_btn = Button(root, text = "Check" ,
             fg = "red", command=checker_clicked)
checker_btn.grid(column=0, row=1)

converter_btn = Button(root, text = "Convert" ,
             fg = "red", command=converter_clicked)
converter_btn.grid(column=1, row=1)
 
root.mainloop()