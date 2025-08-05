import tkinter as tk
from datetime import datetime
import pytz

# List of time zones to display
TIME_ZONES = [
    ("UTC", "UTC"),
    ("New York", "America/New_York"),
    ("London", "Europe/London"),
    ("Paris", "Europe/Paris"),
    ("Tokyo", "Asia/Tokyo"),
    ("Sydney", "Australia/Sydney"),
]

class DigitalClock(tk.Tk):
    def __init__(self, zones):
        super().__init__()
        self.title("Multi Time Zone Digital Clock")
        self.zones = zones
        self.labels = []
        for idx, (label, tz) in enumerate(self.zones):
            tk.Label(self, text=label, font=("Arial", 14, "bold")).grid(row=idx, column=0, padx=10, pady=5)
            time_label = tk.Label(self, font=("Arial", 16))
            time_label.grid(row=idx, column=1, padx=10, pady=5)
            self.labels.append((tz, time_label))
        self.update_clock()

    def update_clock(self):
        for tz, lbl in self.labels:
            now = datetime.now(pytz.timezone(tz))
            lbl.config(text=now.strftime("%H:%M:%S"))
        self.after(1000, self.update_clock)

if __name__ == "__main__":
    try:
        import pytz
    except ImportError:
        print("Please install pytz: pip install pytz")
        exit(1)

    app = DigitalClock(TIME_ZONES)
    app.mainloop()