import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import sys

from parser import read_log_file
from analyzer import LogAnalyzer
from reporter import format_report


# -----------------------
# FIX FOR PYINSTALLER
# -----------------------

def resource_path(relative_path):
    """Get path for dev and PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class LogSenseGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("LogSense")
        self.root.geometry("1200x750")
        self.root.configure(bg="#0f172a")

        self.logs = {}

        # window icon
        icon_path = resource_path("assets/logsense.ico")
        try:
            self.root.iconbitmap(icon_path)
        except:
            pass

        self.build_layout()


    def build_layout(self):

        self.create_topbar()
        self.create_body()

    # -----------------------
    # TOP BAR
    # -----------------------

    def create_topbar(self):

        topbar = tk.Frame(self.root, bg="#020617", height=60)
        topbar.pack(fill="x")

        logo_path = resource_path("assets/logo.png")

        logo_img = Image.open(logo_path)
        logo_img = logo_img.resize((38, 38))

        self.logo = ImageTk.PhotoImage(logo_img)

        logo = tk.Label(topbar, image=self.logo, bg="#020617")
        logo.pack(side="left", padx=15)

        title = tk.Label(
            topbar,
            text="LogSense",
            fg="white",
            bg="#020617",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(side="left")

        open_btn = tk.Button(
            topbar,
            text="Open Log",
            command=self.open_file,
            bg="#6366f1",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=14,
            pady=6
        )

        open_btn.pack(side="right", padx=10)

        manual_btn = tk.Button(
            topbar,
            text="Manual",
            command=self.show_manual,
            bg="#334155",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=14,
            pady=6
        )

        manual_btn.pack(side="right")

    # -----------------------
    # BODY LAYOUT
    # -----------------------

    def create_body(self):

        body = tk.Frame(self.root, bg="#0f172a")
        body.pack(fill="both", expand=True)

        sidebar = tk.Frame(body, bg="#020617", width=260)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        label = tk.Label(
            sidebar,
            text="Logs",
            fg="white",
            bg="#020617",
            font=("Segoe UI", 12, "bold")
        )

        label.pack(pady=15)

        self.log_list = tk.Listbox(
            sidebar,
            bg="#020617",
            fg="#cbd5f5",
            highlightthickness=0,
            borderwidth=0,
            font=("Segoe UI", 10)
        )

        self.log_list.pack(fill="both", expand=True, padx=15)

        self.log_list.bind("<<ListboxSelect>>", self.switch_log)

        self.content = tk.Frame(body, bg="#0f172a")
        self.content.pack(side="right", fill="both", expand=True)

        self.show_welcome()

    # -----------------------
    # WELCOME SCREEN
    # -----------------------

    def show_welcome(self):

        for widget in self.content.winfo_children():
            widget.destroy()

        welcome = tk.Frame(self.content, bg="#0f172a")
        welcome.pack(expand=True)

        logo_path = resource_path("assets/logo.png")

        logo_img = Image.open(logo_path)
        logo_img = logo_img.resize((120, 120))

        self.big_logo = ImageTk.PhotoImage(logo_img)

        logo = tk.Label(welcome, image=self.big_logo, bg="#0f172a")
        logo.pack(pady=20)

        title = tk.Label(
            welcome,
            text="Welcome to LogSense",
            fg="white",
            bg="#0f172a",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(pady=10)

        subtitle = tk.Label(
            welcome,
            text="Intelligent log analysis for developers",
            fg="#94a3b8",
            bg="#0f172a",
            font=("Segoe UI", 13)
        )

        subtitle.pack(pady=5)

        instructions = tk.Label(
            welcome,
            text="Open a log file to begin analyzing errors and incidents.",
            fg="#64748b",
            bg="#0f172a",
            font=("Segoe UI", 11)
        )

        instructions.pack(pady=10)

    # -----------------------
    # MANUAL SCREEN
    # -----------------------

    def show_manual(self):

        for widget in self.content.winfo_children():
            widget.destroy()

        manual = tk.Frame(self.content, bg="#0f172a")
        manual.pack(fill="both", expand=True)

        title = tk.Label(
            manual,
            text="LogSense Manual",
            fg="white",
            bg="#0f172a",
            font=("Segoe UI", 26, "bold")
        )

        title.pack(pady=20)

        text = tk.Text(
            manual,
            bg="#020617",
            fg="#e2e8f0",
            font=("Segoe UI", 11),
            borderwidth=0,
            padx=20,
            pady=20
        )

        text.pack(fill="both", expand=True, padx=40, pady=20)

        manual_content = """

Welcome to LogSense

LogSense helps developers analyze large log files and quickly identify system failures.

------------------------------------------------------------

1. Opening Logs

Click the "Open Log" button in the top bar.
Select a .log or .txt file.

The file will appear in the Logs explorer on the left.

------------------------------------------------------------

2. Analyzing Logs

Click a log file in the sidebar.
LogSense will automatically analyze it.

------------------------------------------------------------

3. Understanding the Report

Root Cause Candidate
    The earliest detected error.

Timeline
    Shows the order errors occurred.

Top Issues
    Displays the most frequent errors.

------------------------------------------------------------

Supported Logs

ERROR
Exception
Traceback

Example:

2026-03-10 10:20:05 ERROR NullPointerException
"""

        text.insert(tk.END, manual_content)
        text.config(state="disabled")

        back_btn = tk.Button(
            manual,
            text="Back",
            command=self.show_welcome,
            bg="#6366f1",
            fg="white",
            relief="flat",
            padx=16,
            pady=8
        )

        back_btn.pack(pady=20)

    # -----------------------
    # OPEN FILE
    # -----------------------

    def open_file(self):

        path = filedialog.askopenfilename(
            filetypes=[("Log files", "*.log *.txt")]
        )

        if not path:
            return

        name = os.path.basename(path)

        self.logs[name] = path

        self.log_list.insert(tk.END, name)

    # -----------------------
    # SWITCH LOG
    # -----------------------

    def switch_log(self, event):

        selection = self.log_list.curselection()

        if not selection:
            return

        name = self.log_list.get(selection[0])

        path = self.logs[name]

        self.show_report(path)

    # -----------------------
    # SHOW REPORT
    # -----------------------

    def show_report(self, path):

        for widget in self.content.winfo_children():
            widget.destroy()

        analyzer = LogAnalyzer()

        for line in read_log_file(path):
            analyzer.process_line(line)

        results = analyzer.get_results()

        report = format_report(results)

        panel = tk.Frame(self.content, bg="#020617")
        panel.pack(fill="both", expand=True, padx=20, pady=20)

        text = tk.Text(
            panel,
            bg="#020617",
            fg="#e2e8f0",
            font=("Consolas", 11),
            borderwidth=0,
            insertbackground="white"
        )

        text.pack(fill="both", expand=True, padx=15, pady=15)

        text.insert(tk.END, report)
        text.config(state="disabled")


def start_gui():

    root = tk.Tk()

    app = LogSenseGUI(root)

    root.mainloop()