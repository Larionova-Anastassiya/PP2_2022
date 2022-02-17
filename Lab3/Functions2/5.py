movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]

#Write a function that takes a category and computes the average IMDB score.
def category(movies, name):  # по категориям как в 3 задаче проверит
    list = []
    for i in movies:
        m = i['category']
        if name.lower() == m.lower():
            list.append(i)
    return list


def score(movies):
    Average = 0
    totaly = len(movies)  # количество фильмов общее
    for i in movies:
        Average = Average + i['imdb']  # будет к 0 прибавлять все рейтинги для общей суммы
    Average = Average / totaly  # найдет среднее значение для рейтингов в задаче 4
    return Average


def Average(movies, name): #найдет среднее значение рейтинга именно категории
    movie = category(movies, name)
    Average = score(movie)
    return Average


n = input()
print(f'Average IMDB {n} category is: ')
if n == 'Thriller':
    ans = Average(movies, 'Thriller')
elif n == 'Action':
    ans = Average(movies, 'Action')
elif n == 'Adventure':
    ans = Average(movies, 'Adventure')
elif n == 'Drama':
    ans = Average(movies, 'Drama')
elif n == 'Romance':
    ans = Average(movies, 'Romance')
elif n == 'War':
    ans = Average(movies, 'War')
elif n == 'Crime':
    ans = Average(movies, 'Crime')
elif n == 'Comedy':
    ans = Average(movies, 'Comedy')
elif n == 'Suspense':
    ans = Average(movies, 'Suspense')
print(ans)
