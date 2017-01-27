#importing webbrowser package to use .open function
import webbrowser
#define movie class
class Movie():
    #initialising variables
    def __init__(self, movie_title, movie_storyline,poster_image,
                 trailer_youtube):
        self.title=movie_title
        self.story_line=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
    #instance method
    def show_Trailer(self):
        webbrowser.open(self.trailer_youtube_url)
