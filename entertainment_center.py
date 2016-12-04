# -*- coding: utf-8 -*-

# little script to display favorite movies in a web browser

import media
import fresh_tomatoes

# Create three movie objects with favorite movies
godfather = media.Movie("The Godfather", 
	"The story, spanning 1945 to 1955, chronicles the family under the patriarch Vito Corleone, focusing on the transformation of Michael Corleone (Pacino) from reluctant family outsider to ruthless Mafia boss.", 
	"https://upload.wikimedia.org/wikipedia/en/thumb/1/1c/Godfather_ver1.jpg/220px-Godfather_ver1.jpg",
	"https://en.wikipedia.org/wiki/The_Godfather", 
	"https://www.youtube.com/watch?v=YYKxj8qiLTg")
das_boot = media.Movie("Das Boot", 
	"An adaptation of Lothar-Günther Buchheim's 1973 German novel of the same name, the film is set during World War II and tells the fictional story of U-96 and its crew.", 
	"https://upload.wikimedia.org/wikipedia/en/thumb/a/a3/Das_boot_ver1.jpg/220px-Das_boot_ver1.jpg",
	"https://en.wikipedia.org/wiki/Das_Boot", 
	"https://www.youtube.com/watch?v=7pzKyeIex2Y")
life_is_beautiful = media.Movie("Life is Beautiful", 
	"Film about a Jewish Italian book shop owner, who employs his fertile imagination to shield his son from the horrors of internment in a Nazi concentration camp.", 
	"https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Vitaebella.jpg/220px-Vitaebella.jpg",
	"https://en.wikipedia.org/wiki/Life_Is_Beautiful", 
	"https://www.youtube.com/watch?v=pysuUJhOnv4")

# create a list with the favorite movies
movies = [godfather, das_boot, life_is_beautiful]

# call fresh_tomatoes to display it in a web browser
fresh_tomatoes.open_movies_page(movies)