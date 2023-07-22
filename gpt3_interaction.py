import openai

# Set your API key here
openai.api_key = "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"

def chat_with_gpt3(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )
    return response['choices'][0]['message']['content']





