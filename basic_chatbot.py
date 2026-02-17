def chatbot():
    print("Chatbot Service Activated")
    print("Type 'exit' to end the conversation")

    while True:
        user_input = input("User: ").lower()

        if user_input == "hello":
            print("Bot: Hello. How can I assist you?")
        elif user_input == "how are you":
            print("Bot: I am functioning properly. Thank you for asking.")
        elif user_input == "bye":
            print("Bot: Goodbye. Have a nice day.")
        elif user_input == "exit":
            print("Bot: Session terminated.")
            break
        else:
            print("Bot: Sorry, I did not understand your request.")

chatbot()