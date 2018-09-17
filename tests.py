
import requests_html

session = requests_html.HTMLSession()
r = session.get('https://www.instagram.com/espol1/tagged')
r.html.render(wait=3, scrolldown=5, sleep=1)
items = r.html.find('article')
cont = 0

for item in items:
    posts = item.find('a')
    for post in posts:
        cont += 1
        print("\nLink: https://www.instagram.com" + post.attrs['href'])
        try:
            print(post.find('img')[0].attrs['alt'])
        except KeyError:
            pass

print(cont)
