'''
Get recommendations for a given person user-based method or item-based method.
Using the weighted average of ratings given by all other users.
'''
from similarity_measure import *
from top_matches import *


def user_based(data, this, similarity=euclidean_distance):
    # Making lists of users.
    current_list = range(1, data.shape[0])
    # Checking which film this user don`t appreciated.
    iterable_list = np.where(data[this] == 0)[0][2:]
    totals = {}
    simSums = {}
    # For other users.
    for other in current_list:
        # Miss current user.
        if other == this:
            continue
        # Check similarity of this person and other.
        sim = similarity(data, this, other, axis=0)
        if sim == 0:
            continue
        # Checking which film other user appreciated.
        other_iterable_list = np.where(data[other] != 0)[0]
        '''
        For each film which other user appreciated and this user don`t appreciated,
        multiply users similarity and mark which other user give this film and write this in totals.
        Also save similarity by this users.
        '''
        for item in other_iterable_list:
            if item in iterable_list:
                totals.setdefault(item, 0)
                totals[item] += data[other, item] * sim
                simSums.setdefault(item, 0)
                simSums[item] += sim
    # Build find rating of films for this user.
    rankings = np.array([[total / simSums[item], item] for item, total in totals.items()])
    rankings = rankings[rankings[:, 0].argsort()]
    rankings = rankings[::-1]
    return rankings


def item_based(data, this, similarity=euclidean_distance):
    # Checking which user appreciated this film.
    iterable_list = np.where(data[:, this] != 0)[0]
    totals = {}
    simSums = {}
    # For users which apreciated this film.
    for other in iterable_list:
        # Checking what film it rated.
        other_iterable_list = np.where(data[other] != 0)[0]
        # For all this movie.
        for item in other_iterable_list:
            # If it is current mivie - miss it.
            if item == this:
                continue
            # Check similarity of this movie and other.
            sim = similarity(data, this, item, axis=1)
            if sim == 0:
                continue
            '''
            For each movie rated by the user who rated this movie
            multiply film similarity and mark which user give this film and write this in totals.
            Also save similarity by this movies.
            '''
            totals.setdefault(item, 0)
            totals[item] += data[other, item] * sim
            simSums.setdefault(item, 0)
            simSums[item] += sim
    rankings = np.array([[total / simSums[item], item] for item, total in totals.items()])
    rankings = rankings[rankings[:, 0].argsort()]
    rankings = rankings[::-1]
    return rankings


def recommendations(data, this, axis=0, similarity=euclidean_distance):
    if axis == 0:
        recommendation = user_based(data, this, similarity=similarity)
    else:
        recommendation = item_based(data, this, similarity=similarity)
    # Return top-10 films.
    return list(map(int, recommendation[:, 1]))[:10]
