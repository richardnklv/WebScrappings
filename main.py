from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    title_html_tags = soup.find_all('h1')
    for title in title_html_tags:
        print(title.text)
