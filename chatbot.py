print("Simple Chatbot")
print("Type 'bye' to exit")

while True:
    user = input("You: ")

    if user.lower() == "hello":
        print("Bot: Hello!")

    elif user.lower() == "how are you":
        print("Bot: I am fine.")

    elif user.lower() == "your name":
        print("Bot: I am a Python chatbot.")

    elif user.lower() == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand.")
