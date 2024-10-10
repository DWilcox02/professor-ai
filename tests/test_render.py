from jinja2 import Template

# Example test documents
documents = [{"content": "Document 1 content"}, {"content": "Document 2 content"}]
question = "What is anthropology?"

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

t = Template(template)
rendered_template = t.render(documents=documents, question=question)
print(rendered_template)
