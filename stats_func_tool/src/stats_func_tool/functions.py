"""
Module for statistics functions.

"""

from math import floor
import matplotlib.pyplot as plt
from collections import Counter


def mean(data):
    """
    Finding mean value of dataset.

    :param data: list of data.
    :return: Mean value of the data
    """
    return sum(data) / len(data)


def median(data):
    """
    Finding median value of dataset.

    :param data: list of data.
    :return: Median value of data.
    """
    length = len(data)
    sorted_data = sorted(data)
    middle = length // 2
    if length % 2 == 1:
        return sorted_data[middle]
    else:
        return mean(sorted_data[middle - 1: middle + 1])


def mode(data):
    """
    Finding mode value of dataset.

    :param data: list of data.
    :return: Mode value of data
    """
    counts = Counter(data)
    max_value = max(counts.values())
    return [k for k, count in counts.items() if count == max_value]


def quantile(data, probability):
    """
    Return values at the given quantile.

    :param data: list of data.
    :param probability: probability
    :return: list of values at the given quantile.
    """
    quantile_idx = int(probability * len(data))
    return sorted(data)[quantile_idx]


def variance(data):
    """
    Finding variance of data.

    :param data: list of data.
    :return: variance of given data.
    """
    mean_value = mean(data)
    return sum([(i - mean_value) ** 2 for i in data]) / (len(data) - 1)


def std(data):
    """
    Finding standard deviation.

    :param data: list of data.
    :return: value of standard deviation.
    """
    return variance(data) ** 0.5


def data_range(data):
    """
    Finding range of data values.

    :param data: list of data.
    :return: range of values.
    """
    return max(data) - min(data)


def dot(x, y):
    """
    Multiply two data lists.

    :param x:  list of data.
    :param y:  list of data.
    :return:  list of multiplied data.
    """
    return sum([i * j for i, j in zip(x, y)])


def covariance(x, y):
    """

    :param x:  list of data.
    :param y:  list of data.
    :return: value of the covariance.
    """
    m_x = mean(x)
    m_y = mean(y)
    dev_x = [i - m_x for i in x]
    dev_y = [i - m_y for i in y]
    return dot(dev_x, dev_y) / (len(x) - 1)


def correlation(x, y):
    """


    :param x:  list of data.
    :param y:  list of data.
    :return: correlation value.
    """
    std_x = std(x)
    std_y = std(y)
    if std_x > 0 and std_y > 0:
        return covariance(std_x, std_y) / std_x / std_y
    else:
        return 0


def make_buckets(x, bucket_size):
    """

    :param x:  list of data.
    :param bucket_size: size of a bucket.
    :return: data, separated into buckets of given size.
    """
    return Counter([bucket_size * floor(i / bucket_size) for i in x])


def hist(data, bucket_size, title="", xlabel="", ylabel=""):
    """
    Plots histogram of the given data.

    param data: given data to plot.
    :param bucket_size: size of a bucket.
    :param xlabel: name of x axis.
    :param ylabel: name of y axis
    :param title: title of the plot.

    :return: None. It only shows plot.
    """
    hist_data = make_buckets(data, bucket_size)
    plt.bar(hist_data.keys(), hist_data.values(), width=bucket_size)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def plot_data(data, title="", xlabel="", ylabel=""):
    """
    Plots data.

    :param data: given data to plot.
    :param xlabel: name of x axis.
    :param ylabel: name of y axis
    :param title: title of the plot.
    :return: None. It only shows plot.
    """
    plt.plot(data)
    plt.xlabel = xlabel
    plt.ylabel = ylabel
    plt.title(title)

    plt.show()


def box_plot(data):
    """
    Plots data in boxplot form.

    :param data: given data to plot.
    :return: None. It only shows plot.
    """
    plt.boxplot(data)


list_1 = [1, 2, 1, 5, 1]
list_2 = [5, 4, 3, 2, 1]
print(std(list_1))
print(std(list_2))
