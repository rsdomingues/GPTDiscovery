
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
    
    #generate context
    context_info = ""
    for article in response.data:
        context_info += f"article['content'] \n---\n"

    #generate expert prompt
    expert_prompt = f""" You are a very enthusiastic DevOps specialist who loves
        to help people! Given the following sections from the Dora
        documentation, answer the question using only that information,
        outputted in markdown format. If you are unsure and the answer
        is not explicitly written in the documentation, say
        'Sorry, I don't know how to help with that.'
        Context sections:{context_info}
        Question: {prompt}
        """
    
    # Call the function with the user's prompt
    response = gpt.prompt(expert_prompt)
    
    # Print the generated text
    print(f"ChatGPT: {response}")

