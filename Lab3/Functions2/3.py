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

#Write a function that takes a category name and returns just those movies under that category.

def category(movies, name):
    list = []
    for i in movies:
        m = i['category']
        if name.lower() == m.lower():
            list.append(i)
    return list


n = input()
print(f'In the {n} are: ')
if n == 'Thriller':
    list = category(movies, 'Thriller')
elif n == 'Action':
    list = category(movies, 'Action')
elif n == 'Adventure':
    list = category(movies, 'Adventure')
elif n == 'Drama':
    list = category(movies, 'Drama')
elif n == 'Romance':
    list = category(movies, 'Romance')
elif n == 'War':
    list = category(movies, 'War')
elif n == 'Crime':
    list = category(movies, 'Crime')
elif n == 'Comedy':
    list = category(movies, 'Comedy')
elif n == 'Suspense':
    list = category(movies, 'Suspense')
for elem in list:
    print(elem)
