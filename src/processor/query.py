from processor.data_reader import query_pipeline


# If multiple replies are provided, concatenate them into a single string
def concatenate_replies(replies):
    concatenated_replies = ""
    reply_no = 1
    for reply in replies:
        concatenated_replies += f"Reply {reply_no}:{reply} \n"
        reply_no += 1

    return concatenated_replies


def ask_professor(question):

    # Query the pipeline
    top_3_replies = query_pipeline(question)

    # Concatenate the replies
    return concatenate_replies(top_3_replies)
