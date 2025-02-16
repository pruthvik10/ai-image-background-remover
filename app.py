import streamlit as st
from rembg import remove
from PIL import Image
import io

# Set up the Streamlit app
st.title("AI Image Background Remover")
st.write("Upload an image below to remove its background:")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Original Image", use_column_width=True)

    # Convert the image to bytes
    img_byte_arr = io.BytesIO()
    input_image.save(img_byte_arr, format='PNG')
    input_bytes = img_byte_arr.getvalue()

    # Remove background using rembg
    output_bytes = remove(input_bytes)

    # Convert processed bytes back to an image
    output_image = Image.open(io.BytesIO(output_bytes))

    # Display the output image
    st.image(output_image, caption="Image with Background Removed", use_column_width=True)
