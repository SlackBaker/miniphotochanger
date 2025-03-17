from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

# Глобальна змінна для збереження оригінального зображення
current_image = None


def openImage():
    global current_image
    # Вибір зображення через діалогове вікно
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        img = cv2.imread(file_path)  # Завантаження зображення через OpenCV
        current_image = img  # Збереження оригінального зображення
        displayImage(img)


def grayImage():
    global current_image
    if current_image is not None:
        # Конвертація зображення в сірий формат
        gray_img = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)
        current_image = gray_img  # Оновлення глобальної змінної
        displayImage(gray_img, is_gray=True)


def saveImage():
    global current_image
    if current_image is not None:
        # Вибір місця для збереження файлу
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),
                                                            ("All Files", "*.*")])
        if file_path:
            # Збереження зображення
            cv2.imwrite(file_path, current_image)
            print("Зображення збережено:", file_path)


def displayImage(img, is_gray=False):
    # Якщо зображення сіре, не потрібно конвертувати в RGB
    if not is_gray:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img_tk = ImageTk.PhotoImage(image=img)

    # Відображення зображення у Tkinter
    label.config(image=img_tk)
    label.image = img_tk


root = Tk()

# Налаштування вікна
root.geometry("600x600")
root.resizable(width=False, height=False)

# Додати кнопку для відкриття зображення
btn_open = Button(root, text="Open Image", command=openImage)
btn_open.pack(pady=10)

# Додати кнопку для конвертації зображення в сірий формат
btn_gray = Button(root, text="Convert to Grayscale", command=grayImage)
btn_gray.pack(pady=10)

# Додати кнопку для збереження зображення
btn_save = Button(root, text="Save Image", command=saveImage)
btn_save.pack(pady=10)

# Додати мітку для відображення зображення
label = Label(root)
label.pack()

# Головний цикл
root.mainloop()
