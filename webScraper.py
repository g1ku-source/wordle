from bs4 import BeautifulSoup
import requests

file = open("words.txt", "a")

url = "https://www.bestwordlist.com/5letterwordspage15.htm"
result = requests.get(url=url)

document = BeautifulSoup(result.text, "html.parser")
spans = document.find_all("span", {"class": "mot2"})

for span in spans:
    word = span.text
    index = 0
    for character in word:
        file.write(character.lower())
        if character == ' ' or character == '\n':
            file.write("\n")
file.write('\n')
