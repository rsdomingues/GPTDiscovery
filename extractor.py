import requests
from bs4 import BeautifulSoup
from GPTInstances import OpenAIGPT
from Repository import VectorRepository

# Start the GPT Instance we want to use
gpt = OpenAIGPT.OpenAIGPT(engine="text-embedding-ada-002")
repo = VectorRepository.VectorRepository()

dora_articles = [ 'https://cloud.google.com/solutions/devops/devops-tech-test-automation', 
    'https://cloud.google.com/solutions/devops/devops-tech-deployment-automation', 
    'https://cloud.google.com/solutions/devops/devops-tech-trunk-based-development', 
    'https://cloud.google.com/solutions/devops/devops-tech-shifting-left-on-security', 
    'https://cloud.google.com/solutions/devops/devops-tech-architecture', 
    'https://cloud.google.com/solutions/devops/devops-tech-teams-empowered-to-choose-tools', 
    'https://cloud.google.com/solutions/devops/devops-tech-continuous-integration', 
    'https://cloud.google.com/solutions/devops/devops-tech-version-control', 
    'https://cloud.google.com/solutions/devops/devops-tech-test-data-management', 
    'https://cloud.google.com/solutions/devops/devops-tech-database-change-management', 
    'https://cloud.google.com/solutions/devops/devops-tech-cloud-infrastructure', 
    'https://cloud.google.com/solutions/devops/devops-tech-code-maintainability', 
    'https://cloud.google.com/architecture/devops/devops-tech-continuous-delivery', 
    'https://cloud.google.com/solutions/devops/devops-measurement-wip-limits', 
    'https://cloud.google.com/solutions/devops/devops-measurement-visual-management', 
    'https://cloud.google.com/solutions/devops/devops-measurement-proactive-failure-notification', 
    'https://cloud.google.com/architecture/devops/devops-measurement-monitoring-systems', 
    'https://cloud.google.com/architecture/devops/devops-measurement-monitoring-and-observability', 
    'https://cloud.google.com/solutions/devops/devops-process-working-in-small-batches', 
    'https://cloud.google.com/solutions/devops/devops-process-work-visibility-in-value-stream', 
    'https://cloud.google.com/solutions/devops/devops-process-customer-feedback', 
    'https://cloud.google.com/solutions/devops/devops-process-team-experimentation', 
    'https://cloud.google.com/solutions/devops/devops-process-streamlining-change-approval', 
    'https://cloud.google.com/solutions/devops/devops-culture-learning-culture', 
    'https://cloud.google.com/solutions/devops/devops-culture-westrum-organizational-culture', 
    'https://cloud.google.com/solutions/devops/devops-culture-job-satisfaction', 
    'https://cloud.google.com/architecture/devops/devops-culture-transformational-leadership'
]

def get_articles(articles):
    for url in articles:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            #parse the article
            article = soup.find('article').get_text()
            title = soup.find('h1', {'class': 'devsite-page-title'}).get_text()
            
            # Call the function with the user's prompt
            vector = gpt.generate_embedding(article)
            
            # Print the generated text
            print(f"'{title}' -> Embedding Generated with size: {len(vector)}")
            
            # Save the vector to the database
            repo.save(title, vector, article)

            print(f"'{title}' -> Embedding Saved")


        except Exception as e:
            print(f"Error with {e}")


if(__name__ == "__main__"):
    get_articles(dora_articles)