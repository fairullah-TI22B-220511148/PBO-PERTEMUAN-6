import pygame
from tkinter import Tk, Button

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("TUGAS KULIAH/Yuika_Sukidakara.mp3")
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

root = Tk()
root.title("pemutar musik")

play_button = Button(root, text="Klik", command=play_music)
play_button.pack(pady=20)

stop_buttop = Button(root, text="stop",command=stop_music)
stop_buttop.pack(pady=20)

root.mainloop()