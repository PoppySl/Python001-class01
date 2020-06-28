from bs4 import BeautifulSoup as bs
import requests
import pandas
import os


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
headers = {
    'User-Agent': user_agent
}
url = 'https://maoyan.com/films?showType=3'
response = requests.request("GET", url, headers=headers)


# with open('../text.html', 'r') as f:
#     data = f.read()

bs_info = bs(response.text, 'html.parser')

items = bs_info.find_all(class_='movie-hover-info', limit=10)

movie_list = []
for item in items:
    movie_name = item.find(class_='name').text
    movie_info = item.find_all(class_='movie-hover-title')
    movie_type = movie_info[1].text.split()
    movie_time = movie_info[3].text.split()
    movie_link = item.parent.get('href')
    moive = {
        '电影名称：': movie_name,
        '链接：': movie_link,
        movie_type[0]: movie_type[1],
        movie_time[0]: movie_time[1]
    }
    movie_list.append(moive)

movie = pandas.DataFrame(movie_list)
movie.to_csv('./movie.csv', index=False)