from GPTInstances import OpenAIGPT
from Repository import VectorRepository

# Start the GPT Instance we want to use
gpt = OpenAIGPT.OpenAIGPT()
repo = VectorRepository.VectorRepository()

# Main loop for taking user input and generating responses
while True:
    # Take user input for the prompt
    prompt = input("You: ")
    
    #find closest article
    prompt_embedding = gpt.generate_embedding(prompt)
    response = repo.find_closest_article(prompt_embedding)
    print(f"Found {len(response.data)} sections to be considered")
    
    #show the identified articles
    for article in response.data:
        print(f"Article: {article['title']} has a similarity of {article['similarity']}")
