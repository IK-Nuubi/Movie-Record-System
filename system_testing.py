from bi28hf_system_source_code import Movies, MovieList, Actors, ActorsList

jamesbond007 = Movies("Casino Royale", 2006, "Action/Adventure", "16/11/2006")

actions = MovieList()

actions.add_movie(jamesbond007)

jamesbond = Actors("Daniel", "Craig", "Male", "02/03/1968")

all_actors = ActorsList()

all_actors.add_actor(jamesbond)

print(jamesbond007)

print(all_actors.no_of_actors())

print(jamesbond)

all_actors.remove_actor("Daniel")

print(all_actors.no_of_actors())
