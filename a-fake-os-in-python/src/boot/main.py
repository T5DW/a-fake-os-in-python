import tkinter as tk
# boot stuff :0
def boot():
          boot = tk.Tk() # so the app is boot :)
          boot.title("A Simple OS: T5DW") #title
          boot.geometry("400x300") # size
          boot.configure(bg="black") # change bg to black
          water_mark = tk.Label(boot, text = "WYOS PRE ALPHA V 0.1", font=("Arial", 10, ), fg="White", bg = "black" )
          water_mark.pack(pady=10, padx=20, anchor = "w")
          
          
          
          
          boot.mainloop()
          
boot()          