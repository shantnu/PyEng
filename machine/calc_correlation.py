import sys
import pdb
import numpy as np
import ast
import json

def find_correlation(movie_list, movie_for_correlation):
    '''
    Input:
    movie_list - List of movies
    movie_for_correlation: The movie to calculate the correlation for

    Return:
    Dictionary of correlation for movie_for_correlation
    '''
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

if len(sys.argv) < 2:
    print("Usage: python calc_correlation.py <data file.py>")
    exit(1)

with open(sys.argv[1], 'r') as f:
    temp = f.read()
    movies_list = ast.literal_eval(temp)
    print(movies_list)

correlated_dict = {}
for movie in movies_list:
    correlated_dict[movie] =  find_correlation(movies_list, movie)

print(correlated_dict)

json.dump(correlated_dict, open("corr_dict.py",'w'))
