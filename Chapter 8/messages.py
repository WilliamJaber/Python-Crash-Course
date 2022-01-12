text_messages = ["Call me later", "Arriving", "Leave a message"]

def show_messages(short_messages) -> str:
    """Prints each text message in the list"""

    for message in short_messages:
        print(f"Hey!! {message}. \n")

show_messages(text_messages)
