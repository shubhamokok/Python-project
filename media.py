import webbrowser

class Movie():
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__ ( self, movie_tittle, movie_storyline, poster_image,
                   trailer_youtube):
        self.tittle = movie_tittle
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
 
