from gpt3_interaction import chat_with_gpt3

# Initialize conversation with a system message
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Goodbye!")
        break

    # Add user message to conversation
    conversation.append({"role": "user", "content": user_input})

    # Get GPT-3.5-turbo response
    response_text = chat_with_gpt3(conversation)

    # Add GPT-3.5-turbo response to conversation
    conversation.append({"role": "assistant", "content": response_text})

    # Print assistant's response
    print("Assistant:", response_text)
