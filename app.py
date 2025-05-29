# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:37:00 2024

@author: raxephion
Image generation with DALL-E-2 and DALL-E-3, including model and size selection
"""

import openai
import urllib.request
from PIL import Image
import io
import gradio as gr
import os
from dotenv import load_dotenv
from datetime import datetime  # Added for unique filenames

# Load environment variables from .env file
load_dotenv()


# IMPORTANT: Never hardcode your OpenAI API key. Use a .env file with OPENAI_API_KEY=<your_key>
# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define supported models and their respective sizes
SUPPORTED_MODELS = ["dall-e-3", "dall-e-2"]

# Dictionary mapping models to their supported sizes
MODEL_SIZES = {
    "dall-e-3": ["1024x1024", "1024x1792", "1792x1024"],
    "dall-e-2": ["256x256", "512x512", "1024x1024"]
}

# I'll provide ALL possible sizes in the dropdown, and validate in the backend function
ALL_SUPPORTED_SIZES = sorted(list(set().union(*MODEL_SIZES.values())))

def generate_image(prompt: str, model: str, size: str):
    """Generates an image using the specified DALL-E model and size."""
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=size,
            model=model
        )
        image_url = response['data'][0]['url']
        return image_url
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        raise gr.Error(f"Failed to generate image: {e}") from e
    except Exception as e:
        print(f"An unexpected error occurred during image generation: {e}")
        raise gr.Error(f"An unexpected error occurred: {e}") from e

def save_image(image_url: str, filename: str):
    """Saves an image from a URL to a file."""
    try:
        script_dir = os.path.dirname(__file__) if '__file__' in globals() else os.getcwd()
        full_path = os.path.join(script_dir, filename)
        urllib.request.urlretrieve(image_url, full_path)
        return full_path
    except Exception as e:
        print(f"Error saving image: {e}")
        raise gr.Error(f"Failed to save image: {e}") from e

def get_image(image_url: str):
    """Gets an image as a PIL Image object from a URL."""
    try:
        with urllib.request.urlopen(image_url) as url:
            img = Image.open(io.BytesIO(url.read()))
        return img
    except Exception as e:
        print(f"Error getting image from URL: {e}")
        raise gr.Error(f"Failed to load image from URL: {e}") from e

def gradio_interface(prompt: str, model: str, size: str):
    """Main function for the Gradio interface."""
    if not prompt:
        raise gr.Error("Please enter a prompt.")
    if model not in MODEL_SIZES or size not in MODEL_SIZES.get(model, []):
        raise gr.Error(f"Invalid size '{size}' for model '{model}'. Supported: {', '.join(MODEL_SIZES.get(model, []))}")

    print(f"Generating image with prompt: '{prompt}', model: '{model}', and size: '{size}'")

    image_url = generate_image(prompt, model, size)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"generated_{timestamp}.png"
    saved_filename = save_image(image_url, filename)
    img = get_image(image_url)

    return img, saved_filename, image_url

iface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter your prompt here...", label="Prompt"),
        gr.Dropdown(choices=SUPPORTED_MODELS, value="dall-e-3", label="AI Model"),
        gr.Dropdown(choices=ALL_SUPPORTED_SIZES, value="1024x1024", label="Image Size")
    ],
    outputs=[
        gr.Image(type="pil", label="Generated Image"),
        gr.Textbox(label="Local Filename"),
        gr.Textbox(label="Temporary Image URL"),
    ],
    title="RazorByte DALL-E WebUI (DALL-E 2 & DALL-E 3)",
    description="Generate images using OpenAI's DALL-E 2 or DALL-E 3 model. Select the model, size, and enter a detailed prompt."
)

if __name__ == "__main__":
    print("Starting Gradio interface...")
    iface.launch()
