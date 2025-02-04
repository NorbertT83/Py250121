print("1. feladat:")
while True:
    a = int(input('Adja meg az "a" számot: '))
    b = int(input('Adja meg a "b" számot: '))
    if a == 0 or b == 0:
        break
    result = (a+b) / (a*b)
    print(f"({a}+{b})/({a}*{b}) = {result}")
    if result % 1 == 0:
        print("Egész")
    else:
        print("Valós")


print("2. feladat:")
from random import randint

num_to_guess = randint(1, 100)
nr_of_guesses = 0
print("Gondoltam egy számra 1 és 100 között!")

guess = -1
while guess != num_to_guess:
    guess = int(input("Mi a tipped? "))
    nr_of_guesses += 1
    if guess > num_to_guess:
        print("Túl magas!")
    elif guess < num_to_guess:
        print("Túl alacsony!")
    print("Eltaláltad! :)")
print("A tippek száma: ",nr_of_guesses)
if nr_of_guesses > 7:
    print("Legközelebb gondold át a stratégiádat, megy ez jobban is!")


print("3. feladat:")

class Movies:
    def __init__(self, data):
        dataset = data.strip().split(";")
        self.title = dataset[0]
        self.release = int(dataset[1])
        self.genre = dataset[2].strip().split(",")

movies = []
with open("filmek.txt", encoding="utf-8") as file:
    for row in file:
        movies.append(Movies(row))

print("3.1: Filmek száma: ", len(movies))

this_century_movies = []
for movie in movies:
    if movie.release > 2000:
        this_century_movies.append(movie)
print(f"3.2: 21. századi filmek száma: {len(this_century_movies)} db")

oldest = 0
for i in range(1, len(movies)):
    if movies[i].release < movies[oldest].release:
        oldest = i
print("3.3: Legkorábbi film: ", movies[oldest].title)

searched_genre = input("3.3: Írja be a keresett műfaj nevét:  ")
print(f"A(z) {searched_genre} műfajmegjelölésű filmek címei:")
for movie in movies:
    if searched_genre in movie.genre:
        print("\t -", movie.title)
