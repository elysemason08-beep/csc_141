''''''
def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = [
    "Ciani is learning about python functions!",
    "I want to become better at coding!",
    "Python is fun to learn!"
]

sent_messages = []

send_messages(messages, sent_messages)

print("\nOriginal list:")
print(messages)

print("\nSent messages:")
print(sent_messages)