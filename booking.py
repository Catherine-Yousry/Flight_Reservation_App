## نموذج حجز الرحلة


import tkinter as tk
from tkinter import messagebox
import database

class BookingPage:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg="#d5e9ff")
        self.frame.pack(fill="both", expand=True)

        content_frame = tk.Frame(self.frame, bg="#d5e9ff")
        content_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            content_frame,
            text="✈️  Book a Flight",
            font=("Arial", 22, "bold"),
            bg="#d5e9ff",
            fg="#134273"
        ).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.create_label_entry(content_frame, "Name:", 1)
        self.create_label_entry(content_frame, "Flight Number:", 2)
        self.create_label_entry(content_frame, "Departure:", 3)
        self.create_label_entry(content_frame, "Destination:", 4)
        self.create_label_entry(content_frame, "Date:", 5)
        self.create_label_entry(content_frame, "Seat Number:", 6)

        button_frame = tk.Frame(content_frame, bg="#d5e9ff")
        button_frame.grid(row=7, column=0, columnspan=2, pady=20)

        submit_btn = tk.Button(
            button_frame,
            text="Submit",
            bg="#4da6ff",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
            height=2,
            activebackground="#3399ff",
            activeforeground="white",
            bd=0,
            relief="solid",
            command=self.book_flight
        )
        submit_btn.pack(side="left", padx=10)

        back_btn = tk.Button(
            button_frame,
            text="Back",
            bg="#ff6666",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
            height=2,
            activebackground="#cc3333",
            activeforeground="white",
            bd=0,
            relief="solid",
            command=self.go_back
        )
        back_btn.pack(side="left", padx=10)

    def create_label_entry(self, parent, label_text, row):
        label = tk.Label(parent, text=label_text, bg="#d5e9ff", fg="#336699", font=("Arial", 12, "bold"))
        label.grid(row=row, column=0, sticky="e", padx=(10, 10), pady=5)

        entry = tk.Entry(parent, font=("Arial", 12), width=30)
        entry.grid(row=row, column=1, padx=(0, 10), pady=5)

        setattr(self, f"{label_text.lower().replace(' ', '_').replace(':', '')}_entry", entry)

    def book_flight(self):
        name = self.name_entry.get()
        flight_number = self.flight_number_entry.get()
        departure = self.departure_entry.get()
        destination = self.destination_entry.get()
        date = self.date_entry.get()
        seat_number = self.seat_number_entry.get()

        if all([name, flight_number, departure, destination, date, seat_number]):
            database.add_reservation(name, flight_number, departure, destination, date, seat_number)
            messagebox.showinfo("Success", "Flight booked successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill all fields")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.flight_number_entry.delete(0, tk.END)
        self.departure_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.seat_number_entry.delete(0, tk.END)

    def go_back(self):
        self.frame.destroy()
        import home
        home.HomePage(self.root)
