import numpy as np


def sample_range(low, high, round_to = 1):
    """
    Sample realistic values
    
    :param low: lower bound of range
    :param high: upper_bound of range
    :param round_to: decimals rouding number

    returns:
        values in given range, rounded to given decimals 
    """

    value = np.random.uniform(low, high)

    return round(value, round_to)