class Movie():
	# Movie class for objects holding details about movies (like title, poster image url, trailer url etc.)

	def __init__(self, movie_title, movie_storyline, poster_image, details_url, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.details_url = details_url
		self.trailer_youtube_url = trailer_youtube
