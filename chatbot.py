from nltk.chat.util import Chat, reflections

pairs = [
    (r"hi|hello|hey", ["Hello!", "How can i help you today?", "Hi there! How Can I help you?"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm  good how about you!"]),
    (r"(.*)color(.*)", ["I like all colors!", "I don't have a favourite color."]),
    (r"(.*)(course|program)(.*)", ["We offer great programs in Android development and Full Stack Development."]),
    (r"(.*)android(.*)", ["We offer an Android development program where you'll learn how to build mobile apps using Kotlin and Java."]),
    (r"(.*)full stack(.*)", ["Our Full Stack Development program covers both front-end(HTML,CSS,Javascript) and back-end develoPython Flask)."]),
    (r"(.*)mobile\s?apps", ["We offer a program in Android development where you'll learn how to build mobile apps using Kotlin and Java."]),
    (r"(.*)", ["Sorry, I didn't understand that.", "Can you please rephrase?", "I'm not sure I understand."]),
]

chatbot = Chat(pairs, reflections)

print("Hello! I'm a chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)