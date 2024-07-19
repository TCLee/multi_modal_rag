"""
This module contains helper functions used by 
the Jupyter notebook. The functions are moved
here to avoid cluttering the notebook.

"""

from os import PathLike

import base64
import json

from IPython.display import HTML, display

def write_to_json(summaries: list[str], json_path: str):
    """
    Saves a list of summaries to a JSON file.

    Args:
        summaries: List of summaries.
        json_path: Path to JSON file.

    """
    with open(
        file=json_path, 
        mode='w', 
        encoding='utf-8') as f:
        json.dump(
            summaries, 
            f,        
            ensure_ascii=False,             
            indent=4
        )


def read_from_json(json_path: str) -> list[str]:
    """
    Returns a list of summaries loaded from a JSON file.

    Args:
        json_path: Path to JSON file.

    Returns:
        List of summaries
    """
    with open(
        file=json_path, 
        mode='r', 
        encoding='utf-8') as f:
        return json.load(f)
    

def encode_image(
    image_path: PathLike
) -> str:
    """
    Encodes an image as a Base64 string.
    
    Args:
        image_path: Path to the image.

    Returns:
        A Base64 string.
        
    """
    with open(
        file=image_path, 
        mode="rb" # read + binary mode
    ) as image_file:
        return base64.b64encode(
            image_file.read()
        ).decode("utf-8")


def plt_img_base64(image_base64: str):
    """
    Display base64 encoded string as image

    """
    # Create an HTML img tag with the base64 string as the source
    image_html = f'<img src="data:image/jpeg;base64,{image_base64}" />'

    # Display the image by rendering the HTML
    display(
        HTML(image_html)
    )
