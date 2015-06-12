import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A movie about toys coming to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

skyfall = media.Movie("Skyfall",
                      "Ian Fleming's 007 Bond adventure",
                      "http://www.impawards.com/2012/posters/skyfall.jpg",
                      "www.youtube.com/watch?v=6kw1UVovByw")

## movies = [toy_story, avatar, skyfall]
## fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
