import os
from haystack import Pipeline
from processor.doc_processing import document_store
from getpass import getpass
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever
from haystack.components.builders import PromptBuilder
from haystack.components.generators import HuggingFaceAPIGenerator

# Set Hugging Face API token
# Should be set in .env as HF_API_TOKEN (see README)
if "HF_API_TOKEN" not in os.environ:
    os.environ["HF_API_TOKEN"] = getpass("Enter Hugging Face token:")

# Template for the prompt. The template is a string that uses Jinja2 templating syntax.
# Modify this to customise the pipeline's response.
template = """
As a university professor with a sense of humour, answer the following questions based on your knowledge. You are funny, and like
to add jokes in your answers.

Your knowledge:
{% for document in documents %}
    {{ document.content }}
{% endfor %}

Question: {{ question }}
Answer:
"""

# Create a pipeline. The pipeline is a sequence of components that process the input data.
# After processing, the pipeline can be run to generate a response.
query_pipeline = Pipeline()

# Query embedding component. This component turns the query into a vector which will be used
# to find relevant documents in the retriever component. See more at:
# https://docs.haystack.deepset.ai/docs/embedders
query_pipeline.add_component(
    "embedder", SentenceTransformersTextEmbedder(model="sentence-transformers/all-MiniLM-L6-v2")
)

# In-memory embedding retriever component. This component retrieves relevant documents based on the query embedding.
# Change this when you want to change how document information is retrieved. See more at:
# https://docs.haystack.deepset.ai/docs/retrievers
query_pipeline.add_component("retriever", InMemoryEmbeddingRetriever(document_store=document_store))

# Prompt builder component. This component builds the prompt that will be used to generate the response.
# Doesn't really need to be changed, just change the template.
query_pipeline.add_component("prompt_builder", PromptBuilder(template=template))

# Language model generator component. This component generates the response based on the prompt.
# Change this when you want to change how the response is generated. See more at:
# https://docs.haystack.deepset.ai/reference/generators-api
query_pipeline.add_component(
    "llm",
    HuggingFaceAPIGenerator(api_type="serverless_inference_api", api_params={"model": "meta-llama/Meta-Llama-3-8B"}),
)

# After embedding the query, connect it to the document retriever
query_pipeline.connect("embedder.embedding", "retriever.query_embedding")

# Connect the collected documents from the retriever to the prompt builder
query_pipeline.connect("retriever", "prompt_builder.documents")

# Connect the built prompt to the language model generator
query_pipeline.connect("prompt_builder", "llm")


# Entry function that will run the pipeline and return the response
def query_pipeline(question):

    # Learn more at: https://docs.haystack.deepset.ai/docs/pipelines
    result = query_pipeline.run(
        {
            "embedder": {"text": question},
            "prompt_builder": {"question": question},
            "llm": {"generation_kwargs": {"max_new_tokens": 350}},
        },
        include_outputs_from={"prompt_builder", "llm"},
    )

    return result["llm"]["replies"]
