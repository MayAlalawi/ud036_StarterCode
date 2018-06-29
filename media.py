import webbrowser
class Movie():
    """ class Movie to  store my favorite movies
    including movie title, poster image URL
    and a YouTube link to the movie trailer.

    Attributes:
    title: a string of the movie title.
    poster_image_url: a string containig the poster url.
    trailer_youtube_url: a string containig the moive youtube url.
    
    """

    def __init__(self,movie_title,poster_image,youtube_url):
        """Inits Movie with
        title=movie_title
        poster_image_url=poster_image
        trailer_youtube_url=youtube_url
        """
    
        self.title=movie_title   
        self.poster_image_url=poster_image
        self.trailer_youtube_url=youtube_url
        
    def show_trailer(self):
        """a method to show the movie youtube trailer
         It use webbrowser module to open the moive url
        """
        webbrowser.open(self.trailer_url)
