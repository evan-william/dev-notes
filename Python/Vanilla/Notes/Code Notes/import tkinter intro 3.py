import tkinter as tk
from tkinter import messagebox

class MyGUI():
    def __init__(self):
        self.root = tk.Tk()
        
        self.label = tk.Label(self.root, text="Your Message", font=('Arial',18))
        self.label.pack(padx=10,pady=10)
        
        self.textbox = tk.Text(self.root,height= 5 ,font=('Arial',16))
        self.textbox.pack(padx=10,pady=10)
        
        
        self.check_state = tk.IntVar() # ADD VARIALBE CUZ THATS HOW CHECK WORKS 
        
        self.checkez = tk.Checkbutton(self.root, text="Show Messagebox",font=('Arial',16), variable=self.check_state)
        self.checkez.pack(padx=10,pady=10)
        
        self.button = tk.Button(self.root, text="Show Message",font=('Arial',16), command=self.show_message)
        # THE USE OF COMMAND WILL CALL THE FUNCTION WHEN CLICKED
        self.button.pack(padx=10,pady=10)
        
        self.root.mainloop()
        
    def show_message(self):
        """
        print(self.check_state.get())
        # .get() will get the state of the checkbox
        """
        
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END)) # THIS WILL PRINT THE CONTENT OF THE TEXTBOX
            # using .get() is to provide a start and an end with 2 index
            # first index is a string (1.0 to start in the beggining)
            # second index is tk.END to get everything to the end
            
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
MyGUI() # CALLS THE CLASS
        
