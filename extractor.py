import requests
from bs4 import BeautifulSoup, PageElement, Tag
from GPTInstances import OpenAIGPT
from Repository import VectorRepository

# Start the GPT Instance we want to use
gpt = OpenAIGPT.OpenAIGPT()
repo = VectorRepository.VectorRepository()

dora_articles = [ 
    'https://cloud.google.com/solutions/devops/devops-tech-test-automation', 
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


def clean_text(text):
    return text.replace("\n", " ").replace("\r", " ").replace("\t", " ")

def get_sections(article):
    section = ""
    sections = list()
    should_capture = False
    
    for element in article.descendants:
        
        if(element.name == 'h1'):
            section += f"# {clean_text(element.get_text())}\n\n"
            should_capture = True
        
        if (element.name == 'h2'):
            sections.append(section)
            section = f"# {clean_text(element.get_text())}\n\n"
            if(element.get_text() == "What's next"):
                break
        
        if (should_capture and type(element) == Tag):
            if (element.name == 'p'):
                section += f"{clean_text(element.get_text())}\n\n"
            if (element.name == 'li'):
                section += f" * {clean_text(element.get_text())}\n"
    
    return sections

def get_articles(urls):
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            #parse the article
            article: PageElement = soup.find('article')
            title = clean_text(soup.find('h1', {'class': 'devsite-page-title'}).get_text())
            sections = get_sections(article)
            
            # Print the generated text
            print(f"Procesing page '{title}' that has {len(sections)} sections")

            for section in sections:
                # Call the function with the user's prompt
                vector = gpt.generate_embedding(section)
                
                # Refresh the content of the repository
                repo.dump_repository()
                repo.save(title, vector, section)

                print(f"'{title}' -> Embedding Saved")

        except Exception as e:
            print(f"Error with {e}")

if(__name__ == "__main__"):
    get_articles(dora_articles)