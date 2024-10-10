# Professor AI

AI assistant that can answer questions based on a specific knowledge base as if they were a university professor.
Details below explain what to be modified to change the response.

Uses Haystack (https://haystack.deepset.ai/), and is designed to be easily modified by non-programmers by simply changing the models used.

## Python Environment

Running python `3.9.13` as a `pyenv virtualenv` named `professorai`

Activate local environment with `pyenv local professorai`
Deactivate with `pyenv deactivate`
(Note: vscode will do this automatically if interpreter correctly set)

## Running

1. Install all dependencies (see below)
2. Add all relevant documents to `data/knowledge-docs/`
3. Run
   ```
   source .env
   ```
   (only need to do this once at the beginning).
4. To run the Gradio interface (simple interface to talk to the model)
   ```
   python src/gradio_interface.py
   ```
5. Access the chat at `http://127.0.0.1:7860` (or whatever port it says to access)
6. `Ctrl`+`C` to stop the program

### Dependencies

Install dependencies with

```
pip install -r requirements.txt
```

And update them (if installing any new libraries) with

```
pipreqs .
```

## System configuration

My `.env` file contains

```
export PYTORCH_ENABLE_MPS_FALLBACK=1
```

which I recommend adding. It also contains

```
export HF_API_TOKEN=<my token>
```

Don't forget to `source .env` before running the program.

## Changing the Response

The best way to change the response is in `data_reader.py` by modifying the Haystack pipeline:
https://haystack.deepset.ai/tutorials

Places for modification include.

- Changing the query embedding model "embedder" in `data_reader.py` (for processing the query)
- Changing the large language model "llm" in `data_reader.py` (for the response)
- Changing the document retriever "retriever" in `data_reader.py`
- Changing the template "template" in `data_retriever.py`
- Changing the document embedder "document_embedder" in `doc_processing.py`
- Replacing InMemoryReader with another document store in `doc_processing.py`

## Other

Remove pycache with

```
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
rm -rf .pytest_cache
```
