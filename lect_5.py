
class Movie:
	pass


#print(Movie())
#print(Movie)



class Movie:
	max_timekeeping_min = 160
	max_timekeeping_hours = 3

#var = Movie()
#print(var.max_timekeeping_min)


class Movie:
	max_timekeeping_min = 160
	max_timekeeping_hours = 3

	def __init__(self, name = None, year =None, creator = None):
		self.name = name
		self.year = year
		self.director = creator

	def show_info(self):
		print(self.name, self.year, self.director)	


#var = Movie()
#print(var.show_info())



class Movie:
	max_timekeeping_min = 160
	max_timekeeping_hours = 3
	__min_timekeeping_hours = 1.2

	def __init__(self, name = None, year =None, creator = None):
		self.name = name
		self.year = year
		self.director = creator
		self.creators = {'director': self.director, 'screenwriter': 'Nobody', 'budget': 200000}

	def show_info(self):
		print(self.name, self.year, self.director)	


#var = Movie()
#print(var.show_info())
#print(var.__min_timekeeping_hours)



class Movie:
	max_timekeeping_min = 160
	max_timekeeping_hours = 3
	__min_timekeeping_hours = 1.2

	def __init__(self, name = None, year =None, creator = None):
		self.name = name
		self.year = year
		self.director = creator
		self.creators = {'director': self.director, 'screenwriter': 'Nobody', 'budget': 200000}


	def show_info(self):
		print(self.name, self.year, self.director)	


	def write_script(self):
		print('i write script for movie')	

	def write_text(self, text):
		if type(text) is str:
			print(text)
		else:
			print('type is not a string')



#print(Movie().write_script())
#print(Movie().write_text('some text'))
#print(Movie().write_text(('some text',)))

class Movie_:
	pass

new_movie = Movie_()
new_movie.name = 'Six String Samurai'
new_movie.status = 'Classic'
new_movie.time_minutes = 120
new_movie.tagline = lambda tagline:print(tagline)

#print(new_movie.tagline('some tagline'))



class VideoGame(Movie):
	pass

print(VideoGame.max_timekeeping_min)


class VideoGame(Movie):
	max_timekeeping_min = None
	max_timekeeping_hours = None
	pass


#print(VideoGame().max_timekeeping_min)


class VideoGame(Movie):
	max_timekeeping_min = None
	max_timekeeping_hours = None

	def write_script(self):
		print('i write script for videogame')		
		pass


#print(VideoGame().write_script())
#print(VideoGame().show_info())


#print(VideoGame.__dict__)
#print(VideoGame.__module__)
#print(VideoGame.__name__)

#print(VideoGame.__str__)