import os
from getpass import getpass
from transformers import AutoModelForCausalLM, AutoTokenizer
from processor.data_reader import query_pipeline
from huggingface_hub import login

if "HF_API_TOKEN" not in os.environ:
    os.environ["HF_API_TOKEN"] = getpass("Enter Hugging Face token:")

token = os.environ["HF_API_TOKEN"]

login(token=token)
# Load a pre-trained conversational model
model_name = "meta-llama/Meta-Llama-3-8B"  # Lighter version of GPT-2
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


# Maintain conversation history as a string
conversation_history = ""


def truncate_history(conversation_history, max_tokens=1024):
    # Tokenize history
    tokens = tokenizer(conversation_history, return_tensors="pt")["input_ids"]
    # If the token count exceeds the max, truncate it
    if tokens.shape[1] > max_tokens:
        conversation_history = tokenizer.decode(tokens[0, -max_tokens:], skip_special_tokens=True)
    return conversation_history


def query_knowledge(question):
    result = query_pipeline.run(
        {
            "embedder": {"text": question},
            "prompt_builder": {"question": question},
            "llm": {"generation_kwargs": {"max_new_tokens": 350}},
        }
    )

    return result["llm"]["replies"][0]


def ask_professor(question):
    # global conversation_history

    # Query the knowledge base
    knowledge = query_knowledge(question)
    return knowledge
    # print(f"Knowledge of subject: {knowledge}")

    # # Append the question and knowledge to the conversation history
    # conversation_history += f"Human: {question}\n"
    # conversation_history += f"Knowledge: {knowledge}\n"
    # conversation_history = truncate_history(conversation_history)

    # print(f"Conversation history: {conversation_history}")
    # # Tokenize the conversation
    # inputs = tokenizer(conversation_history, return_tensors="pt")
    # print(f"Tokenised inputs: {inputs}")

    # # Generate a response
    # response_ids = model.generate(inputs["input_ids"], max_length=1000, pad_token_id=tokenizer.eos_token_id)
    # print(f"Response IDs: {response_ids}")

    # response = tokenizer.decode(response_ids[:, inputs["input_ids"].shape[-1] :][0], skip_special_tokens=True)
    # print(f"Response: {response}")

    # # Update conversation history with the model's response
    # conversation_history += f"Professor: {response}\n"

    # print(f"Response: {response}")
    # return response
