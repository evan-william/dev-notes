import tkinter as tk

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
        print("Hello, World") 
        
MyGUI() # CALLS THE CLASS
        