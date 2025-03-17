from fastapi import FastAPI
from searcher import google_search

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/search/")
def search_query(query: str):
    results = google_search(query)
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) #uvicorn main:app --reload 
