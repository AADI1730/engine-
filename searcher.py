from googlesearch import search

def google_search(query, num_results=5):
    """Fetch top Google search results for a query."""
    results = []
    try:
        for link in search(query, num_results=num_results):
            results.append({"title": link, "url": link})
    except Exception as e:
        print("⚠ Error fetching Google results:", e)
    
    return results

# Example Usage
query = input("Enter search query: ")
results = google_search(query)

if results:
    print("🔍 Search Results:")
    for result in results:
        print(result["title"])
else:
    print("⚠ No results found. Try a different query.")
