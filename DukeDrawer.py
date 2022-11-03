class DukeBallDrawer:
    def __init__(self):
        self.__pixel = []
        self.__magic_number = ""
        self.__size = 0
        self.__reserve = 0
        self.__offset = 0
        self.__width = 0
        self.__height = 0
        self.__planes = 0
        self.__bit_count = 0
        self.__compression = 0
        self.__size_image = 0
        self.__x_pixels_per_meter = 0
        self.__y_pixels_per_meter = 0
        self.__ppm = 0
        self.__color = 0
        self.__color_important = 0

    def load(self, filepath: str):
        with open(filepath, "rb") as file:
            self.__pixel = file.read()
            file.close()

        with open(filepath, "rb") as file:
            self.__magic_number = self.__read_int_from_file(file, 2)
            self.__size = self.__read_int_from_file(file, 4)
            self.__reserve = self.__read_int_from_file(file, 4)
            self.__offset = self.__read_int_from_file(file, 4)
            self.__width = self.__read_int_from_file(file, 4)
            self.__height = self.__read_int_from_file(file, 4)
            self.__planes = self.__read_int_from_file(file, 2)
            self.__bit_count = self.__read_int_from_file(file, 2)
            self.__compression = self.__read_int_from_file(file, 4)
            self.__size_image = self.__read_int_from_file(file, 4)
            self.__x_pixels_per_meter = self.__read_int_from_file(file, 4)
            self.__y_pixels_per_meter = self.__read_int_from_file(file, 4)
            self.__ppm = self.__read_int_from_file(file, 4)
            self.__color = self.__read_int_from_file(file, 4)
            self.__color_important = self.__read_int_from_file(file, 4)
            file.close()

                           
    def check(self):
        if self.__magic_number != 19778:
            print(self.__magic_number)
            raise Exception("Not a BMP file")

    def __read_int_from_file(self, file, number_of_bytes: int):
        buffer = file.read(number_of_bytes)
        return int.from_bytes(buffer, byteorder='little')

    def save(self, filepath: str):
        with open(filepath, "wb") as file:
            file.write(self.__pixel)
            file.flush()
            file.close()    
    
    def __str__(self) -> str:
        return f"Magic Number: {self.__magic_number}, Size: {self.__size} Reserve: {self.__reserve} Offset: {self.__offset} Width: {self.__width} Height: {self.__height} Planes: {self.__planes} Bit Count: {self.__bit_count} Compression: {self.__compression} Size Image: {self.__size_image} X Pixels Per Meter: {self.__x_pixels_per_meter} Y Pixels Per Meter: {self.__y_pixels_per_meter} PPM: {self.__ppm} Color: {self.__color} Color Important: {self.__color_important}"
    
            
drawer = DukeBallDrawer()
drawer.load("szut.bmp")
print(drawer)