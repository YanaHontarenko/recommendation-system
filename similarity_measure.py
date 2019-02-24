# File in which realizated few similarity measure.
import numpy as np


def find_common(data, this, other, axis=0):
    if axis == 0:
        result = [value for value in np.where(data[this] != 0)[0] if value in np.where(data[other] != 0)[0]]
        common = np.array([*zip(data[this, result], data[other, result])])
    else:
        result = [value for value in np.where(data[:, this] != 0)[0] if value in np.where(data[:, other] != 0)[0]]
        common = np.array([*zip(data[result, this], data[result, other])])
    return common


def euclidean_distance(data, this, other, axis=0):
    # Euclidean distance.
    common = find_common(data, this, other, axis)
    if len(common) == 0:
        return 0
    sum_of_squares = sum([(item[1] - item[0])**2 for item in common])
    return 1 / (1 + np.sqrt(sum_of_squares))


def pearson_correlation(data, this, other, axis=0):
    # Pearson correlation.
    common = find_common(data, this, other, axis)
    if len(common) == 0:
        return 0
    sum_one = sum([item[0] for item in common])
    sum_two = sum([item[1] for item in common])
    sum_one_square = sum([item[0]**2 for item in common])
    sum_two_square = sum([item[1]**2 for item in common])
    sum_production = sum([item[0] * item[1] for item in common])
    numerator = sum_production - (sum_one * sum_two / common.shape[0])
    denominator = np.sqrt((sum_one_square - sum_one**2 / common.shape[0]) * (sum_two_square - sum_two**2 / common.shape[0]))
    if denominator == 0:
        return 0
    return numerator / denominator


def cosine_similarity(data, this, other, axis=0):
    # Cosine similarity.
    common = find_common(data, this, other, axis)
    if len(common) == 0:
        return 0
    numerator = sum([item[0] * item[1] for item in common])
    denominator = np.sqrt(sum([item[0] * item[0] for item in common])) * np.sqrt(sum([item[1] * item[1] for item in common]))
    return numerator / denominator


def manhattan_similarity(data, this, other, axis=0):
    # Manhattan similarity.
    common = find_common(data, this, other, axis)
    if len(common) == 0:
        return 0
    result = sum([abs(item[0] - item[1]) for item in common])
    return 1 / (1 + result)


def сhebyshev_similarity(data, this, other, axis=0):
    # Chebyshev similarity.
    common = find_common(data, this, other, axis)
    if len(common) == 0:
        return 0
    result = max([abs(item[0] - item[1]) for item in common])
    return 1 - (result / 5)


def assembly_metrics(data, this, other, axis=0):
    '''
    This assembly of five metrics:
    Euclidean distance,
    Pearson correlation,
    cosine similarity,
    manhattan similarit1y,
    Chebyshev similarity.
    '''
    if axis == 0:
        koef = [0.3, 0.3, 1, 0.4, 0.8]
    else:
        koef = [0.2, 0.5, 0.6, 0.2, 0.7]
    result = [euclidean_distance(data, this, other, axis) * koef[0],
              pearson_correlation(data, this, other, axis) * koef[1],
              cosine_similarity(data, this, other, axis) * koef[2],
              manhattan_similarity(data, this, other, axis) * koef[3],
              сhebyshev_similarity(data, this, other, axis) * koef[4],
              ]
    if all(item == 0 for item in result):
        return 0
    return sum(result) / len(result)
