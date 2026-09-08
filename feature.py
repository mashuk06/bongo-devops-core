import requests
from bs4 import BeautifulSoup
url = input("Enter URL: ")
soup = BeautifulSoup(requests.get(url).text, "html.parser")
print("Title:", soup.title.text.strip() if soup.title else "N/A")
print("\nLinks:")
for a in soup.find_all("a", href=True): print(a.get_text(strip=True), "->", a["href"])
