## عرض قائمة الحجوزات


import tkinter as tk
from tkinter import ttk, messagebox
import database
import edit_reservation

class ReservationsPage:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg="#f0f8ff")
        self.frame.pack(fill="both", expand=True)

        tk.Label(
            self.frame,
            text="🧾 Your Reservations",
            font=("Arial", 20, "bold"),
            fg="#134273",
            bg="#f0f8ff"
        ).pack(pady=(20, 10))

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 11), rowheight=30)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

        self.tree = ttk.Treeview(
            self.frame,
            columns=("ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat"),
            show="headings",
            height=10
        )
        columns = {
            "ID": 40, "Name": 120, "Flight": 100, "Departure": 100,
            "Destination": 100, "Date": 100, "Seat": 80
        }

        for col, width in columns.items():
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")

        self.tree.pack(pady=10, padx=20)

        self.load_reservations()

        self.tree.bind("<Double-1>", self.on_double_click)

        btn_frame = tk.Frame(self.frame, bg="#f0f8ff")
        btn_frame.pack(pady=20)

        tk.Button(
            btn_frame, text="🔄 Refresh", bg="#4da6ff", fg="white", font=("Arial", 11, "bold"),
            width=15, height=2, bd=0, relief="solid",
            activebackground="#3399ff", command=self.load_reservations
        ).pack(side="left", padx=10)

        tk.Button(
            btn_frame, text="🗑 Delete Selected", bg="#ff4d4d", fg="white", font=("Arial", 11, "bold"),
            width=18, height=2, bd=0, relief="solid",
            activebackground="#cc0000", command=self.delete_selected
        ).pack(side="left", padx=10)

        tk.Button(
            btn_frame, text="⬅ Back", bg="#6ab2ff", fg="white", font=("Arial", 11, "bold"),
            width=12, height=2, bd=0, relief="solid",
            activebackground="#4a90e2", command=self.go_back
        ).pack(side="left", padx=10)

    def load_reservations(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        reservations = database.get_all_reservations()

        for res in reservations:
            self.tree.insert("", tk.END, values=res)

    def on_double_click(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item[0], 'values')
            self.frame.destroy()
            edit_reservation.EditReservationPage(self.root, *values)

    def delete_selected(self):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item[0], 'values')
            res_id = values[0]
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?")
            if confirm:
                database.delete_reservation(res_id)
                self.load_reservations()
        else:
            messagebox.showwarning("No Selection", "Please select a reservation to delete.")

    def go_back(self):
        self.frame.destroy()
        import home
        home.HomePage(self.root)

