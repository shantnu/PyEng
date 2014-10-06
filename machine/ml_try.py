import scipy.stats 
import numpy as np
import pdb

movies_list = {'Terminator': {'Tom': 4.0,
  'Jack': 1.5,
  'Lisa': 3.0,
  'Sally': 2.0},
  
 'Terminator 2': {'Tom': 5.0,
  'Jack' : 1.0,
  'Lisa': 3.5,
  'Sally': 2.0},
  
 'It happened one night': {'Tom': 3.5,
  'Jack': 3.5,
  'Tiger': 4.0,
  'Lisa': 5.0,
  'Michele': 3.0,
  'Sally': 4.0,},
  
 '27 Dresses': {'Tom': 3.0,
  'Jack': 3.5,
  'Tiger': 3.0,
  'Lisa': 5.0,
  'Michele': 4.0,
  'Sally': 4.0},

  'Poirot': {'Tom': 4.0,
  'Jack': 3.0,
  'Tiger': 5.0,
  'Lisa': 4.0,
  'Michele': 3.5,
  'Sally': 3.0,
  },

 'Sherlock Holmes': {'Tom': 4.0,
  'Jack': 3.0,
  'Tiger': 3.5,
  'Lisa': 3.5,
  'Sally': 2.0,
  }}
  
  
#movie_for_correlation = 'The Night Listener'
#key_b = 'Snakes on a Plane'

def find_correlation(movie_list, movie_for_correlation):
    correlate_dict = {}
    for movie in movie_list:
        # Don't include current movie in correlation, as you can't compare a movie to itself!
        if movie != movie_for_correlation:

            movie_for_correlation_list = []
            movie_to_compare_list = []
            
            # Loop through the people who reviewed the movie
            for reviewer_name in movie_list[movie_for_correlation]:
                
                # Check that the reviewer has reviewed the current movie.
                # If so, calculate the correlation coefficient.
                # If they haven't reviewed the movie, then it makes no sense doing a correlation.
                
                if reviewer_name in movie_list[movie]:
                    movie_for_correlation_list.append(movie_list[movie_for_correlation][reviewer_name])
                    movie_to_compare_list.append(movie_list[movie][reviewer_name])

            correlate_dict[movie] = np.corrcoef(movie_for_correlation_list,movie_to_compare_list)[1][0]

    return correlate_dict


# @TODO: In second variation, store these in file, so they can be updated daily.    
correlated_dict = {}
for movie in movies_list:
    correlated_dict[movie] =  find_correlation(movies_list, movie)
        

#print correlated_dict

my_movies = {'Terminator': 5.0,
      'Sherlock Holmes' : 4.0,
      'Poirot' : 4.5
      }


# A dictionary to store the total of my calculated votes      
total_my_votes = {}

# A running total  to store intermediate results.
running_total = 0 

# Loop over rated movies
for movie_key in my_movies.keys():
   
   # Is the movie I rated in the correlated dictionary? If so, loop over it.
    if movie_key in correlated_dict.keys():
        
        # Loop over the dictionary of correlation coefficients
        for corr_coefs in correlated_dict[movie_key]:
            running_total = 0 
            
            # If it is not a movie I have rated, we can calculate the correlation
            if corr_coefs not in my_movies.keys():
            
                # If this is the first time we are running the code, we won't have anything stored.
                # In that case, create a new dictionary element.
                if corr_coefs not in total_my_votes:
                    # Line below creates a new dictionary element for total_my_votes and gives it a value.
                    total_my_votes.setdefault(corr_coefs, (correlated_dict[movie_key][corr_coefs] * my_movies[movie_key]) )
                    
                else:
                    # If this is not the first time, merely update the values we have created before
                    total_my_votes[corr_coefs] += correlated_dict[movie_key][corr_coefs] * my_movies[movie_key]

                    

print "total_my_votes = ", total_my_votes


recommended_movies = {}
for movie_key in total_my_votes.keys():
    if movie_key in total_my_votes:
        recommended_movies.setdefault(movie_key, total_my_votes[movie_key]/len(total_my_votes.keys()))
        
print recommended_movies
      
'''
[a[key_b][ll] for ll in a[movie_for_correlation] if ll in a[key_b]]
Out[44]: [4.0, 4.0, 3.5, 3.5, 3.5, 3.0]

[[ll] for ll in a[movie_for_correlation] if ll in a[key_b]]
Out[45]: 
[['Tiger'],
 ['Sally'],
 ['Tom'],
 ['Lisa'],
 ['Jack'],
 ['Michele']]

[ll for ll in a[movie_for_correlation] if ll in a[key_b]].sort()

[ll for ll in a[movie_for_correlation] if ll in a[key_b]]

correlated_dict={'27 Dresses': {'Poirot': -0.30434782608695654, 'Terminator 2': -0.12547286652195427, 'It happened one night': 0.5791405068790082, 'Sherlock Holmes': -0.27583864218368526, 'Terminator': -0.15404159684748153}, 'It happened one night': {'Terminator 2': 0.13468700594029476, '27 Dresses': 0.5791405068790082, 'Terminator': 0.10629880069054677, 'Sherlock Holmes': 0.0, 'Poirot': 0.2895702534395041}, 'Terminator 2': {'Poirot': 0.90726470872655474, '27 Dresses': -0.12547286652195427, 'It happened one night': 0.13468700594029476, 'Sherlock Holmes': 0.73889576951817515, 'Terminator': 0.99861543720375834}, 'Terminator': {'Terminator 2': 0.99861543720375834, '27 Dresses': -0.15404159684748153, 'It happened one night': 0.10629880069054677, 'Sherlock Holmes': 0.77020798423740755, 'Poirot': 0.91132237686576711}, 'Poirot': {'Terminator 2': 0.90726470872655474, '27 Dresses': -0.30434782608695654, 'It happened one night': 0.2895702534395041, 'Sherlock Holmes': 0.66989384530323559, 'Terminator': 0.91132237686576711}, 'Sherlock Holmes': {'Poirot': 0.6698938453032357, 'Terminator 2': 0.73889576951817515, '27 Dresses': -0.27583864218368526, 'It happened one night': 0.0, 'Terminator': 0.77020798423740755}}


for movie_key in my_movies.keys():
 if movie_key in correlated_dict.keys():
     #print my_movies[movie_key], correlated_dict[movie_key]
     for corr_coefs in correlated_dict.keys():
         print movie_key, corr_coefs
         #print correlated_dict[movie_key][corr_coefs]
         
         

'''