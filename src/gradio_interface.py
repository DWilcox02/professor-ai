import gradio as gr
from processor.query import ask_professor


# Define the Gradio function to ask questions
def gradio_ask(question):
    return ask_professor(question)


# Set up the Gradio interface
interface = gr.Interface(fn=gradio_ask, inputs="text", outputs="text", title="Anthropology Professor Assistant")
interface.launch()
