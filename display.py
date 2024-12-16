import tkinter as tk

# Function to read and display the first n lines of the text file
def display_first_lines(n):
    try:
        with open("results.txt", "r") as file:
            lines = file.readlines()
            first_n_lines = lines[2:8]  # Get the first n lines
            text_widget.delete(1.0, tk.END)
            text_widget.tag_configure("center", justify="center")
            for line in first_n_lines:
                text_widget.insert(tk.END, line, "center")
            text_widget.configure(bg="yellow",fg = "black")
    except FileNotFoundError:
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, "File 'results.txt' not found")

# Function to read and display the last n lines of the text file
def display_last_lines(n):
    try:
        with open("results.txt", "r") as file:
            lines = file.readlines()
            last_n_lines = lines[-n:]  # Get the last n lines
            text_widget.delete(1.0, tk.END)
            text_widget.tag_configure("center", justify="center")
            for line in last_n_lines:
                text_widget.insert(tk.END, line, "center")
            text_widget.configure(bg="red",fg = "black")
    except FileNotFoundError:
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, "File 'results.txt' not found")

# Function to read and display the lines from the 11th to the 6th lines from the end of the text file
def display_custom_lines():
    try:
        with open("results.txt", "r") as file:

            lines = file.readlines()
            # Get the lines from the 11th to the 6th lines from the end
            custom_lines = lines[-14:-8]
            text_widget.delete(1.0, tk.END)
            text_widget.tag_configure("center", justify="center")
            for line in custom_lines:
                text_widget.insert(tk.END, line, "center")
            text_widget.configure(bg="lightblue",fg = "black")
          
    except FileNotFoundError:
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, "File 'results.txt' not found")

# Create a tkinter window
root = tk.Tk()
root.title("Custom Lines Viewer")

# Create a text widget with center alignment
text_widget = tk.Text(root, wrap=tk.WORD, width=600, height=400, font=("Arial Black", 75))
text_widget.tag_configure("title", font=("Arial", 30))
text_widget.pack()

# Start the tkinter main loop
def fn_key_pressed(event):
    if event.keysym == "t" or event.keysym == "g" or event.keysym == "v" or event.keysym == "y" or event.keysym == "h" or event.keysym == "b" or event.keysym == "r" or event.keysym == "f" or event.keysym == "c" :
        # Simulate a click on the "D Results" button
        display_custom_lines()
    if event.keysym == "u" or event.keysym == "j" or event.keysym == "n" or event.keysym == "i" or event.keysym == "k" or event.keysym == "m" or event.keysym == "o" or event.keysym == "l" or event.keysym == "p":
        # Simulate a click on the "D Results" button
        display_last_lines(6)
    if event.keysym == "q" or event.keysym == "a" or event.keysym == "z" or event.keysym == "w" or event.keysym == "s" or event.keysym == "x" or event.keysym == "e" or event.keysym == "d":
        # Simulate a click on the "D Results" button
        display_first_lines(8)
root.bind("<Key>", fn_key_pressed)

root.mainloop()
