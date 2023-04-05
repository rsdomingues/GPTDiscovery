from GPTInstances import OpenAIGPT

# Start the GPT Instance we want to use
openai = OpenAIGPT.OpenAIGPT()

# Main loop for taking user input and generating responses
while True:
    # Take user input for the prompt
    prompt = input("You: ")
    
    # Call the function with the user's prompt
    response = openai.prompt(prompt)
    
    # Print the generated text
    print(f"ChatGPT: {response}")