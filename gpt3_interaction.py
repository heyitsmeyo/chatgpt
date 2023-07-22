import openai

openai.api_key = ""

def chat_with_gpt3(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )
    return response['choices'][0]['message']['content']





