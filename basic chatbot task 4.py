def basic_chatbot():
    print("--- Basic Chatbot ---")
    print("Chatbot: Hi! How can I help you today? (Type 'bye' to exit)")

    while True: # Infinite loop to keep the chatbot running
        user_input = input("You: ").lower() # Get user input and convert to lowercase for easier matching

        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "how are you":
            print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break # Exit the loop if the user says "bye"
        else:
            # Default response for anything not recognized
            print("Chatbot: I'm sorry, I don't understand that. Can you rephrase?")
    print("-" * 20)

# To run the Basic Chatbot:
if __name__ == "__main__":
    basic_chatbot()