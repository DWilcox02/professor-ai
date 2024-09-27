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

which I recommend adding. Don't forget to `source .env` to ensure it's saved

## Running

Add all relevant documents to `data/knowledge-docs/`, then run:

```
python src/gradio_interface.py
```

## Other

Remove pycache with

```
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
```
