import requests
import bs4

def get_reddit_links(link, pages=5):
    current_page = 1
    links = []
    while current_page <= pages:
        if current_page == 1:
            res = requests.get(link + '/nsfw.html')
        else:
            res = requests.get(link + '/nsfw' + str(current_page) + '.html')
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # Find all the links under the span tag of `subreddit-url`
        l = soup.select('span.subreddit-url a')
        for i in l:
            links.append(i['href'])
        # Get the next page
        current_page += 1
    return links

if __name__ == '__main__':
    l = get_reddit_links('https://redditlist.com')
    with open('data/nsfw/nsfw_sites.txt', 'a') as f:
        for i in l:
            f.write(i + '\n')
