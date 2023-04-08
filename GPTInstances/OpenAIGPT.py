import openai
import os

class OpenAIGPT:
    def __init__(self, engine="text-davinci-003"):
        # Init OpenAI API key
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        self.engine = engine

    def schedulle_finetune(self, training_files):
        try:
            #Configure the fine tunning model
            training_configuration = {
                "model": "text-embedding-ada-002",
                "model_name": "my-dora-ada-001",
                "description": "Model to classify DevOps articles",
                "training_files": training_files,
                "finetune": True
            }
            #schedule the fine tunning model
            return openai.FineTune.create(training_configuration)
        except openai.APIError as e:
            # Return the error message
            return f"Error: {e.json_body['error']}"

    def prompt(self, prompt):
        try:
            # Make API call to OpenAI
            response = openai.Completion.create(
                engine=self.engine,
                prompt=prompt,
                max_tokens=1024
            )
       
            # Extract and return the response string
            return response.choices[0].text.strip()
            
        except openai.APIError as e:
            # Return the error message
            return f"Error: {e.json_body['error']}"

    def generate_embedding(self,text):
        try:
            # Make API call to OpenAI to generate an embedding
            response = openai.Embedding.create(
                model = "text-embedding-ada-002", 
                input = text
            )

            # Extract and return the embedding vector
            embedding = response['data'][0]['embedding']
            return embedding

        except openai.APIError as e:
            # Return the error message
            return f"Error: {e.json_body['error']}"