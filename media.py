import webbrowser

class Movie():
    ## This below can be accessed via the doc method on Classes (Media.__doc__)
    """ This class provides a way to store movie related information """

    ## This is a class variable which is also a constant
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, cast):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.cast = cast

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
