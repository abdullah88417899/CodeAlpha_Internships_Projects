import nltk
from nltk.chat.util import Chat, reflections

# pairs of patterns and responses
pairs = [
    (r'Hi|Hello|Hey', ['Hello! How can I help you today?', 'Hi there! How can I assist you?']),
    (r'What is your name?', ['I am a chatbot created with NLTK.']),
    (r'How are you?', ['I am just a program, but thanks for asking! How can I help you?']),
    (r'I need help with (.*)', ['I can help with %1. What do you need help with?']),
    (r'Bye|Goodbye', ['Goodbye! Have a great day!', 'See you later!']),
    (r'(.*)', ['Sorry, I did not understand that.'])
]

# Created a chatbot instance
chatbot = Chat(pairs, reflections)

# A function to interact with the chatbot
def chat_with_bot():
    print("Chatbot: Hi! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start chatting with the bot
if __name__ == "__main__":
    chat_with_bot()
