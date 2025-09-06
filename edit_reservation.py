## تعديل وحذف الحجوات


import tkinter as tk
from tkinter import messagebox
import database

class EditReservationPage:
    def __init__(self, root, reservation_id, name, flight_number, departure, destination, date, seat_number):
        self.root = root
        self.frame = tk.Frame(self.root, bg="#f0f8ff")
        self.frame.pack(fill="both", expand=True)
        self.reservation_id = reservation_id

        form_frame = tk.Frame(self.frame, bg="#f0f8ff")
        form_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            form_frame,
            text="✏️ Edit Reservation",
            font=("Arial", 20, "bold"),
            fg="#800080",
            bg="#f0f8ff"
        ).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.create_label_entry(form_frame, "Name:", name, 1)
        self.create_label_entry(form_frame, "Flight Number:", flight_number, 2)
        self.create_label_entry(form_frame, "Departure:", departure, 3)
        self.create_label_entry(form_frame, "Destination:", destination, 4)
        self.create_label_entry(form_frame, "Date:", date, 5)
        self.create_label_entry(form_frame, "Seat Number:", seat_number, 6)

        btn_frame = tk.Frame(form_frame, bg="#f0f8ff")
        btn_frame.grid(row=7, column=0, columnspan=2, pady=20)

        tk.Button(
            btn_frame,
            text="✔ Update",
            bg="#4caf50",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
            height=2,
            bd=0,
            relief="solid",
            activebackground="#388e3c",
            command=self.update_reservation
        ).pack(side="left", padx=10)

        tk.Button(
            btn_frame,
            text="⬅ Back",
            bg="#6ab2ff",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
            height=2,
            bd=0,
            relief="solid",
            activebackground="#4a90e2",
            command=self.go_back
        ).pack(side="left", padx=10)

    def create_label_entry(self, parent, label_text, initial_value, row):
        label = tk.Label(parent, text=label_text, bg="#f0f8ff", fg="#333", font=("Arial", 12, "bold"))
        label.grid(row=row, column=0, sticky="e", padx=(10, 10), pady=5)

        entry = tk.Entry(parent, font=("Arial", 12), width=30)
        entry.insert(0, initial_value)
        entry.grid(row=row, column=1, padx=(0, 10), pady=5)

        setattr(self, f"{label_text.lower().replace(' ', '_').replace(':', '')}_entry", entry)

    def update_reservation(self):
        name = self.name_entry.get()
        flight_number = self.flight_number_entry.get()
        departure = self.departure_entry.get()
        destination = self.destination_entry.get()
        date = self.date_entry.get()
        seat_number = self.seat_number_entry.get()

        if all([name, flight_number, departure, destination, date, seat_number]):
            database.update_reservation(self.reservation_id, name, flight_number, departure, destination, date, seat_number)
            messagebox.showinfo("Success", "Reservation updated!")
            self.go_back()
        else:
            messagebox.showerror("Error", "Please fill all fields")

    def go_back(self):
        self.frame.destroy()
        import reservations
        reservations.ReservationsPage(self.root)
