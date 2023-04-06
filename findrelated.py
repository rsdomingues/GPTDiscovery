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
    response = repo.find_closest_article(prompt_embedding)
    
    for article in response.data:
        print(f"Article: {article['title']} has a similarity of {article['similarity']}")
