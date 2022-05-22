# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:50:44 2022

@author: atbaldwin
"""
import tkinter as tk
from tkinter import (filedialog, ttk, Button, N, W, E, S, Tk, Label)

filename = str()
outputtext = str()
# █▓▒░░▒▓█
def Ui():
    root = Tk()
    root.geometry("780x216")
    root.title()
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    shortString = tk.StringVar()
    
    #filename to select txts
    def filenamefetch():
        global filename
        global outputtext
        filename = filedialog.askopenfilename(
            initialdir='/', title="Select .txt file")
        ttk.Label(mainframe, text=filename +
                  ': loaded').grid(column=4, row=2, sticky=(W))
        with open(filename) as f:
            outputtext = f.readlines()
        #print(outputtext)
        return filename
    
    ###text field for short strings
    shortstring_entry = ttk.Entry(mainframe, width=70, textvariable=shortString)
    shortstring_entry.grid(column=4, row=4)
    
    ###Buttons
    filenameButton = Button(mainframe, text='Load New .txt', command=lambda: (
        filenamefetch()))
    filenameButton.grid(column=3, row=2)
    quitButton = Button(mainframe, text="Exit Program", command=root.destroy)
    quitButton.grid(column=0, row=1)
    stringButton = Button(mainframe, text="Process String", command=lambda: SixtyTranslator([str(shortString.get())]))
    stringButton.grid(column=2, row=4)
    translatetxtButton = Button(mainframe, text="Process .txt file", command=lambda: SixtyTranslator(outputtext))
    translatetxtButton.grid(column=2, row=2)
    
    ##Text labels
    option1 = Label(mainframe, text='Option 1:')
    option1.grid(column=3, row=1)
    option2 = Label(mainframe, text='Option 2:')
    option2.grid(column=3, row=3)
    txtInstructLabel = Label(mainframe, text='Load a .txt file using the \"Load New .txt\" button, then click \"Process .txt file\":')
    txtInstructLabel.grid(column=4, row=1, sticky=(W))
    strInstructLabel = Label(mainframe, text='Enter desired alphanumeric text in the box below, then click \"Process String\":')
    strInstructLabel.grid(column=4, row=3, sticky=(W))
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
    root.mainloop()

def SixtyTranslator(inputList: list):
    outputList = []
    for inputString in inputList:
        outputString = ''
        fullshade = 'hfszv'
        mostshade = 'mngcboyu3457'
        halfshade = 'aeixjwrl9160'
        lightshade = 'dktpq28'
        for character in inputString.lower():
            if character in fullshade:
                outputString += '█'
            elif character in mostshade:
                outputString += '▓'
            elif character in halfshade:
                outputString += '▒'
            elif character in lightshade:
                outputString += '░'
            
            if character == ' ':
             outputString += ' '
        outputList.append(outputString + '\n')
    #print(outputList)
    with open('Translated.txt', 'w', encoding='utf-8') as a:
        a.writelines(outputList)
        a.close()
    print('Done.')
    return outputString

#SixtyTranslator(['I dont know what to do, maybe you can help. Extreme pants.'])
Ui()