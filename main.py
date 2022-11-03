import get_hex
import check_extensions
import get_all_files

def main():
    PNG = "89504E470D0A"
    GIF = "474946383961"
    JPG = "FFD8FFE00010"
    path = input("Enter the path to the folder: ")
    file_list_location = get_all_files.get_files_location(path)
    for i in range(len(file_list_location)):
        file = file_list_location[i]
        hex = get_hex.get_hex(file)
        check_extensions.check_extensions(hex, PNG, JPG, GIF, file)

if __name__ == "__main__":
    main()