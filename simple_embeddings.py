from GPTInstances import OpenAIGPT

# Start the GPT Instance we want to use
gpt = OpenAIGPT.OpenAIGPT(engine="text-embedding-ada-002")

# Main loop for taking user input and generating responses
while True:
    # Take user input for the prompt
    prompt = input("You: ")
    
    # Call the function with the user's prompt
    vector = gpt.generate_embedding(prompt)
    
    # Print the generated text
    print(f"Embedding size: {len(vector)}")
    print(f"Embedding: {vector}")