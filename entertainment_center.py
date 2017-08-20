from media import *
import fresh_tomatoes




# Avatar movie


image =  "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg"
video = "https://www.youtube.com/watch?v=5PSNL1qE6VY"
avatar_info = MovieTrailer("Avatar", "A marine on an alien planet",  image, video)
avatar= avatar_info.get_media()


# School of rock movie
image = "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg"
video = "https://www.youtube.com/watch?v=XCwy6lW5Ixc"
School_of_rock_info = MovieTrailer("School of rock", "Using rock music to learn",  image, video)
school_of_rock = School_of_rock_info.get_media()

# Ratatouille movie
title = "Ratatouille"
description = "A rat is a chef in Paris"
image = "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg"
video = "https://www.youtube.com/watch?v=c3sBBRxDAqk"
ratatouille_info = MovieTrailer("Ratatouille", "A rat is a chef in Paris",  image, video)
ratatouille = ratatouille_info.get_media()

# Midnight in paris movie
title = "Midnight in Paris"
description = "Going back in time to meet authors"
image = "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg"
video = "https://www.youtube.com/watch?v=FAfR8omt-CY"
midnight_in_paris_info = MovieTrailer("Midnight in Paris", "Going back in time to meet authors",  image, video)
midnight_in_paris = midnight_in_paris_info.get_media()

# Hunger games movie

title = "Hunger games"
description = "A really real reality show"
image = "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg"
video = "https://www.youtube.com/watch?v=mfmrPu43DF8"
hunger_games_info = MovieTrailer("Hunger games", "A really real reality show",  image, video)
hunger_games = hunger_games_info.get_media()

# The movie list to show
movies = [avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

# Open the movies page
fresh_tomatoes.open_movies_page(movies)

'''TO DO: Commit to github'''
