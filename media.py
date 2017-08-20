'''The movie class'''

class Movie():
    '''The movie class constructor with parameters the title,
    description, image, and movie trailer'''
    def __init__(self, MovieTrailer):
        self.title = MovieTrailer.title
        self.storyline = MovieTrailer.description
        self.poster_image_url = MovieTrailer.image
        self.trailer_youtube_url = MovieTrailer.video


class MovieTrailer:
	def __init__(self, title, description, image, video):
		self.title = title
		self.description = description
		self.image = image
		self.video = video

	def get_media(self):
		return Movie(self)

