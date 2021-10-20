import tkinter as tk
from tkinter import ttk
from PasswordStrength import *

root = tk.Tk()
dan = PassStrength()
root.title('PassWord Strength Checker') # Changes the title of the window
root.geometry('400x400+50+50') # Changes the sze of the window
# root.resizable(True)  Allows you to resize the window
def checkPass():
    input = text.get('1.0', 'end-1c')
    if (dan.hasNum(input)):
        containsNum.set('Contains Number: ✓')
    else:
        containsNum.set('Contains Number:  ')

    if (dan.lowerCaseWhole(input)):
        containsLower.set('Contains LowerCase: ✓')
    else:
        containsLower.set('Contains LowerCase:  ')

    if (dan.upperCaseWhole(input)):
        containsUpper.set('Contains UpperCase: ✓')
    else:
        containsUpper.set('Contains UpperCase:  ')

    if (False):
        containsSpecial.set('Contains Special Character: ✓')
    else:
        containsSpecial.set('Contains Special Character:  ')

    print(text.get('1.0', 'end-1c'))


frame = tk.Frame(root)
frame.columnconfigure(0, weight=7)

containsNum = tk.StringVar(root, "Contains Number: ")
containsUpper = tk.StringVar(root,"Contains UpperCase: ")
containsLower = tk.StringVar(root,"Contains LowerCase: ")
containsSpecial = tk.StringVar(root,"Contains Special Character: ")

prompt = tk.Label(root, text='Enter a Password:').grid(column=0,row=0)
numCheck = tk.Label(root,textvariable=containsNum).grid(column=0,row=1)
upperCheck = tk.Label(root,textvariable=containsUpper).grid(column=0,row=2)
lowerCheck = tk.Label(root, textvariable=containsLower).grid(column=0,row=3)
specialCheck = tk.Label(root, textvariable=containsSpecial).grid(column=0,row=4)

text = tk.Text(root, height=1, width=20)
text.insert('1.0', 'Password')
text.grid(column=1,row=0)
button = tk.Button(root, text='GO', command=lambda:checkPass())
newPass = tk.Text(root, height=1, width=20).grid(column=1,row=7)
generate = tk.Button(root, text='Generate').grid(column=0,row=7)
button.grid(column=2,row=0)



#ttk.Label(root, text='Enter a Password:Themed Label').pack() # .pack() adds it to the window
# Note that ttk stands for Tk themed. Therefore, Tk themed widgets are the same as ttk widgets
# Another way to make a label with text using a dictionary to specify an attribute
#label = ttk.Label(root)
#label['text'] = 'Another Example'
#label.pack()
# Another way to make a label with text using the config method
#label2 = ttk.Label(root)
#label2.config(text='Hello vrother')
#label2.pack()
# Tkinter Commands Binding


root.mainloop()
