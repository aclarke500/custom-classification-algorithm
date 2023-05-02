import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from TrainDataObject import Datum, ColumnDistributions
import temp

data = pd.read_csv('iris.csv')
rows, cols = data.shape
testing_indices = temp.generate_random_numbers(rows/5, 0, rows-1)

def create_predicted_distribution(column_name, data, testing_indices):
    # converts data frames to lists
    [setosa_training, setosa_testing] = temp.get_data_as_lists(
        'Iris-setosa', column_name, testing_indices, data)
    [virginica_training, virginica_testing] = temp.get_data_as_lists(
        'Iris-virginica', column_name, testing_indices, data)
    [versicolor_training, versicolor_testing] = temp.get_data_as_lists(
        'Iris-versicolor', column_name, testing_indices, data)

    setosa_train_df = temp.make_data_frame(setosa_training, 'setosa length')
    virginica_train_df = temp.make_data_frame(
        virginica_training, 'virginica length')
    versicolor_train_df = temp.make_data_frame(
        versicolor_training, 'versicolor length')

    set_bell = temp.get_bell_curve(setosa_training)
    vir_bell = temp.get_bell_curve(virginica_training)
    ver_bell = temp.get_bell_curve(versicolor_training)

    return(ColumnDistributions(set_bell, vir_bell, ver_bell, setosa_train_df, virginica_train_df, versicolor_train_df))


def test(data_row, distributions):
    setosa_p_values = []
    virginica_p_values = []
    versicolor_p_values = []

    current_column = 0
    for column in distributions:
        virginica_t_statistic, virginica_p_value = stats.ttest_1samp(a=column.virginica_df, popmean=data_row[current_column])
        virginica_p_values.append(virginica_p_value)
        setosa_t_statistic, setosa_p_value = stats.ttest_1samp(a=column.setosa_df, popmean=data_row[current_column])
        setosa_p_values.append(setosa_p_value)
        versicolor_t_statistic, versicolor_p_value = stats.ttest_1samp(a=column.versicolor_df, popmean=data_row[current_column])
        versicolor_p_values.append(versicolor_p_value)

        current_column+=1
    
    setosa_total = temp.dot_product(setosa_p_values)[0] # is returning an array for some reason
    virginica_total = temp.dot_product(virginica_p_values)[0]
    versicolor_total = temp.dot_product(versicolor_p_values)[0]

    results = [setosa_total, virginica_total, versicolor_total]
    group = data_row[len(data_row)-1] # get the classification

    if group == 'Iris-setosa':
        return max(results) == setosa_total
    elif group == 'Iris-versicolor':
        return max(results) == versicolor_total
    elif group == 'Iris-virginica':
        return max(results) == virginica_total 

    return

columns = ["5.1", "3.5", "1.4", "0.2"]
distributions = []
for c in columns:
    distributions.append(create_predicted_distribution(c, data, testing_indices))

training_data = [data.iloc[i].tolist() for i in testing_indices]
total=len(training_data)
success = 0
for t in training_data:
    if test(t, distributions):
        success+=1

print(success/total)