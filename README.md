# Multi-modal RAG

## Overview

Many documents contain a mixture of content types, including text, tables, and images. 

Semi-structured data can be challenging for [conventional RAG](https://github.com/TCLee/rag-langchain) for at least two reasons:

* Text splitting may break up tables, corrupting the data in retrieval.
* Embedding tables may pose challenges for semantic similarity search.

And the information captured in images is typically lost.

With the emergence of more affordable multimodal LLMs, like [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-1.5-flash) and [GPT-4o mini](https://platform.openai.com/docs/models/gpt-4o-mini), it is worth considering how to utilize images in RAG.

The code in this notebook is adapted from the 
[LangChain cookbook](https://github.com/langchain-ai/langchain/blob/master/cookbook/Multi_modal_RAG.ipynb).


## Setup

### Git
Clone this repository to your local computer by running:

```zsh
git clone https://github.com/TCLee/multi_modal_rag
```

### Conda
1. You will need conda in order to install the required packages to run the notebook. [Installing conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html).

2. Make sure the current working directory is this cloned project's directory:

   ```zsh
   cd /path/to/project_dir
   ```
   
3. Create the environment from the 
   [`environment.yml`](environment.yml) file:

    ```zsh
    conda env create -f environment.yml -p ./env
    ```

    This will create a new environment in a subdirectory of the project directory called `env`, (i.e., `project_dir/env`)

4. Activate the environment: 

    ```zsh
    conda activate ./env
    ```

### Environment variables
This project makes use of 
[python-dotenv](https://github.com/theskumar/python-dotenv)
to load in the environment variables from a `.env` file.

Create a `.env` file in the root directory of your project
(i.e., `project_dir/.env`):

```Dotenv
# Google Gemini API
GOOGLE_API_KEY="your-google-secret-key"
```

See instructions below to get your own API key.

#### Google Gemini
The LLM that we will use in the notebook is Google's **Gemini 1.5 Flash**. It's fast and it offers us a free tier to play around with.

To use the Gemini API, you'll need an API key. If you do not already have one, create a key in Google AI Studio.

[Get an API key](https://makersuite.google.com/app/apikey)


### Jupyter Notebook

The conda environment includes an installation of [Jupyter Lab](https://jupyter.org/). Start Jupyter Lab from your terminal:

```zsh
jupyter lab
```

In Jupyter Lab, open the notebook 
[`Multi_Modal_RAG.ipynb`](Multi_Modal_RAG.ipynb) 
and follow the instructions there.