import requests
from bs4 import BeautifulSoup
from GPTInstances import OpenAIGPT
from Repository import VectorRepository

# Start the GPT Instance we want to use
gpt = OpenAIGPT.OpenAIGPT(engine="text-embedding-ada-002")
repo = VectorRepository.VectorRepository()


# Main loop for taking user input and generating responses
while True:
    # Take user input for the prompt
    prompt = input("You: ")
    
    #find closest article
    prompt_embedding = gpt.generate_embedding(prompt)
    article = repo.find_closest_article(prompt_embedding)

    # Call the function with the user's prompt
    response = gpt.prompt(prompt)
    
    
    # Print the generated text
    print(f"ChatGPT: {response}")