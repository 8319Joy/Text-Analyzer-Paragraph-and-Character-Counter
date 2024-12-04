#!/usr/bin/env python
# coding: utf-8
Here’s a brief description of the program:

This Python program provides a GUI-based Paragraph and Character Counter using the `tkinter` library. It allows users to input text into a multi-line text area, press a "Count" button, and view the results showing:

1. Number of Paragraphs: Counts non-empty lines as paragraphs.
2. Number of Characters: Counts all characters in the paragraphs.

Features:
- Simple and interactive interface.
- Real-time result display.
- Handles empty inputs gracefully with a warning popup.

Usage:
1. Enter or paste text into the provided box.
2. Click the Count button.
3. View the results displayed below.
# In[4]:


import tkinter as tk
from tkinter import messagebox

def count_paragraphs_and_characters():
    # Get text from the text area
    content = text_area.get("1.0", tk.END).strip()
    
    if not content:
        messagebox.showwarning("Warning", "Please enter some text!")
        return
    
    # Splitting paragraphs and filtering empty lines
    paragraphs = [p.strip() for p in content.split('\n') if p.strip()]
    num_paragraphs = len(paragraphs)
    num_characters = sum(len(p) for p in paragraphs)
    
    # Display results
    result_label.config(
        text=f"Number of paragraphs: {num_paragraphs}\nNumber of characters: {num_characters}"
    )

# Create the main application window
root = tk.Tk()
root.title("Paragraph and Character Counter")

# Create a text area
text_area = tk.Text(root, wrap=tk.WORD, height=15, width=50)
text_area.pack(pady=10)

# Create a button to trigger the counting process
count_button = tk.Button(root, text="Count", command=count_paragraphs_and_characters)
count_button.pack(pady=5)

# Label to display results
result_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()


# In[ ]:




