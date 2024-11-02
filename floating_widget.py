import tkinter as tk
from tkinter import ttk
from datetime import datetime
import calendar

class FloatingClockWidget:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # Remove window borders
        self.root.attributes("-topmost", True)  # Keep on top
        self.root.attributes("-alpha", 0.9)  # Transparency level

        # Set window background color for a modern feel
        self.root.configure(bg="#2E2E2E")

        # Layout configuration
        self.create_widgets()
        self.update_time()
        
        # Enable dragging
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.on_move)
        
    def create_widgets(self):
        # Frame for date and time
        self.time_frame = tk.Frame(self.root, bg="#2E2E2E")
        self.time_frame.pack(padx=10, pady=10)

        # Clock label
        self.time_label = tk.Label(
            self.time_frame, font=("Helvetica", 18, "bold"), bg="#2E2E2E", fg="white"
        )
        self.time_label.pack()

        # Date label
        self.date_label = tk.Label(
            self.time_frame, font=("Helvetica", 14), bg="#2E2E2E", fg="light gray"
        )
        self.date_label.pack()

        # Calendar
        self.calendar_label = tk.Label(
            self.root, font=("Courier", 10), justify=tk.LEFT, bg="#2E2E2E", fg="white"
        )
        self.calendar_label.pack(pady=10)

        # Update calendar for the current month
        self.update_calendar()

    def update_time(self):
        # Update time and date
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.root.after(1000, self.update_time)  # Update every second

    def update_calendar(self):
        # Display the current month's calendar
        month_calendar = calendar.month(datetime.now().year, datetime.now().month)
        self.calendar_label.config(text=month_calendar)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        x = self.root.winfo_pointerx() - self.x
        y = self.root.winfo_pointery() - self.y
        self.root.geometry(f"+{x}+{y}")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    widget = FloatingClockWidget(root)
    root.mainloop()
