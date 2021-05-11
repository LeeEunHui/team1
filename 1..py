import matplotlib.pyplot as plt
import matplotlib
from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%97%AD%EB%8C%80%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84') as response:
    soup = BeautifulSoup(response,'html.parser')
    #print(soup)

    movie = soup.find('div',{'class':'_content'})

    movie_name = movie.select('strong')
    movie_name1 = []
    for i in movie_name:
        movie_name1.append(i.text)
    print(movie_name1)

    movie_poplaration = movie.select('dd')
    movie_poplaration1 = []
    for i in movie_poplaration:
        movie_poplaration1.append(i.text)
    print( movie_poplaration1)

    figure = []
    for i in range(len(movie_poplaration1)):
        if i % 2 == 1:
            k = movie_poplaration1[i]
            p = k[0] + k[1] + k[3] + k[4] + k[5] + k[7] + k[8] + k[9]
            p = int(p)
            figure.append(p)

    x = [0, 1, 2, 3, 4, 5, 6, 7]
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.bar(x, figure)
    plt.xticks(x, movie_name1)
    plt.show()