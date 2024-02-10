import google.generativeai as genai
from constants import api_key

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while True:
    user_input = input("Enter the query (type 'exit' to end): ")
    if user_input.lower() == 'exit':
        break
    response =chat.send_message(user_input, stream=True)
    for chunk in response:
        print(chunk.text)
        print("_" * 80)

print(chat.history)
