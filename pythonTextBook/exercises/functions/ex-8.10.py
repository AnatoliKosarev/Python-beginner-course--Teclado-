def show_messages(messages: list):
    for message in messages:
        print(message)


def send_messages(messages: list) -> list:
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)


messages = ["Hello", "YO!", "What is up, baby ?"]
sent_messages = []
send_messages(messages)
show_messages(messages)
show_messages(sent_messages)
