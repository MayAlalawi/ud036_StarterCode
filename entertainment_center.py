import media  # import media to use the class
import fresh_tomatoes  # import fresh_tomato to display movie on webpage


# create six defferent objects of Class Movie to be displayed on the webpage
# toy story
toy_story = media.Movie("Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/" +
                        "13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc&t=6s")
# baby Boss
baby_boss = media.Movie("Baby_Boss",
                        "http://deavilavideo.com.br/loja2/wp-content/uploads" +
                        "/2017/06/O-PODEROSO-CHEFINHO.jpg",
                        "https://www.youtube.com/watch?v=O2Bsw3lrhvs")
# Frozen
frozen = media.Movie("Frozen",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcTIaSaZM-" +
                     "kGnMKWNNMW9-_v008JrEh58Ab3DAV1geUNJvXeyXS",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")
# Tangled
tangled = media.Movie("Tangled",
                      "http://i.ebayimg.com/00/s/NDk5WDM1OA==/z/0UgAAOx" +
                      "yVLNS-sa5/$_3.JPG?set_id=2",
                      "https://www.youtube.com/watch?v=JYKpIr1lSG0")
# Inside out
inside_Out = media.Movie("Inside Out",
                         "https://images-na.ssl-images-amazon.com/images/" +
                         "I/51g%2B1-GJCuL.jpg",
                         "https://www.youtube.com/watch?v=_MC3XuMvsDI")
# Ratatouille
ratatouille = media.Movie("Ratatouille",
                          "http://www.pixartalk.com/wp-content/uploads/2009/" +
                          "06/ratus1.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
# create list of movies
movies = [toy_story, baby_boss, frozen, tangled, inside_Out, ratatouille]

# call open_movies_page methode to display the movies list
fresh_tomatoes.open_movies_page(movies)
