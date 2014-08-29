# Be sure to change var names

import pandas as pd
import matplotlib.pyplot as plt

u_cols = ['user_id', 'age', 'sex']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols, usecols=range(3))

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols,  usecols=range(3))

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = ['movie_id', 'title']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(2))

# create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
lens = pd.merge(movie_ratings, users)


# Top rated movies
lens.groupby('title').size().order(ascending=False)[:10]

#Users distribtion
users.age.hist(bins=30)
plt.title("Distribution of users' ages")
plt.ylabel('count of users')
plt.xlabel('age');


plt.show()

# Find top rated movies

movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})


mean_ratings=lens.pivot_table('rating', rows='title',cols='sex')
ratings_by_title = data.groupby('title').size()
mean_ratings = mean_ratings.ix[active_titles]
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
disagreements = mean_ratings['diff']

disagreements.order().plot(kind='barh', figsize=[9, 15])
plt.title('Male vs. Female Avg. Ratings\n(Difference > 0 = Favored by Men)')
plt.ylabel('Title')
plt.xlabel('Average Rating Difference');
plt.show()
