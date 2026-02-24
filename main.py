def chatbot(msg):
    if "hi" in msg.lower():
        return "Hello!"
    elif "bye" in msg.lower():
        return "Goodbye!"
    else:
        return "I don't understand"

print(chatbot("Hi"))
