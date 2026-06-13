while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user_input == "what is your name":
        print("Bot: I am a Rule-Based Chatbot.")

    elif user_input == "bye" or user_input == "exit":
        print("Bot: Goodbyee! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")