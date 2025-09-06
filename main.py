## بيشتغل ك entry point بين الصفحات ويدير التنقل

import tkinter as tk
from tkinter import ttk
import home

def main():

    print("\nStarting the application...\n\n")

    root = tk.Tk()
    root.title("Flight Reservation System")
    root.geometry("800x600")
    #root.iconbitmap("icon.ico")
    # import os
    # root.iconbitmap(os.path.join(os.path.dirname(__file__), "icon.ico"))
    app = home.HomePage(root)
    root.mainloop()

if __name__ == "__main__":
    main()