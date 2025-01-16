print("Welcome to Coding Thinker ChatBot")
import time # time is lib that allows to use time related fnx
t = time.ctime()

ans = {
    "hi": "Hello",
    "how are you": "I'm fine, thank you",
    "what's your name": "My name is Bot",
    "what's your age": "I'm a Bot, I don't have an age",
    "What do you do": "I'm a Bot, I don't have any actions",
    "what's your favorite color": "I don't have a favorite color, I'm a Bot",
    "tell me the current time": t,
}

while(True):
    inp = input("Enter question: ")
    if(inp == "quit"):
        break
    elif(ans[inp] == False):
        print("wront input")
    else: 
        print(ans[inp])