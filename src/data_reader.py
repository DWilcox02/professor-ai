from haystack.nodes import BM25Retriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline
from doc_processing import document_store


# Set up the retriever
retriever = BM25Retriever(document_store=document_store)

# Initialize the reader (LLM)
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")

# Combine the retriever and reader into a pipeline
pipe = ExtractiveQAPipeline(reader, retriever)
