import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name",
        ["I am AWBoot.",]
    ],
    [
        r"how are you?",
        ["I'm good and you!",]
    ],
    [
        r"when were you created",
        ["i was created in 18 10 2024.",]
    ],
    [
        r"quit",
        ["Goodbye!", "Have a nice day!"]
    ],
    [
        r"(.*)",
        ["I am not sure how to respond to that.",]
    ]
]

def chatbot():
    print("Hi, I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()