from tkinter import *
from tkinter import ttk
import datetime
import calendar

class HabitTracker:
    def __init__(self, master):
        self.master = master
        master.title("Trackzilla: An Habit Tracker")
        master.geometry("420x740")  
        master.resizable(False, False)  

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(".", background="#f0f0f0")
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", foreground="#444")
        style.configure("TEntry", fieldbackground="#fff", foreground="#444")
        style.configure("TButton", background="#4CAF50", foreground="white")

        self.main_frame = ttk.Frame(master, style="TFrame")
        self.main_frame.pack(fill=BOTH, expand=True)

        self.header_frame = ttk.Frame(self.main_frame, style="TFrame")
        self.header_frame.pack(fill=X, pady=10)

        self.habit_label = ttk.Label(self.header_frame, text="Add New Habit:", font=("Arial", 14, "bold"))
        self.habit_label.pack(anchor="center")

        self.new_habit_entry = ttk.Entry(self.header_frame, width=25, font=("Arial", 12))
        self.new_habit_entry.pack(pady=5)
        self.new_habit_entry.bind("<Return>", self.add_habit)

        self.add_habit_button = ttk.Button(self.header_frame, text="Add Habit", command=self.add_habit)
        self.add_habit_button.pack(pady=5)

        self.scrollable_frame = ttk.Frame(self.main_frame, style="TFrame")
        self.scrollable_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self.canvas = Canvas(self.scrollable_frame, bg="#f0f0f0", highlightthickness=0)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.scrollable_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.habit_frame = ttk.Frame(self.canvas, style="TFrame")
        self.canvas.create_window((0, 0), window=self.habit_frame, anchor="nw")

        self.habit_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.habits = []

        self.load_habits()
        self.update_habit_list()

    def add_habit(self, event=None):
        new_habit = self.new_habit_entry.get()
        if new_habit:
            self.habits.append({"name": new_habit, "streak": 0, "history": []})
            self.new_habit_entry.delete(0, END)
            self.save_habits()
            self.update_habit_list()

    def update_habit_list(self):
        for widget in self.habit_frame.winfo_children():
            widget.destroy()

        for habit in self.habits:
            habit_frame = ttk.Frame(self.habit_frame, borderwidth=1, relief="solid", style="TFrame")
            habit_frame.pack(pady=5, fill="x")

            habit_name_label = ttk.Label(habit_frame, text=habit["name"], font=("Arial", 12, "bold"))
            habit_name_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

            done_button = ttk.Button(
                habit_frame,
                text="Done",
                command=lambda h=habit: self.mark_done(h)
            )
            done_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

            delete_button = ttk.Button(
                habit_frame,
                text="Delete",
                command=lambda h=habit: self.delete_habit(h)
            )
            delete_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")

            calendar_frame = ttk.Frame(habit_frame)
            calendar_frame.grid(row=1, column=1, rowspan=2, padx=10, pady=5, sticky="nsew")
            self.create_calendar_grid(calendar_frame, habit)

    def create_calendar_grid(self, frame, habit):
        today = datetime.date.today()
        current_month = today.month
        current_year = today.year
        month_name = calendar.month_name[current_month]

        month_label = ttk.Label(frame, text=month_name, font=("Arial", 10, "bold"))
        month_label.pack(side=TOP)

        cal = calendar.monthcalendar(current_year, current_month)

        day_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        day_row = Frame(frame)
        day_row.pack(side=TOP, fill=X)
        for day_name in day_names:
            day_label = Label(day_row, width=3, text=day_name, relief=RAISED, font=("Arial", 8)) 
            day_label.pack(side=LEFT)

        for week in cal:
            row = Frame(frame)
            row.pack(side=TOP, fill=X)
            for day in week:
                if day == 0:
                    label = Label(row, width=3, text=" ", relief=RAISED)
                else:
                    date = datetime.date(current_year, current_month, day)
                    date_str = date.strftime("%Y-%m-%d")
                    bg_color = "white"
                    if date_str in habit["history"]:
                        bg_color = "lightgreen" 
                    label = Label(row, width=3, text=str(day), relief=RAISED, bg=bg_color)
                label.pack(side=LEFT)

    def mark_done(self, habit):
        today = datetime.date.today().strftime("%Y-%m-%d")
        if today not in habit["history"]:
            habit["streak"] += 1
            habit["history"].append(today)

        self.save_habits()
        self.update_habit_list()

    def delete_habit(self, habit):
        if habit in self.habits:
            self.habits.remove(habit)
            self.save_habits()
            self.update_habit_list()

    def load_habits(self):
        try:
            with open("habits.txt", "r") as f:
                self.habits = eval(f.read())
        except FileNotFoundError:
            pass

    def save_habits(self):
        with open("habits.txt", "w") as f:
            f.write(str(self.habits))

if __name__ == "__main__":
    root = Tk()
    app = HabitTracker(root)
    root.mainloop()
