import requests
from bs4 import BeautifulSoup
# url= "https://jsonplaceholder.typicode.com/posts"
# data ={
#     "title": 'foo',
#     "body":'bar',
#     "userID": 1,
# }
# headers={
#     'Context-type': 'application/json; charset=UTF-8',
# }
# response = requests.post(url, headers=headers, json=data)
# print(response.text)


url= "https://www.codewithharry.com/blogpost/the-term-pip-is-not-recognized-error/"
r= requests.get(url)
soup= BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)
# print(r.text)