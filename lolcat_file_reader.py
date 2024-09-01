import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def run_with_lolcat(python_interpreter, file_path):
    # Ensure the file exists
    if not os.path.isfile(file_path):
        messagebox.showerror("Error", f"The file '{file_path}' does not exist.")
        return

    # Run the Python file using the selected interpreter and pipe the output through lolcat
    command = f"{python_interpreter} {file_path} | lolcat"
    subprocess.run(command, shell=True)

def browse_file():
    file_path = filedialog.askopenfilename(title="Select Python File", filetypes=[("Python Files", "*.py")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def browse_directory():
    directory_path = filedialog.askdirectory(title="Select Directory")
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory_path)

def execute():
    python_interpreter = interpreter_entry.get()
    file_path = file_entry.get()
    run_with_lolcat(python_interpreter, file_path)

# Create the main window
root = tk.Tk()
root.title("Python Lolcat Runner")

# Python interpreter selection
tk.Label(root, text="Python Interpreter:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
interpreter_entry = tk.Entry(root)
interpreter_entry.grid(row=0, column=1, padx=10, pady=5)

# File selection
tk.Label(root, text="Python File:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
file_entry = tk.Entry(root)
file_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_file).grid(row=1, column=2, padx=10, pady=5)

# Directory for placing files
tk.Label(root, text="Place Files Here:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
directory_entry = tk.Entry(root)
directory_entry.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_directory).grid(row=2, column=2, padx=10, pady=5)

# Run button
tk.Button(root, text="Run with Lolcat", command=execute).grid(row=3, column=1, padx=10, pady=20)

# Start the GUI loop
root.mainloop()

