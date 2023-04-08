import os
from supabase import create_client, Client

class VectorRepository:
    def __init__(self):
        # Init Supabase API key
        url = os.environ.get("SUPABASE_URL")
        key= os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)

    def get_all_articles(self):
        try:
            # Make API call to Supabase
            data, count = self.supabase.table('articles').select("*").execute()
            
            # Extract and return the response string
            return data
        except Exception as e:
            # Return the error message
            return f"Error: {e}"

    def save(self, title, vector, content):
        try:
            # Make API call to Supabase
            data, count = self.supabase.table('articles').insert({"title": title, "embedding":vector, "content": content}).execute()
            
            # Extract and return the response string
            return count
        except Exception as e:
            # Return the error message
            return f"Error: {e}"
        
    def dump_repository(self):
        try:
            # Make API call to Supabase
            data, count = self.supabase.table('articles').delete("*").execute()
            
            # Extract and return the response string
            return count
        except Exception as e:
            # Return the error message
            return f"Error: {e}"
        
    def find_closest_article(self, vector):
        try:
            # Make API call to Supabase
            data = self.supabase.rpc("find_closest_article", {"embedding":vector, "match_threshold":0.35, "match_count":10}).execute()
            
            # Extract and return the response string
            return data
        except Exception as e:
            # Return the error message
            return f"Error: {e}"