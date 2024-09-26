# Professor AI

AI assistant that can answer questions based on a specific knowledge base as if they were a university professor.

## Python configuration

Running python `3.9.13` as a `pyenv virtualenv` named `professorai`

Activate local environment with `pyenv local professorai`
Deactivate with `pyenv deactivate`

## Running

```
python src/gradio_interface.py
```

## Other

Remove pycache with

```
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
```
