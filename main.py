from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from fastapi import FastAPI, Query
import pandas as pd
import uvicorn

df = pd.read_csv('./gutenberg_book_deer.csv')

df['Key Words'] = df['Title'] + df['Subject']
df['Key Words'] = df['Key Words'].fillna('').astype(str)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Key Words'])

app = FastAPI()

@app.get('/')
def root_route():
    return {"message": "Project Gutenberg Book Recommendation. Access the /query endpoint to test recommendations."}

@app.get('/query', response_model=dict)
def query_route(query: str = Query(description="Query")):
    query_vec = vectorizer.transform([query])

    similarity_scores = linear_kernel(query_vec, X).flatten()
    sorted_indices = similarity_scores.argsort()[::-1]
    sorted_indices = sorted_indices[:10]
    indices = [i for i in sorted_indices if similarity_scores[i] > 0]

    results = []
    for i in indices:
        results.append({
            "title": df.iloc[i]['Title'],
            "author": df.iloc[i]['Author'],
            "content": df.iloc[i]['Subject'],
            "url": df.iloc[i]['URL'],
            "relevance": float(similarity_scores[i])
        })
    
    return {"results": results, "message": "OK"}

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=34567, reload=True)