import requests
from bs4 import BeautifulSoup as BS

def pars():
    links = {}
    r = requests.get('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83')

    while(True):
        html = BS(r.content, 'html.parser')
        for el in html.select('.mw-category-group'):
            letter = el.select('h3')[0].text
            if letter == 'A':
                return links
            link = el.select('a')
            
            if links.get(letter):
                links[letter] += len(link)
            else:
                links[letter] = len(link)
        next_elem = html.select('#mw-pages a:last-child')[-1]
        r = requests.get('https://ru.wikipedia.org' + next_elem['href'])
    
# ------------------------------------------------------------
task = lambda arr: None if arr[-1] == '1' else arr.find('0')

def main():
    print('task 1 answer:', task("111111111111111111111111100000000")) 
    pets = pars()
    for name, item in pets.items():
        print(name + ':', item)
    

main()