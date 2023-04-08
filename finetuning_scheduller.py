from GPTInstances import OpenAIGPT

# Start the GPT Instance we want to use
gpt = OpenAIGPT.OpenAIGPT()

def finetune():
    try:
        # Make API call to OpenAI
        response = gpt.finetune(["./data/finetuning_data.json"]"])
        return response
    except Exception as e:
        print(f"Error: {e}")