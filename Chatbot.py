def chatbot():
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input:
            print("Bot: Hi!")
        elif "how are you" in user_input:
            print("Bot: I'm fine, thanks!")
        elif "bye" in user_input:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

chatbot()