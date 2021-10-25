current_movies = {'The Grinch':'11:00AM',
                   'Rudolph':'1:30PM',
                   'Frosty: The Snowman':'3:00PM'}

print('We are showing the following movies:')
for key in current_movies:
    print(key)

movie = input('What movie would you like the show time for?\n')

showtime = current_movies.get(movie)

print(showtime)