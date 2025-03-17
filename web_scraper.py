import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("title").text if soup.find("title") else "No Title"
    paragraphs = [p.text for p in soup.find_all("p")]

    return {"title": title, "content": " ".join(paragraphs)}

# Example Usage
url = "https://example.com"
data = scrape_website(url)
print(data)
