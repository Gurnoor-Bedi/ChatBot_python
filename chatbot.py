import nltk
import re

# Define some responses
responses = {
    "hello": "Hi there!",
    "what's your name?": "My name is ChatBot.",
    "how are you?": "I'm doing well, thanks for asking.",
    "bye": "Goodbye!",
}
def generate_response(user_input):
  for i,response in responses.items():
    if re.search(i,user_input,re.IGNORECASE):
      return response
  return "I am sorry, I dont understand."
while True:
  user_input=input("you: ")
  response=generate_response(user_input)
  print("chatbot:", response)
    