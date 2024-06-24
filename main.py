import requests

from flask import Flask, request, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def converter():
    first = "рубль"
    second = "гривны"

    url = f"https://www.google.com/search?q=конвертер+валют+{first}+{second}&sca_esv=d9eef79a7f076b3b&sxsrf=ADLYWIIC9WZeQqd3YV-IiULmXlNKoG2K6g%3A1719267042482&ei=4u55ZqCPHZKA1fIPooeziA0&oq=%D0%BA%D0%BE%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%B5%D1%80+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82&gs_lp=Egxnd3Mtd2l6LXNlcnAiHdC60L7QvdCy0LXRgNGC0LXRgCDQstCw0LvRjtGCKgIIATIHECMYsAMYJzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIZEC4YgAQYsAMY0QMYQxjHARjIAxiKBdgBATIZEC4YgAQYsAMY0QMYQxjHARjIAxiKBdgBATIWEC4YgAQYsAMYQxjUAhjIAxiKBdgBAUjxFFAAWABwAXgBkAEAmAEAoAEAqgEAuAEDyAEAmAIBoAIImAMAiAYBkAYMugYECAEYCJIHATGgBwA&sclient=gws-wiz-serp"

    # хиадер делает вид, что ты человек, что бы можно было сделать запрос. #!Без него не работает
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

    # получаем страницу с конвертором валют
    fullPage = requests.get(url, headers=headers)

    # парсим содержимое страницы
    soup = BeautifulSoup(fullPage.content, 'html.parser')

    # находим и выводим цифру конвертации
    convert = soup.find("span", {"class": "DFlfde SwHCTb", "data-precision":"2"})

    return render_template('index.html', convert=convert.text)
app.run(debug=True)