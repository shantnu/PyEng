import pdb
import json


# My ratings for movies.
my_movies = {'Terminator': 5.0,
      'Sherlock Holmes' : 4.0,
      'Poirot' : 4.5
      }


# Read the data from the correlation dictionary we calculated earlier      
correlated_dict = json.load(open("corr_dict.py"))

# A dictionary to store the total of my calculated votes      
total_my_votes = {}

# A running total  to store intermediate results.
running_total = 0 

# Loop over rated movies
for movie_key in my_movies.keys():
        
        # Loop over the dictionary of correlation coefficients
        for movie_to_compare in correlated_dict[movie_key]:
            running_total = 0 
            
            # If it is not a movie I have rated, we can calculate the correlation
            if movie_to_compare not in my_movies.keys():
            
                # If this is the first time we are running the code, we won't have anything stored.
                # In that case, create a new dictionary element.
                if movie_to_compare not in total_my_votes:
                    # Line below creates a new dictionary element for total_my_votes and gives it a value.
                    total_my_votes.setdefault(movie_to_compare, (correlated_dict[movie_key][movie_to_compare] * my_movies[movie_key]) )
                    
                else:
                    # If this is not the first time, merely update the values we have created before
                    total_my_votes[movie_to_compare] += correlated_dict[movie_key][movie_to_compare] * my_movies[movie_key]       

print "total_my_votes = ", total_my_votes

recommended_movies = {}
for movie_key in total_my_votes.keys():
    recommended_movies[movie_key] =  total_my_votes[movie_key] / len(total_my_votes.keys())
        
print recommended_movies

for movie_key in recommended_movies:
    if recommended_movies[movie_key] > 3.0:
        print "Strongly recommended for you: ", movie_key
    elif recommended_movies[movie_key] > 0.0:
        print "Recommended for you: ", movie_key    
    else :
        print "Not recommended: ", movie_key
