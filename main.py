from get_recommendations import *
from helpful import *
from similarity_measure import *
from top_matches import *

'''
Make matrix moviLens and vector films.
Vector films consist of [number in sequence, movie Id]
'''

movieLens = load_matrix()
# Names of the films.
films_names = [0, 0] + list(pd.read_csv('movieLens/movies.csv')['title'].values)
# Fill a row of matrices (we will make recommendations for this user).
movieLens[610, :] = np.zeros(movieLens.shape[1])
movieLens[610, 7497] = 5
movieLens[610, 7496] = 4
movieLens[610, 7455] = 4
movieLens[610, 7433] = 5
movieLens[610, 7387] = 5
movieLens[610, 7375] = 4
movieLens[610, 7358] = 5
movieLens[610, 7347] = 5
movieLens[610, 7349] = 5
movieLens[610, 7328] = 4
movieLens[610, 7301] = 5
movieLens[610, 7293] = 5
movieLens[610, 7296] = 5
movieLens[610, 7286] = 5
movieLens[610, 7272] = 5

'''
Here you select the row or column(if you create your row choose it) by which the analysis will be done.
Also choose axis(0 - user based algorithm, 1 - item based) and metrics
'''

'''
Uncomment this if you want do recommendation by user.
result = recommendations(movieLens, 610, axis=0, similarity=assembly_metrics)
'''

result = recommendations(data=movieLens, this=2, axis=1, similarity=assembly_metrics)
print(result)
print("We recommend you such films: ")
for film in result:
    print(films_names[film])
