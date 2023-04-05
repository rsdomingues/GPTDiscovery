import openai
import os

class OpenAIGPT:
    def __init__(self, engine="text-davinci-003"):
        # Init OpenAI API key
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        self.engine = engine

    def prompt(self, prompt):
        try:
            # Make API call to OpenAI
            response = openai.Completion.create(
                engine=self.engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7
            )
       
            # Extract and return the response string
            return response.choices[0].text.strip()
            
        except openai.APIError as e:
            # Return the error message
            return f"Error: {e.json_body['error']}"
        
    import openai

    def generate_embedding(self,text):
        try:
            # Make API call to OpenAI to generate an embedding
            response = openai.Embedding.create(
                model=self.engine, 
                input = text
            )

            # Extract and return the embedding vector
            embedding = response['data'][0]['embedding']
            return embedding

        except openai.APIError as e:
            # Return the error message
            return f"Error: {e.json_body['error']}"