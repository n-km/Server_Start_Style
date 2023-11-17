import tkinter as tk
import tkinter.ttk as ttk
import sys

# Dunkler Modus
dark_mode = False

def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    update_mode()

def update_mode():
    if dark_mode:
        root.configure(bg='#333333')  # Hintergrundfarbe ändern
        style.configure("TButton", background='#666666', foreground='black')  # Button-Stil ändern
        console_output.config(bg='#666666', fg='white')  # Textwidget-Stil ändern
    else:
        root.configure(bg='white')  # Hintergrundfarbe zurücksetzen
        style.configure("TButton", background='light gray', foreground='black')  # Button-Stil zurücksetzen
        console_output.config(bg='white', fg='black')  # Textwidget-Stil zurücksetzen

def zeige_nachricht():
    nachricht = "The Server is currently off."
    print(nachricht)
    root.title('🔴-Server off')

def aendere_titel():
    nachricht = "The Server is currently on."
    print(nachricht)
    root.title('🟢-Server on')

def exit():
    root.destroy()

root = tk.Tk()
root.title("🔴-Server off")

# Stil für die runden Buttons
style = ttk.Style()
style.configure("TButton", padding=(10, 5), font=("Arial", 12))  # Schriftart auf Arial ändern

button2 = ttk.Button(root, text="🟢 Start Server", command=aendere_titel, style="TButton")
button2.pack(pady=10)

button1 = ttk.Button(root, text="🔴 Shutdown Server", command=zeige_nachricht, style="TButton")
button1.pack(pady=10)

button3 = ttk.Button(root, text="Exit Program", command=exit, style="TButton")
button3.pack(pady=10)

mode_button = ttk.Button(root, text="Toggle Mode", command=toggle_mode, style="TButton")
mode_button.pack(padx=0, pady=0, anchor='nw')  # 'nw' steht für die obere linke Ecke

console_output = tk.Text(root, height=10, width=40)
console_output.pack()
console_output.config(state=tk.DISABLED, font=("Arial", 12))  # Schriftart im Textwidget auf Arial ändern

update_mode()  # Setzen Sie den Modus zu Beginn auf den Standardmodus

class ConsoleRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, text)
        self.text_widget.config(state=tk.DISABLED)

sys.stdout = ConsoleRedirector(console_output)

root.mainloop()
