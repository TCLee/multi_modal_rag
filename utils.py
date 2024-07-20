"""
This module contains helper functions used by 
the Jupyter notebook. The functions are moved
here to avoid cluttering the notebook.

"""

import base64
import json
import uuid

from os import PathLike

from IPython.display import HTML, display

from langchain_core.documents import Document


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
    

def generate_random_ids(
    count: int
) -> list[str]:
    """
    Generates a list of random UUID.

    Args:
        count: Number of random UUID to generate.

    Returns:
        List of random UUID with `count` elements.
        
    """
    return [
        str(uuid.uuid4()) 
        for _ in range(count)
    ]


def create_documents_from_texts(
    id_key: str,
    texts: list[str],
    doc_ids: list[str],
) -> list[Document]:
    """
    Creates a LangChain `Document` object for each text content.

    Args:
        id_key: Key for the document ID value.
        texts: List of text contents.
        doc_ids: List of unique IDs for each document.

    Returns:
        List of LangChain `Document` objects.
    
    """
    return [
        Document(
            page_content=text, 
            metadata={
                id_key: doc_ids[index]
            }
        )
        for index, text in enumerate(texts)
    ]


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


def plot_image_base64(image_base64: str):
    """
    Display base64 encoded string as image

    """
    # Create an HTML img tag with the base64 string as the source
    image_html = f'<img src="data:image/jpeg;base64,{image_base64}" />'

    # Display the image by rendering the HTML
    display(
        HTML(image_html)
    )
