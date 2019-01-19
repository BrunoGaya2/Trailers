import fresh_tomatoes
import media

avengers_infinite_war = media.Movie("Avengers: Infinite War",
                        "A story of a group of hereos facing the greastes threat to the earth",
                        "https://upload.wikimedia.org/wikipedia/pt/9/90/Avengers_Infinity_War.jpg",
                        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")                        


the_lord_of_the_rings = media.Movie("The Lord of the Rings",
                     "A fight for the middle earth",
                     "https://upload.wikimedia.org/wikipedia/pt/thumb/0/0c/The_Fellowship_Of_The_Ring.jpg/250px-The_Fellowship_Of_The_Ring.jpg",
                     "https://www.youtube.com/watch?v=V75dMMIW2B4")


the_hobbit = media.Movie("A unexpected journey",
                         "A hobbit going into a adventure",
                         "https://upload.wikimedia.org/wikipedia/en/b/b3/The_Hobbit-_An_Unexpected_Journey.jpeg",
                         "https://www.youtube.com/watch?v=ZEOM13UyZ0A")


mib = media.Movie("MIB",
                  "Fighting Aliens to protect Earth",
                  "https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Men_in_Black_Poster.jpg/220px-Men_in_Black_Poster.jpg",
                  "https://www.youtube.com/watch?v=HYUd7AOw_lk")


the_incredibles = media.Movie("The Incredibles",
                              "Heroes living among us",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/The_Incredibles.jpg/220px-The_Incredibles.jpg",
                              "https://www.youtube.com/watch?v=i5qOzqD9Rms")


the_lion_king = media.Movie("The Lion King",
                           "A Lion will be a king",
                           "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                           "https://www.youtube.com/watch?v=_ujGv5dhGfk")

movies = [avengers_infinite_war, the_lord_of_the_rings, the_hobbit, mib, the_incredibles, the_lion_king]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VALID_RATINGS)
                                
