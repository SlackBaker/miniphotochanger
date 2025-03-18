from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

# Глобальні змінні
original_image = None  # Початкове зображення
current_image = None    # Поточне змінене зображення


def openImage():
    global original_image, current_image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        img = cv2.imread(file_path)
        original_image = img.copy()  # Збереження оригіналу
        current_image = img
        displayImage(img)


def grayImage():
    global current_image
    if current_image is not None:
        gray_img = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)
        current_image = gray_img
        displayImage(gray_img, is_gray=True)


def bluredImage():
    global current_image
    if current_image is not None:
        blured_img = cv2.GaussianBlur(current_image, (15, 15), 0)
        current_image = blured_img
        displayImage(blured_img, is_gray=False)


def resetImage():
    """Повертає зображення до оригіналу"""
    global current_image, original_image
    if original_image is not None:
        current_image = original_image.copy()
        displayImage(current_image)


def saveImage():
    global current_image
    if current_image is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),
                                                            ("All Files", "*.*")])
        if file_path:
            cv2.imwrite(file_path, current_image)
            print("Зображення збережено:", file_path)


def displayImage(img, is_gray=False):
    if not is_gray:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img_tk = ImageTk.PhotoImage(image=img)

    label.config(image=img_tk)
    label.image = img_tk


root = Tk()
root.title("Редактор Зображень")
root.geometry("600x600")
root.resizable(width=False, height=False)

# Фрейм для кнопок
button_frame = Frame(root)
button_frame.pack(pady=10)

btn_open = Button(button_frame, text="Відкрити", command=openImage)
btn_open.pack(side="left", padx=10)

btn_gray = Button(button_frame, text="Градації сірого", command=grayImage)
btn_gray.pack(side="left", padx=10)

btn_blur = Button(button_frame, text="Розмиття", command=bluredImage)
btn_blur.pack(side="left", padx=10)

btn_reset = Button(button_frame, text="Скинути", command=resetImage)  # Кнопка "Скинути"
btn_reset.pack(side="left", padx=10)

btn_save = Button(button_frame, text="Зберегти", command=saveImage)
btn_save.pack(side="left", padx=10)

# Мітка для відображення зображення
label = Label(root)
label.pack()

root.mainloop()
