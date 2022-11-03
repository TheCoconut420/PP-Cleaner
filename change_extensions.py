import os

def change_to_png(file):
    base = os.path.splitext(file)[0]
    os.rename(file, base + ".png")

def change_to_gif(file):
    base = os.path.splitext(file)[0]
    os.rename(file, base + ".gif")

def change_to_jpg(file):
    base = os.path.splitext(file)[0]
    os.rename(file, base + ".jpg")