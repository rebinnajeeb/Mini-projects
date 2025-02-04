from PIL import Image

def resize_image(input_path, output_path, size):
    try:
        original = Image.open(input_path)
        resized = original.resize(size)
        resized.save(output_path)
        print(f"Image saved as {output_path} with size {size}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_image = input("Enter input image file name (with extension): ")
    output_image = input("Enter output image file name (with extension): ")
    width = int(input("Enter new width: "))
    height = int(input("Enter new height: "))
    size_new = (width, height)
    
    resize_image(input_image, output_image, size_new)