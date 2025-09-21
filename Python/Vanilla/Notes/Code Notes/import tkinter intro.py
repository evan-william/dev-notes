import tkinter as tk

playerapp = tk.Tk() # THIS TO NAME THE WINDOW 
playerapp.geometry("500x500") # AUTOMATICALLY MAKE THE SQUARE WHEN OPENED
playerapp.title("Music Player") # ADDS TITLE
 
label = tk.Label(playerapp, text="Music Player", font=("Arial", 18)) # THIS TO DEFINE THE TEXT
# Only label.pack() also works
label.pack(padx=20, pady=20) # THIS TO ADD THE TEXT


textbox = tk.Text(playerapp, height= 3, font=('Arial', 16)) # THIS TO DEFINE THE TEXTBOX
textbox.pack(padx=10, pady=1) # THIS TO ADD THE TEXTBOX

""" THIS TO ADD NON MULTIPLE LINE STUFF LIKE PASSWORD
textbox2 = tk.Entry(playerapp)
textbox2.pack()
"""

button1 = tk.Button(playerapp, text="Test !", font=('Arial', 8), width="20") # THIS TO DEFINE BUTTON
button1.pack(pady=10) # THIS TO ADD THE BUTTON

# ADDING GRID

frame1 = tk.Frame(playerapp) # TO DEFINE 3 COLUMNS
frame1.columnconfigure(0, weight = 1)
frame1.columnconfigure(1, weight = 1)
frame1.columnconfigure(2, weight = 1)

button2 = tk.Button(frame1, text="Test Again! ", font=('Arial', 8)) # DEFINE FIRST OF 3 BUTTON
button2.grid(row=0, column=0, sticky=tk.W + tk.E) # THIS TO ADD THE BUTTON TO GRID , NOT USING PACK
# row = 0 , colum = 0 means first row first column
# sticky is to make it fill the screen and not like all in middle badly

button3 = tk.Button(frame1, text="Test Again 2! ", font=('Arial', 8)) # DEFINE FIRST OF 3 BUTTON
button3.grid(row=0, column=1, sticky=tk.W + tk.E)

button4 = tk.Button(frame1, text="Test Again 3! ", font=('Arial', 8)) # DEFINE FIRST OF 3 BUTTON
button4.grid(row=0, column=2, sticky=tk.W + tk.E)

button5 = tk.Button(frame1, text="Test Again 4! ", font=('Arial', 8)) # DEFINE FIRST OF 3 BUTTON
button5.grid(row=1, column=0, sticky=tk.W + tk.E)
             
button6 = tk.Button(frame1, text="Test Again 5! ", font=('Arial', 8)) # DEFINE FIRST OF 3 BUTTON
button6.grid(row=1, column=1, sticky=tk.W + tk.E)

button7 = tk.Button(frame1, text="Test Again 6! ", font=('Arial', 8)) # DEFINE FIRST OF 3 BUTTON
button7.grid(row=1, column=2, sticky=tk.W + tk.E)
             
frame1.pack(fill='x') # THIS TO ADD THE ALL FRAME WE MADE FROM ABOVE
# FILL = X means it will stretch to the x dimension


precisebutton = tk.Button(playerapp, text="PRCISE") # DEFINE LIKE ALWAYSS
precisebutton.place(x=200, y=200, height= 100, width= 100) # PUT BUTTON AT THAT COORDS

playerapp.mainloop() # THIS TO INITIATE THE OPEN WINDOW