create or replace function find_closest_article(embedding vector(1536), match_threshold float, match_count int)
returns table (title text, content text, similarity float)
language plpgsql
as $$
#variable_conflict use_variable
begin
  return query
  select
    articles.title,
    articles.content,
    (articles.embedding <#> embedding) * -1 as similarity
  from articles

  -- The dot product is negative because of a Postgres limitation, so we negate it
  where (articles.embedding <#> embedding) * -1 > match_threshold

  -- OpenAI embeddings are normalized to length 1, so
  -- cosine similarity and dot product will produce the same results.
  -- Using dot product which can be computed slightly faster.
  --
  -- For the different syntaxes, see https://github.com/pgvector/pgvector
  order by articles.embedding <#> embedding
  
  limit match_count;
end;
$$;