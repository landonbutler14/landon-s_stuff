#This will be a cookie clicker style game where the user can accumulate points by clicking a button. (AI Wrote this one lol)
import time
import random
import sys
import os
import json
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

class JabbaTheHuttGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jabba the Hutt Game")
        self.points = 0
        self.click_value = 1
        self.upgrades = {
            "Small Upgrade": {"cost": 10, "value": 1},
            "Medium Upgrade": {"cost": 50, "value": 5},
            "Large Upgrade": {"cost": 200, "value": 20}
        }
        self.auto_clickers = {
            "Small Auto-Clicker": {"cost": 100, "value": 1},
            "Medium Auto-Clicker": {"cost": 500, "value": 5},
            "Large Auto-Clicker": {"cost": 2000, "value": 20}
        }
        self.auto_clicker_threads = []
        self.create_widgets()
        self.update_points_label()

    def create_widgets(self):
        self.points_label = tk.Label(self.master, text="Points: 0", font=("Helvetica", 16))
        self.points_label.pack(pady=10)

        self.click_button = tk.Button(self.master, text="Click Me!", command=self.click)
        self.click_button.pack(pady=10)

        self.upgrade_frame = tk.Frame(self.master)
        self.upgrade_frame.pack(pady=10)
        tk.Label(self.upgrade_frame, text="Upgrades:", font=("Helvetica", 14)).pack()
        for upgrade in self.upgrades:
            btn = tk.Button(self.upgrade_frame, text=f"{upgrade} (Cost: {self.upgrades[upgrade]['cost']})", 
                            command=lambda u=upgrade: self.buy_upgrade(u))
            btn.pack(pady=2)

        self.auto_clicker_frame = tk.Frame(self.master)
        self.auto_clicker_frame.pack(pady=10)
        tk.Label(self.auto_clicker_frame, text="Auto-Clickers:", font=("Helvetica", 14)).pack()
        for auto_clicker in self.auto_clickers:
            btn = tk.Button(self.auto_clicker_frame, text=f"{auto_clicker} (Cost: {self.auto_clickers[auto_clicker]['cost']})", 
                            command=lambda ac=auto_clicker: self.buy_auto_clicker(ac))
            btn.pack(pady=2)

        self.save_button = tk.Button(self.master, text="Save Game", command=self.save_game)
        self.save_button.pack(pady=5)
        self.load_button = tk.Button(self.master, text="Load Game", command=self.load_game)
        self.load_button.pack(pady=5)
        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(pady=5)
    def click(self):
        self.points += self.click_value
        self.update_points_label()
    def buy_upgrade(self, upgrade):
        if self.points >= self.upgrades[upgrade]["cost"]:
            self.points -= self.upgrades[upgrade]["cost"]
            self.click_value += self.upgrades[upgrade]["value"]
            self.update_points_label()
        else:
            messagebox.showinfo("Insufficient Points", "You don't have enough points to buy this upgrade.")
    def buy_auto_clicker(self, auto_clicker):
        if self.points >= self.auto_clickers[auto_clicker]["cost"]:
            self.points -= self.auto_clickers[auto_clicker]["cost"]
            thread = threading.Thread(target=self.auto_clicker_worker, args=(self.auto_clickers[auto_clicker]["value"],))
            thread.daemon = True
            thread.start()
            self.auto_clicker_threads.append(thread)
            self.update_points_label()
        else:
            messagebox.showinfo("Insufficient Points", "You don't have enough points to buy this auto-clicker.")
    def auto_clicker_worker(self, value):
        while True:
            time.sleep(1)
            self.points += value
            self.update_points_label()
    def update_points_label(self):
        self.points_label.config(text=f"Points: {self.points}")
    def save_game(self):
        save_data = {
            "points": self.points,
            "click_value": self.click_value
        }
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(save_data, f)
            messagebox.showinfo("Game Saved", "Your game has been saved successfully.")
    def load_game(self):
        file_path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as f:
                save_data = json.load(f)
                self.points = save_data.get("points", 0)
                self.click_value = save_data.get("click_value", 1)
                self.update_points_label()
            messagebox.showinfo("Game Loaded", "Your game has been loaded successfully.")
if __name__ == "__main__":
    root = tk.Tk()
    game = JabbaTheHuttGame(root)
    root.mainloop()


    
