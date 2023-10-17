import media

import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        " A story of a boy and his toy",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://youtu.be/wmiIUN-7qhE")

print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an aline plant",
                     "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/wuRK_-caLB0?t=7")

batman = media.Movie("Batman the Dark Knight", "a great experience for comic fans",
                       "http://geekretreatimages.s3.amazonaws.com/wp-content/uploads/2016/03/The-Dark-Knight.jpg"
                       , "https://www.youtube.com/watch?v=EXeTwQWrcwY")
equilibrium = media.Movie("Equilibrium", "a great action movie, with a deep message",
                        "http://www.gstatic.com/tv/thumb/movieposters/30590/p30590_p_v8_aa.jpg"
                        , "https://www.youtube.com/watch?v=raleKODYeg0")

movies = [toy_story,avatar,batman.equilibrium]

fresh_tomotoes.open_movies_page(movies)

#print(avatar.storyline)
#avatar.show_trailer()
