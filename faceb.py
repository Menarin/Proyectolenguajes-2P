
import requests_html

session = requests_html.HTMLSession()
r = session.get('https://touch.facebook.com/pg/espol/posts/?ref=page_internal&mt_nav=0')
r.html.render(wait=2, scrolldown=20, sleep=2)
items = r.html.find('article')
cont = 0
#print(items)
#https://www.facebook.com/espol/photos/a.10151149463443286/10156523918298286/?type=3
for item in items:

    try:
        print('\n' + item.find('abbr')[0].text)
        print(item.find('span p')[0].text)
        print(item.find('header a')[0].attrs['href'])
    except KeyError:
        pass
    '''
    for post in posts:
        try:
            print(post.find('abbr'))
            print(post.find('span p'))
        except KeyError:
            pass
    '''
   # posts = item.find('div')
    #print(posts)
    cont += 1

print(cont)
