import requests
from bs4 import BeautifulSoup

response = requests.get("http://unkno.com")
# print(response.content)
soup = BeautifulSoup(response.content, "html.parser")
content = soup.find_all("div", id="content")
print(content[0].getText())

