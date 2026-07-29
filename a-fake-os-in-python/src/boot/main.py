import tkinter as tk
# boot stuff :0
def boot():
    boot = tk.Tk() # so the app is boot :)
    boot.title("A Simple OS: T5DW") #title
    boot.geometry("400x300") # size
    boot.configure(bg="black") # change bg to black
    #water mark might remove idk
    water_mark = tk.Label(boot, text="WYOS PRE ALPHA V 0.1", font=("Arial", 10), fg="White", bg="black")
    water_mark.pack(pady=10, padx=20, anchor="w")
    text1 = tk.Label(boot, text="Type Your UserName Here:", font=("Arial", 10), fg="White", bg="black")
    # reduced padx/pady so it fits 
    text1.pack(pady=10, padx=20, anchor="w")
    # username stuff
    login_main = tk.Text(boot, width=20, height=1, bg="White")
    login_main.insert("1.0", "")  # Inserts text correctly 
    login_main.pack(pady=10, padx=20, anchor="w")
    # password stuff
    text2 = tk.Label(boot, text="Type Your Password Here", font=("Arial", 10), fg="White", bg="black")
    text2.pack(pady=10,padx=20,anchor="w")
    pass_main = tk.Text(boot,width=20,height=1,bg="White")
    pass_main.insert("1.0", "") # Inserts text correctly 
    pass_main.pack(pady=10,padx=20,anchor="w")
    boot.mainloop()
boot()
