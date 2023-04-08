from Repository import VectorRepository

#create a repo instance
repo = VectorRepository.VectorRepository()

def clean_prompt(prompt):
    #clean the prompt text
    return prompt.replace("\n", " ").replace("\r", " ").replace("\t", " ").replace("\"", "\'")

def clean_title(title):
    #clean the title text
    return title.replace("DevOps tech: ","").split(" | ")[0]

def generage_fine_tunning_data():

    fine_tunning_data = list()    
    
    #get all the articles from the database
    articles = repo.get_all_articles()

    print(f"Total articles: {len(articles[1])}")
    for article in articles[1]:
        #generating the fine tunning model using the template {"prompt": "<prompt text>", "completion": "<ideal generated text>"}
        data = "{\"prompt\": \""
        data += clean_prompt(article["content"])
        data += "\", \"completion\": \""
        data += clean_title(article["title"])
        data += "\"}"

        fine_tunning_data.append(data)

    for data in fine_tunning_data:
        print(data)

if(__name__ == "__main__"):
    generage_fine_tunning_data()