## واجهة الصفحة الرئيسية


import tkinter as tk
from tkinter import ttk
import booking
import reservations

class HomePage:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg="#d5e9ff")
        self.frame.pack(fill="both", expand=True)

        center_frame = tk.Frame(self.frame, bg="#d5e9ff")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            center_frame,
            text="✈️ Flight Reservation System",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#6ab2ff",
            pady=10,
            padx=30
        ).pack(pady=(0, 30), fill="x")

        tk.Button(
            center_frame,
            text="Book Flight",
            bg="#4da6ff",
            fg="white",
            font=("Arial", 12, "bold"),
            width=25,
            height=2,
            activebackground="#3399ff",
            activeforeground="white",
            bd=0,
            relief="solid",
            command=self.open_booking
        ).pack(pady=10)

        tk.Button(
            center_frame,
            text="View Reservations",
            bg="#4da6ff",
            fg="white",
            font=("Arial", 12, "bold"),
            width=25,
            height=2,
            activebackground="#3399ff",
            activeforeground="white",
            bd=0,
            relief="solid",
            command=self.open_reservations
        ).pack(pady=10)

        tk.Button(
            center_frame,
            text="Exit",
            bg="#ff4d4d",
            fg="white",
            font=("Arial", 12, "bold"),
            width=25,
            height=2,
            activebackground="#cc0000",
            activeforeground="white",
            bd=0,
            relief="solid",
            command=self.root.quit
        ).pack(pady=10)

    def open_booking(self):
        self.frame.destroy()
        booking.BookingPage(self.root)

    def open_reservations(self):
        self.frame.destroy()
        reservations.ReservationsPage(self.root)
