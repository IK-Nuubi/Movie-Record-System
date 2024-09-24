import random #importing the random module
from datetime import datetime #importing the datetime module to make our release date appear in a date format 
import secrets #importing secrets to create unique random numbers


class Movies(): #creating the movies class
    def __init__(self, title, year, genre, release_date): #creating the constructor of the movies class with attributes
        self.title = title
        self.year = year
        self.genre = genre
        self.release_date = release_date
        self.id = self.__make_id()
        
    def __make_id(self):
        temp_ID = str(secrets.randbelow(1000)) #using the secrets module create a randomly generated ID for the movie
        ID = temp_ID + self.title[:2].lower() #concatenating the first two letters of the title with the randomly generated ID
        return ID
       
    def set_title(self, title): #a method to set the title of the movie
        self.title = title

    def set_year(self, year): #a method to set the year of the movie
        self.year = year

    def set_genre(self, genre): #a method to set the genre of the movie
        self.genre = genre

    def set_release_date(self, release_date): #a method to set the release_date of the movie
        try:
            self.release_date = datetime.strptime(release_date, '%d/%m/%Y').date() #this to make the date to appear in a datetime format
        except ValueError:
            print("Date entered is invalid")
        except NameError:
            print("Date entered is wrong")

    def get_id(self): #a method to get the release date of the movie
        return self.id

    def get_title(self): #a method to get the title of the movie
        return self.title

    def get_year(self): #a method to get the year of the movie
        return self.year

    def get_genre(self): #a method to get the genre of the movie
        return self.genre

    def get_release_date(self): #a method to get the release date of the movie
        return self.release_date

    def __str__(self): #a method to show the attributes of the class
        return "Movie ID: {0}, Title: {1}, Year: {2}, Genre: {3}, Release Date: {4}".format(self.id, self.title.capitalize(), 
                                                                                            self.year, self.genre.capitalize(), 
                                                                                            self.release_date)


class MovieList(): #Creating the class MovieList
    def __init__(self):
        self.movie_list = {} #Creating a dictionary to store the objects created.

    def add_movie(self, movies): #A method to add objects to the already created list 
        if isinstance(movies, Movies): #to ensure that the objects added are of the movie class
            self.movie_list[movies.get_id()] = movies #adding the movie to the dictionary using the movie's key as value
        else:
            print("Movie is not an instance of the Movies Class")

    def search_movie(self, search_key): #a method to search through the dictionary
        search_results = [] #create an empty list to store the result of the search
        for movies in self.movie_list.values(): #looping through the values of the movie_list dictionary
            if (movies.get_title().lower() == search_key.lower()) or (movies.get_genre().lower() == search_key.lower()) or (movies.get_release_date() == search_key.lower) is True:
                search_results.append(movies) #adding any matching values to the search_result list    
        if len(search_results) == 0: #If nothing is found and list is empty then:
            return "Movie not in collection" #return this statement to inform the user
        else:
            return [movies.__str__() for movies in search_results] #else print the search results.

    def remove_movie(self, title): #a method to remove a movie using the title of the movie
        remove_movie = False
        for movies in self.movie_list.values(): #looping through the values of the movie_list dictionary
            if (movies.get_title().lower() == title.lower()):
                del self.movie_list[movies.get_id()]
                remove_movie = True
                break
        if not remove_movie:
            print("Movie is not in the collection")

    def movie_counter(self): #to get the total number of movies, we calculate the number of keys in the dictionary
        movie_counter = len(self.movie_list)
        return(movie_counter, "is the total number of movies in our collection")

    def __str__(self): #a method to show the attributes of the class
        return "\n".join (str(movies) for movies in self.movie_list.values())
        

class Actors(): #creating the actors class
    def __init__(self, first_name, surname, gender, date_of_birth): #creating the constructor of the Actors class with its attributes
        self.first_name = first_name
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.id_actors = self.__make_id_actors()

    def __make_id_actors(self): #to create a randomly generated ID for the actor
        temp_ID = str(secrets.randbelow(1000))
        ID = temp_ID + self.first_name[:2].lower()
        return ID

    def set_first_name(self, first_name): #a method to set the first name of the actor
        self.first_name = first_name

    def set_surname(self, surname): #to set the surname of the actor
        self.surname = surname

    def set_gender(self, gender): #to set the gender of the actor
        self.gender = gender

    def set_date_of_birth(self, date_of_birth): #to set the date of birth of the actor
        try:
            self.date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y').date()
        except ValueError:
            print("Date entered is invalid")
        except NameError:
            print("Date entered is wrong")

    def get_id_actors(self): #a method to get the id of the actor
        return self.id_actors

    def get_first_name(self): #a method to get the first name of the actor
        return self.first_name

    def get_surname(self): #to get the surname of the actor
        return self.surname

    def get_gender(self): #to get the gender of the actor
        return self.gender

    def get_date_of_birth(self): #to get the date of birth of the actor
        return self.date_of_birth

    def __str__(self): #showing the attributes of the class
        return "First Name: {0}, Surname: {1}, Gender: {2}, Date of birth: {3}".format(self.first_name.capitalize(), self.surname.capitalize(), 
                                                                                       self.gender.capitalize(), self.date_of_birth)


class ActorsList():
    def __init__(self): #initialising the ActorsList class and adding attributes 
        self.actors_list = {} #creating a dictionary to store objects created.

    def add_actor(self, actor): #to add an actor to the actor_list dictionary
        if isinstance(actor, Actors): #to check that the actor name provided is an instance of the Actor Class
            self.actors_list[actor.get_id_actors()] = actor #adding the actor to the actor_list dictionary using the actor_ID as key 
        else:
            return "Actor is not an instance of the Actor Class"

    def remove_actor(self, first_name): #to remove an actor from the dictionary using the first name
        for actor in self.actors_list.values(): #looping through the values of the dictionary
            if (actor.get_first_name().lower() == first_name.lower()):
                del self.actors_list[actor.get_id_actors()]
                print (f"{first_name} has been successfully deleted")
                break
        else:
            return "Actor is not in the collection"

    def no_of_actors(self): #getting the total number of actors on the actor_list dictionary
        no_of_actors = len(self.actors_list)
        return no_of_actors, "is the total number of actors in our collection"

    def search_actors_list(self, first_name):
        actor_search_results = [] #create an empty list to store the result of the search
        for actor in self.actors_list.values():
            if (actor.get_first_name().lower() == first_name.lower()) is True:
                actor_search_results.append(actor)
        if len(actor_search_results) == 0:
            return "Actor not in collection"
        else:
            return [actor.__str__() for actor in actor_search_results]

    def __str__(self): #a method to show the attributes of the class
        return "\n".join (str(actor) for actor in self.actors_list.values())