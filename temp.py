import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

# generate a random array of 1000 numbers

def plot_stuff(numbers):
    size=len(numbers)

    # calculate the mean and standard deviation of the array
    mean = np.mean(numbers)
    std_dev = np.std(numbers)

    # create an array of x-values
    x_values = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, size)

    # calculate the corresponding y-values for the bell curve
    y_values = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(-(x_values - mean)**2 / (2 * std_dev**2))

    # create a new figure
    fig = plt.figure()

    # add a subplot to the figure
    ax = fig.add_subplot(1, 1, 1)

    # plot the bell curve
    ax.plot(x_values, y_values, color='blue')

    # set the title and labels for the axes
    ax.set_title('Bell Curve Distribution')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # show the plot
    plt.show()

def generate_random_numbers(n, x, y):
    """
    Generate n random unique numbers between x and y.

    Parameters:
    n (int): The number of random unique numbers to generate.
    x (int): The minimum value of the range (inclusive).
    y (int): The maximum value of the range (inclusive).

    Returns:
    list: A list of n random unique numbers between x and y.
    """

    if n > (y - x + 1):
        raise ValueError("The range between x and y is too small to generate n unique numbers.")

    numbers = set()
    while len(numbers) < n:
        numbers.add(random.randint(x, y))

    return list(numbers)


def get_data_as_lists(classification, col_string, testing_indices,data):
    """
    Parameters:
    classification (string): the class of the data frame
    col_string (string): the first element of the intended column as a string
    data: pointer to pandas data frame

    Returns:
    list: [testing_data, training_data]
    """
    subset = data[data['Iris-setosa']==classification] # get all pieces with the correct classification
    col_as_list = subset[col_string].values.tolist() # convert the specified column to list
    # testing_indices=generate_random_numbers(int(len(col_as_list)/5),0,len(col_as_list))
    testing_data =[]
    training_data =[]
    for i in range(len(col_as_list)):
        if i in testing_indices:
            testing_data.append(col_as_list[i])
        else:
            training_data.append(col_as_list[i])
    return [training_data, testing_data]


# def get_data_as_lists(classification, col_string, data): BACKUP
#     """
#     Parameters:
#     classification (string): the class of the data frame
#     col_string (string): the first element of the intended column as a string
#     data: pointer to pandas data frame

#     Returns:
#     list: [testing_data, training_data]
#     """
#     subset = data[data['Iris-setosa']==classification] # get all pieces with the correct classification
#     col_as_list = subset[col_string].values.tolist() # convert the specified column to list
#     testing_indices=generate_random_numbers(int(len(col_as_list)/5),0,len(col_as_list))
#     testing_data =[]
#     training_data =[]
#     for i in range(len(col_as_list)):
#         if i in testing_indices:
#             testing_data.append(col_as_list[i])
#         else:
#             training_data.append(col_as_list[i])
#     return [training_data, testing_data]

def make_data_frame(train, name='name'):
    train_df = pd.DataFrame({
        name: train
    })
    return train_df


def get_bell_curve(training_data):
    mean = np.mean(training_data)
    std_dev = np.std(training_data)

    # create an array of x-values
    x_values = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, len(training_data))

    # calculate the corresponding y-values for the bell curve
    y_values = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(-(x_values - mean)**2 / (2 * std_dev**2))

    return [x_values, y_values]

def dot_product(arr):
    prod=1
    for a in arr:
        prod*=a
    return prod

