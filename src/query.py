from data_reader import pipe


def ask_professor(question):
    # Reformat the query to sound like a professor
    reformatted_question = f"As an computer science professor, {question} Please explain in detail."

    # Retrieve relevant documents using Haystack
    result = pipe.run(query=reformatted_question, params={"Retriever": {"top_k": 5}, "Reader": {"top_k": 5}})

    # Get the relevant document content
    document_content = result["documents"][0].content

    return document_content

    # # Create a full prompt for the LLM
    # prompt = f"Explain the following topic to a student in a conversational, professor-like tone:\n\nTopic: {question}\n\nContext from anthropology documents:\n\n{document_content}\n"

    # # You can replace this with any LLM model you prefer (local or hosted)
    # response = LLM(prompt)  # Replace with actual LLM call (e.g., OpenAI GPT, local Huggingface model)

    # return response
