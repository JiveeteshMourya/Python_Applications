print("Welcome to Coding Thinker ChatBot")
import time # time is lib that allows to use time related fnx
t = time.ctime()
import tkinter as tk

ans = {
    "hi": "Hello",
    "how are you": "I'm fine, thank you",
    "what's your name": "My name is Bot, James Bot",
    "what's your age": "I'm a Bot, I don't have an age",
    "What do you do": "I'm a Bot, I don't have any actions",
    "what's your favorite color": "I don't have a favorite color, I'm a Bot",
    "tell me the current time": t,
    "what is your purpose": "My purpose is to assist you with your queries",
    "can you help me with coding": "Yes, I can assist you with coding!",
    "what is your favorite food": "I don't eat food, I'm a Bot",
    "do you like music": "I don't have preferences, I'm a Bot",
    "how can I contact you": "You can interact with me through this interface",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "what is the weather like today": "Sorry, I can't check the weather right now, but I can help with other queries.",
    "what is your favorite book": "I don't have a favorite book, but I can recommend some!",
    "do you have feelings": "I don't have feelings, I'm just a Bot",
    "can you solve math problems": "Yes, I can help you with math problems",
    "what is your favorite hobby": "I don't have hobbies, I'm a Bot",
    "do you watch movies": "I don't watch movies, but I can suggest some!",
    "can you play games": "I don't play games, but I can help you create one",
    "where do you live": "I don't have a physical location, I'm a Bot",
    "do you like the internet": "I exist on the internet, so yes!",
    "what's the meaning of life": "That's a big question! Many philosophers have tried to answer it.",
    "can you give me a motivational quote": "Sure! 'The only way to do great work is to love what you do.' - Steve Jobs",
    "how do you work": "I work by processing your queries and providing responses based on patterns and information.",
    "what's your favorite movie": "I don't have a favorite movie, but I can recommend some for you!"
}

# while(True):
#     inp = input("Enter question: ")
#     if(inp == "quit"):
#         break
#     elif(ans[inp] == False):
#         print("wront input")
#     else: 
#         print(ans[inp])

def chatbot_response():
    user_input = user_entry.get()

    response = ans.get(user_input.lower(), "I don't understand that!")
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"You: {user_input}\nChatbot: {response}\n\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.see(tk.END)

root = tk.Tk()
root.title("Chatbot")

chat_history = tk.Text(root, height=20, width=80, state=tk.DISABLED, wrap=tk.WORD)
chat_history.grid(row = 0, column=0, columnspan=2, padx=10, pady=10)

user_entry = tk.Entry(root, width=40, font=("Arial", 12))
user_entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=chatbot_response)
send_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()