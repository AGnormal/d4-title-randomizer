import tkinter as tk
from tkinter import ttk
import random

# Arrays for prefixes and suffixes
prefixes = ["Brave", "Mighty", "Fearless", "Cunning", "Wise"]
suffixes = ["the Bold", "the Swift", "the Just", "the Sly", "the Wise"]

# Function to pick a random prefix
def pick_prefix():
    prefix_var.set(random.choice(prefixes))

# Function to pick a random suffix
def pick_suffix():
    suffix_var.set(random.choice(suffixes))

# Initialize the main window
root = tk.Tk()
root.title("Title Generator")

# Character Name
tk.Label(root, text="Character Name:").grid(row=0, column=0, padx=10, pady=10)
name_var = tk.StringVar()
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=10)

# Prefix
tk.Label(root, text="Prefix:").grid(row=1, column=0, padx=10, pady=10)
prefix_var = tk.StringVar()
tk.Entry(root, textvariable=prefix_var).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Pick Prefix", command=pick_prefix).grid(row=1, column=2, padx=10, pady=10)

# Suffix
tk.Label(root, text="Suffix:").grid(row=2, column=0, padx=10, pady=10)
suffix_var = tk.StringVar()
tk.Entry(root, textvariable=suffix_var).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Pick Suffix", command=pick_suffix).grid(row=2, column=2, padx=10, pady=10)

# Run the application
root.mainloop()
