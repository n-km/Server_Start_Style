import tkinter as tk
import subprocess

def open_explorer():
    drive_letter = "C:"  # Ändere dies auf den gewünschten Laufwerksbuchstaben
    subprocess.Popen(['explorer', drive_letter])

# Hauptfenster erstellen
root = tk.Tk()
root.title("Fast_Ex")

# Button erstellen
button = tk.Button(root, text="Open Explorer", command=open_explorer, pady=10)
button.pack(pady=40, padx=70)

# Hauptloop starten
root.mainloop()
