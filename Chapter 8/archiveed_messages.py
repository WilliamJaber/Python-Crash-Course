text_messages = ["Call me later", "Arriving", "Leave a message"]
sent_messages = []

def send_messages(short_messages, sent) -> str:
    """Prints each text message in the list and copy them into a new sent messages list"""

    for message in short_messages:
        print(f"Hey!! {message}.\n")
    while short_messages:
        current_message = short_messages.pop()
        sent.append(current_message)

send_messages(text_messages[:], sent_messages)
# print both of your lists to show that the original list has retained its messages
print(text_messages)
print(sent_messages)
