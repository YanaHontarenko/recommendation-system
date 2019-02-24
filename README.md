Recommendation system. Collaborative filtering.
===============================================
A **recommendation system** is a subclass of information filtering system that seeks to predict the "rating" or "preference" a user would give to an item.

In the center of any advisory system there is a **matrix preferences**. This matrix is one of the axes of which all customers are located, and on other objects recommendations (films, sites, items). At the intersection of some pairs (user, item), this matrix is filled with estimates (ratings) is a well-known index of user interest in this items, expressed on a given scale(for example, from 1 to 5).

![Image of userItemMatrix](https://www.researchgate.net/profile/Khadija_Almohsen/publication/284737564/figure/fig1/AS:391543350415362@1470362617700/Sample-of-user-item-matrix.png)

**Collaborative filtering** is a method of making automatic predictions (filtering) about the interests of a user by collecting preferences or taste information from many users (collaborating).

**Used method:**
- user-based;
- item-based;

**User-based** method checking similarity of two people by metrics. 

**Item-based** method checking similarity of two films by metrics. 

One of the problems of this type of advisory systems is non-standard users. It is possible that the person has not seen in his life a movie that would have liked her so that she could put him 5, and he usually raises ratings of 3, a maximum of 4. Or, on the contrary, a person is so emotional, that any movie captures her and she puts it all 5. To solve this problem, by quantifying the amount of user ratings for a particular movie we averaging it. For example, for user-based model after summing up all ratings for the current movie, their amount is divided by the amount similarities of the current user with all the users who rated this current movie.

**Used metrics:**
- euclidean distance;
- pearson correlation coefficient;
- cosine similarity;
- manhattan metric;
- chebyshev distance;
- aseembly of used metrics (similarity equals the similarity for each of the above metrics multiplied by the corresponding coefficients).

Computer experiments
====================
To checking how to behave the model **user-based** was created a person with certain tastes (replaced by an already existing person). *These are 15-30 lines in the file.* She was offered a person who rated only comedy films. The model returns 10 films. If the film had a genre comedy, it was counted as correct. The results are shown below. *(1 film = 10%):*
- euclidean distance 30%;
- pearson correlation coefficient 30%;
- cosine similarity 100%;
- manhattan metric 40%;
- chebyshev distance 80%;

For checking item-based method was chosen film which have 4 genres: comedy, animation, adventure, fantasy. If film which model recommendd have one of this genre, it was counted as correct. Results:
- euclidean distance 20%;
- pearson correlation coefficient 50%;
- cosine similarity 60%;
- manhattan metric 20%;
- chebyshev distance 70%.
