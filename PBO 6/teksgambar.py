import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

# Tentukan path ke Tesseract OCR (ganti dengan path di sistem Anda)
pytesseract.pytesseract.tesseract_cmd = r'TUGAS KULIAH/Gambar.jpeg'

def extract_text_from_image(image_path):
    # Buka gambar menggunakan Pillow
    image = Image.open(image_path)

    # Ekstrak teks menggunakan Pytesseract
    text = pytesseract.image_to_string(image)

    return text

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", ".png;.jpg;*.jpeg")])
    if file_path:
        text_result.delete(1.0, tk.END)  # Clear previous text
        display_image(file_path)
        extracted_text = extract_text_from_image(file_path)
        text_result.insert(tk.END, extracted_text)

def display_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((300, 300))
    photo = ImageTk.PhotoImage(image)

    # Update the label with the new image
    label_image.config(image=photo)
    label_image.image = photo

# Create the main window
root = tk.Tk()
root.title("Text Extraction from Image")

# Create widgets
btn_open_file = tk.Button(root, text="Open Image", command=open_file_dialog)
label_image = tk.Label(root)
text_result = tk.Text(root, height=10, width=50, wrap=tk.WORD)

# Place widgets in the window
btn_open_file.pack(pady=10)
label_image.pack()
text_result.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()