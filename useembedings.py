
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
    
    #generate context
    context_info = ""
    for article in response.data:
        context_info += f"{article['content']}---\n"

    #generate expert prompt
    expert_prompt = "Positioned as a DevOps engineer, you are asked to provide a answer to a question,"
    expert_prompt += f"you need to consider the following:\n {context_info}"
    expert_prompt += f"\n The question you must answer is: {prompt}"

    # Call the function with the user's prompt
    response = gpt.prompt(expert_prompt)
    
    # Print the generated text
    print(f"\n\n{response}")
