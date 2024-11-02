import tkinter as tk
from tkinter import ttk, colorchooser
from datetime import datetime
import calendar
import pytz

class FloatingClockWidget:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # Remove window borders
        self.root.attributes("-topmost", True)  # Keep on top
        self.root.attributes("-alpha", 0.9)  # Default transparency level

        # Initial background color
        self.bg_color = "#2E2E2E"
        self.root.configure(bg=self.bg_color)

        # Time zone for the selected country
        self.selected_timezone = pytz.timezone('UTC')  # Default time zone

        # Layout configuration
        self.create_widgets()
        self.update_time()

        # Enable dragging
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.on_move)

        # Center the widget on the screen initially
        self.center_window()

    def create_widgets(self):
        # Frame for date and time
        self.time_frame = tk.Frame(self.root, bg=self.bg_color)
        self.time_frame.pack(padx=10, pady=10)

        # Local Clock label
        self.local_time_label = tk.Label(
            self.time_frame, font=("Helvetica", 18, "bold"), bg=self.bg_color, fg="white"
        )
        self.local_time_label.pack()

        # Selected Time Zone Clock label
        self.tz_time_label = tk.Label(
            self.time_frame, font=("Helvetica", 18, "bold"), bg=self.bg_color, fg="light blue"
        )
        self.tz_time_label.pack()

        # Date label
        self.date_label = tk.Label(
            self.time_frame, font=("Helvetica", 14), bg=self.bg_color, fg="light gray"
        )
        self.date_label.pack()

        # Calendar
        self.calendar_label = tk.Label(
            self.root, font=("Courier", 10), justify=tk.LEFT, bg=self.bg_color, fg="white"
        )
        self.calendar_label.pack(pady=10)

        # Transparency slider
        self.transparency_slider = tk.Scale(
            self.root, from_=0.1, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, label="Transparency",
            command=self.update_transparency, bg=self.bg_color, fg="white"
        )
        self.transparency_slider.set(0.9)  # Default value
        self.transparency_slider.pack(pady=(0, 10))

        # Color selector button
        self.color_button = tk.Button(
            self.root, text="Change Color", command=self.change_color, bg="light gray"
        )
        self.color_button.pack(pady=(0, 10))

        # Time Zone selector
        self.tz_label = tk.Label(self.root, text="Select Time Zone:", bg=self.bg_color, fg="white")
        self.tz_label.pack()
        self.timezone_combo = ttk.Combobox(
            self.root, values=pytz.all_timezones, width=30, state="readonly"
        )
        self.timezone_combo.pack(pady=(0, 10))
        self.timezone_combo.bind("<<ComboboxSelected>>", self.change_timezone)

        # Close button
        self.close_button = tk.Button(
            self.root, text="Close", command=self.root.quit, bg="red", fg="white"
        )
        self.close_button.pack(pady=(0, 10))

        # Update calendar for the current month
        self.update_calendar()

    def update_time(self):
        # Update local time and date
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")
        self.local_time_label.config(text=f"Local Time: {current_time}")
        self.date_label.config(text=current_date)

        # Update selected time zone time
        tz_time = datetime.now(self.selected_timezone).strftime("%H:%M:%S")
        self.tz_time_label.config(text=f"{self.selected_timezone}: {tz_time}")

        # Refresh every second
        self.root.after(1000, self.update_time)

    def update_calendar(self):
        # Display the current month's calendar
        month_calendar = calendar.month(datetime.now().year, datetime.now().month)
        self.calendar_label.config(text=month_calendar)

    def update_transparency(self, value):
        # Adjust the transparency level of the widget
        self.root.attributes("-alpha", float(value))

    def change_color(self):
        # Open color chooser and update background color
        color_code = colorchooser.askcolor(title="Choose Background Color")[1]
        if color_code:
            self.bg_color = color_code
            self.root.configure(bg=self.bg_color)
            self.time_frame.configure(bg=self.bg_color)
            self.local_time_label.configure(bg=self.bg_color)
            self.tz_time_label.configure(bg=self.bg_color)
            self.date_label.configure(bg=self.bg_color)
            self.calendar_label.configure(bg=self.bg_color)
            self.transparency_slider.configure(bg=self.bg_color)
            self.tz_label.configure(bg=self.bg_color)

    def change_timezone(self, event):
        # Change the selected time zone based on dropdown selection
        selected_tz = self.timezone_combo.get()
        if selected_tz:
            self.selected_timezone = pytz.timezone(selected_tz)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        # Calculate new position based on mouse movement
        x = self.root.winfo_x() + event.x - self.x
        y = self.root.winfo_y() + event.y - self.y
        self.root.geometry(f"+{x}+{y}")

    def center_window(self):
        # Center the widget on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"+{x}+{y}")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    widget = FloatingClockWidget(root)
    root.mainloop()
