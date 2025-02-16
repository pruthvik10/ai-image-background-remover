from rembg import remove
from PIL import Image
import io
import sys

def remove_background(input_path, output_path):
    # Open the input image
    input_image = Image.open(input_path)
    # Convert image to bytes
    img_byte_arr = io.BytesIO()
    input_image.save(img_byte_arr, format='PNG')
    input_bytes = img_byte_arr.getvalue()

    # Remove background using rembg
    output_bytes = remove(input_bytes)

    # Convert bytes back to an image
    output_image = Image.open(io.BytesIO(output_bytes))
    output_image.save(output_path)
    print(f"Background removed. Saved output to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_image_path> <output_image_path>")
    else:
        input_image_path = sys.argv[1]
        output_image_path = sys.argv[2]
        remove_background(input_image_path, output_image_path)
