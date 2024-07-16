"""
This module contains helper functions used by 
the Jupyter notebook. The functions are moved
here to avoid cluttering the notebook.

"""

import base64
import json

from unstructured.documents.elements import Element


def categorize_elements(
    raw_pdf_elements: list[Element]
) -> tuple[list[str], list[str]]:
    """
    Categorize partitioned elements from 
    a PDF document into tables and texts.
    
    Args:
        raw_pdf_elements: List of elements partitioned from PDF.

    Returns:
        Tuple containing the text elements' 
        contents and the table elements' contents.

    """
    texts, tables = ([], [])
    
    for element in raw_pdf_elements:
        if element.category == "Table":
            tables.append(element.text)
        elif element.category == "CompositeElement":
            texts.append(element.text)
            
    return texts, tables


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
    
