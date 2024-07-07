# Extract Structured Data from Text

## Overview

In the [notebook](extract_structured_data.ipynb), we will see how we can extract structured data from unstructured text. More specifically, we'll use Google's Gemini model to extract the lists of characters, relationships, things, and places from a short story.

The code in the notebook is adapted from Google's 
[Gemini tutorial](https://ai.google.dev/gemini-api/tutorials/extract_structured_data).


## Setup

### Git
Clone this repository to your local computer by running:

```zsh
git clone https://github.com/TCLee/extraction
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
[`extract_structured_data.ipynb`](extract_structured_data.ipynb) 
and follow the instructions there.