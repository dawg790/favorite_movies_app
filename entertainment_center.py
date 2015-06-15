import fresh_tomatoes
import media

# My Movie Instances below, instantiated from the Media Class
star_wars = media.Movie("Star Wars",
                        "The Force Awakens - Episode VII",
                        "https://upload.wikimedia.org/wikipedia/en/7/73/Forceawakenspromo.jpg",
                        "https://www.youtube.com/watch?v=OprvFVBGtEc",
                        "Harrison Ford, Mark Hamill, Carrie Fisher")

interstellar = media.Movie("Interstellar",
                            "Humans search for an inhabitable planet",
                            "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                            "https://www.youtube.com/watch?v=lRTTCrdzKAo",
                            "Matthew McConaughey, Michael Caine")

skyfall = media.Movie("Skyfall",
                      "Ian Fleming's 007 Bond adventure",
                      "http://www.impawards.com/2012/posters/skyfall.jpg",
                      "www.youtube.com/watch?v=6kw1UVovByw",
                      "Daniel Craig")

swingers = media.Movie("Swingers",
                        "Cocktails first, questions later.",
                        "https://upload.wikimedia.org/wikipedia/en/9/91/Swingers_ver2.jpg",
                        "https://www.youtube.com/watch?v=nWCct8XbQD0",
                        "Vince Vaughn, Jon Favreau")

braveheart = media.Movie("Braveheart",
                         "William Wallace fights for Scottish Independence",
                         "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
                         "https://www.youtube.com/watch?v=wj0I8xVTV18",
                         "Mel Gibson")

jaws = media.Movie("Jaws",
                    "A shark terrorizes a summer community",
                    "https://upload.wikimedia.org/wikipedia/en/e/eb/JAWS_Movie_poster.jpg",
                    "https://www.youtube.com/watch?v=U1fu_sA7XhE",
                    "Richard Dreyfus, Roy Schneider, Robert Shaw")


# Adding my movie instances to the movies array, to be used in the open_movies_page method below
movies = [star_wars, interstellar, skyfall, swingers, braveheart, jaws]

# Calling the open_movies_method from the fresh_tomatoes file
fresh_tomatoes.open_movies_page(movies)