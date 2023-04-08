# GPTDiscovery

This repository conteins experiments for the OpenAI API's. This code was design to be easy to understand concepts, that is why it is using only the open AI libraries. For production use refer to libraries to help with each operation here. At this moment I can recommend the [LangChaing](https://github.com/hwchase17/langchain), it is a comprehensive framwork to solve multiple of the use cases explored here.

## Setup your environment
First of all to run the codes in this repository you need the following.

### Python
I've use python 3 for all the examples in this repository. The version that I have installed is the Python 3.8.9. But there are no specifc elements of this version, so any Python 3 version should work.

### OpenAI
You will need a OpenAI account, and api key to be able to run the experiments in this code. For more information on how to get your account and api key visit [OpenAi.com](https://openai.com/)

### Database 
For the use of embeddings the code require and database that can handle vectors (storage and operations). [SupaBase](https://supabase.com/) was selected for this example because is a free alternative of Firebase, that is implemented on top of PostGress and allow us to use the [PgVector] (https://github.com/pgvector/pgvector) extension. You will need to create your account on it and activate the Vector Extension

### Setting up your environment
To start create all the accounts and get all the api keys necessary.

On the Supabase, run the scripts on the "migrations" folder, that will create the Table and Function required to run the embeedings example.

After you have created the database, you need to add 3 environment variables containing the necessary keys, here is an example.

```
export OPENAI_API_KEY=<OPENAI_API_KEY>
export SUPABASE_URL=<MY_SUPABASE_URL>
export SUPABASE_URL=<MY_SUPABASE_URL>
```
        
## Simple exploration
All code that start with a simple_, is a simple exploration, it just call the OpenAI API and explore the result, these codes are designed to give you a view on how to explore the API's.

## Embeddings
All code that starts with embeddings_, are related to the embeddings experiment. The full solution extract the DevOps Documentation fom Dora (Google) and generate Markdown sections that will be used as the base data.

The following are the components of the solution
* **embeddings_extractor.py** : This component is responsabile for parsing the HTML pages of the DevOps Documentation, Break it down in sections, get the embeddings of each section and store it in the Supabase
* **embeddings_findrelated.py** : This component can be used to explore the embedding database. This will get the embedding of the prompt and use dot product to find the closest meaninful sections of the DevOps Documentation, and return the title.
* **embeddings_enrich_prompt.py** : This component is a evolutio of the simple_prompt.py, on this version the related content found using the find_related method is added to the prompt to be used as context to build the response.

## Fine tuning
All code that starts with finetuning_, are related to the examples of finetuing. We are generating the data files that need to be used for fine tuning of the model. The specific usecase we are implementing is a classification. Where we are using the sections of DevOps Content to determine what is the best category for a future prompt.

The data generaged is for designed to be for learning purpose only, for a real classification fine tunning it would be required a more substantial training dataset.