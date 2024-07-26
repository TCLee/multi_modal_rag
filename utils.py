"""
This module contains helper functions used by 
the Jupyter notebook. The functions are moved
here to avoid cluttering the notebook.

"""

import base64
import json
import uuid
import re

from os import PathLike
from typing import TypedDict

from IPython.display import HTML, display

from langchain_core.documents import Document
from langchain.storage import LocalFileStore
from langchain.retrievers.multi_vector import MultiVectorRetriever


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


def remove_all_documents_from_store(
    document_store: LocalFileStore
):
    """
    Removes all documents from the local document store.

    Args:
        document_store: The document store to remove the 
            documents from.
    """
    all_document_ids = [
        doc_id 
        for doc_id 
        in document_store.yield_keys()
    ]
    document_store.mdelete(all_document_ids)


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


def add_documents(    
    retriever: MultiVectorRetriever, 
    summaries: list[str], 
    raw_contents: list[str],
):
    """
    Add summaries to the vector store and full raw 
    contents to the document store of the multi vector 
    retriever.

    Args:
        retriever: The multi-vector retriever.
        summaries: List of summaries for the raw contents.
        raw_contents: List of unsummarized (full) texts, 
            tables, images (Base64 string).
    """
    # Generate a unique ID for each Document.
    doc_ids = generate_random_ids(
        count=len(summaries)
    )

    # Create a LangChain Document for each summary.
    summary_docs = create_documents_from_texts(
        id_key=retriever.id_key,
        texts=summaries,
        doc_ids=doc_ids
    )
    
    retriever.vectorstore.add_documents(
        documents=summary_docs
    )

    # Document store saves the contents as 
    # bytes rather than string.
    raw_contents_bytes = [
        string.encode() 
        for string in raw_contents
    ]
    
    retriever.docstore.mset(
        key_value_pairs=list(
            zip(doc_ids, raw_contents_bytes)
        )
    )

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


def looks_like_base64(string: str):
    """
    Check if the string looks like base64

    """
    return re.match(
        "^[A-Za-z0-9+/]+[=]{0,2}$", string
    ) is not None


def is_image_data(
    base64_data: bytes
) -> bool:
    """
    Check if the base64 data is an image by 
    looking at the start of the data

    """
    image_signatures = {
        b"\xff\xd8\xff": "jpg",
        b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a": "png",
        b"\x47\x49\x46\x38": "gif",
        b"\x52\x49\x46\x46": "webp",
    }

    try:
        # Decode and get the first 8 bytes.
        header = base64.b64decode(base64_data)[:8]

        # If header starts with any of the above image
        # signatures, then it is an image (True)        
        for signature, _ in image_signatures.items():
            if header.startswith(signature):
                return True
            
        # Header not found in the image signatures,
        # not an image (False).
        return False
    
    except Exception:
        # Failed to decode as Base64.
        return False
    

class PromptContext(TypedDict):
    """
    Context that will be injected into the prompt 
    and passed to the LLM.

    Attributes:
        base64_images: List of images encoded in Base64.
        texts_or_tables: List of texts or tables. 
            Tables are also represented as plain string.

    """
    base64_images: list[str]
    texts_or_tables: list[str]


def split_image_text_types(
    retrieved_documents: list[bytes]
) -> PromptContext:
    """
    Split base64-encoded images and texts

    """
    base64_images = []
    texts = []

    for doc_bytes in retrieved_documents:
        doc_str = doc_bytes.decode()

        if (looks_like_base64(doc_str) 
            and is_image_data(doc_bytes)):
            base64_images.append(doc_str)
        else:
            texts.append(doc_str)

    return PromptContext(
        base64_images=base64_images,
        texts_or_tables=texts,
    )