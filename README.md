# Professor AI

AI assistant that can answer questions based on a specific knowledge base as if they were a university professor.

## Python configuration

Running python `3.9.13` as a `pyenv virtualenv` named `professorai`

Activate local environment with `pyenv local professorai`
Deactivate with `pyenv deactivate`
(Note: vscode will do this automatically if interpreter correctly set)

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

which I recommend adding. Don't forget to `source .env` before running the program.

## Running

Add all relevant documents to `data/knowledge-docs/`, then run:

```
python src/gradio_interface.py
```

## Changin Response

The best way to change the response is in `data_reader.py` by modifying the Haystack pipeline:
https://haystack.deepset.ai/tutorials

Potential improvements include:

- Replacing InMemoryReader with its own pre-processed server that can be accessed by this application
- Changing the model
- Changing the prompt template
- etc....

## Other

Remove pycache with

```
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
rm -rf .pytest_cache
```
