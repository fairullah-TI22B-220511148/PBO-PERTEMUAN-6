from gtts import gTTS
import os
import tkinter as tk
from tkinter import ttk

def text_to_speech():
    text = entry.get()
    language = 'id'  # Ganti dengan kode bahasa yang diinginkan (contoh: 'en' untuk Inggris)

    try:
        # Membuat objek gTTS
        tts = gTTS(text=text, lang=language, slow=False)

        # Simpan sebagai file audio
        tts.save("output.mp3")

        # Putar file audio
        os.system("start output.mp3")

    except Exception as e:
        print("Error:", str(e))

# Membuat GUI
root = tk.Tk()
root.title("Text-to-Speech Converter")

# Label
label = ttk.Label(root, text="Masukkan teks:")
label.grid(column=0, row=0, padx=10, pady=10)

# Entry untuk memasukkan teks
entry = ttk.Entry(root, width=40)
entry.grid(column=1, row=0, padx=10, pady=10)

# Tombol untuk konversi teks ke suara
button = ttk.Button(root, text="Konversi", command=text_to_speech)
button.grid(column=0, row=1, columnspan=2, pady=10)

# Menjalankan loop utama
root.mainloop()