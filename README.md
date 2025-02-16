# AI Image Background Remover

An AI-powered tool to remove backgrounds from images using the `rembg` library and pre-trained models. This project leverages Python along with the Pillow library for image processing to deliver quick and effective background removal.

## Features

- **Background Removal:** Easily remove image backgrounds with minimal input.
- **Command-Line Interface:** Simple CLI to process images.
- **Extendable:** Designed for further enhancements and integration with UI frameworks.

## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- [Python 3.6+](https://www.python.org/downloads/)
- Git (for cloning the repository)

### Installation

1. **Clone the Repository:**

2. Set Up a Virtual Environment:

Create and activate a virtual environment:

Windows:
bash
python -m venv venv
venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

### Install Dependencies:

Install the required Python packages using the requirements.txt file:
pip install -r requirements.txt

If you encounter an error regarding a missing module for onnxruntime, install it manually:
pip install onnxruntime

For GPU support (optional), you can install:
pip install onnxruntime-gpu

### Usage
Run the background remover script from the command line:
python main.py <input_image_path> <output_image_path>


For example, if you have an image named input.png and you want to save the processed image as output.png, run:
python main.py input.png output.png


python main.py input.png output.png

The script will process the image, remove its background, and save the new image to the specified output path.

### How It Works
Image Loading:
The script uses the Pillow library to open and process images.

Background Removal:
The rembg library processes the image bytes to remove the background.

Saving the Result:
The processed image (with the background removed) is then saved to the designated output path.

### Contributing
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request. For any issues or suggestions, please open an issue on GitHub.

### Acknowledgments
rembg for the background removal functionality.
Pillow for image processing.
