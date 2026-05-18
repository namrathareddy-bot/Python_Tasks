import numpy as np
ratings = np.array([2,3,4,5,1])
print(ratings)
normalized_rating = (ratings - np.min(ratings))/(np.max(ratings) - np.min(ratings))
print(np.round(normalized_rating, 2))
