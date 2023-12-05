import tkinter as tk
from tkinter import filedialog
import pygame
from pygame.locals import *

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video files", "*.mp4")])
    if file_path:
        play_video(file_path)

def play_video(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Create the main window
root = tk.Tk()
root.title("Video Player")

# Create widgets
btn_open_file = tk.Button(root, text="Open Video", command=open_file_dialog)

# Place widgets in the window
btn_open_file.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()