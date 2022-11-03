import change_extensions

def check_extensions(hex, PNG, JPG, GIF, file):
    if hex == PNG and not file.endswith(".png"):
        change_extensions.change_to_png(file)
    
    elif hex == JPG and not file.endswith(".jpg"):
        change_extensions.change_to_jpg(file)
    
    elif hex == GIF and not file.endswith(".gif"):
        change_extensions.change_to_gif(file)
