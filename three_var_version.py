import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import temp # helper library

data = pd.read_csv('iris.csv')
[setosa_training, setosa_testing] = temp.get_data_as_lists('Iris-setosa','5.1',data)
[virginica_training, virginica_testing] = temp.get_data_as_lists('Iris-virginica','5.1',data)
[versicolor_training, versicolor_testing] = temp.get_data_as_lists('Iris-versicolor','5.1',data)

setosa_train_df = temp.make_data_frame(setosa_training, 'setosa length')
virginica_train_df = temp.make_data_frame(virginica_training, 'virginica length')
versicolor_train_df = temp.make_data_frame(versicolor_training, 'versicolor length')

set_bell = temp.get_bell_curve(setosa_training)
vir_bell = temp.get_bell_curve(virginica_training)
ver_bell = temp.get_bell_curve(versicolor_training)

for bell in [set_bell, vir_bell, ver_bell]:
    plt.plot(bell[0], bell[1]) # x_values and y_values inside the list

y_value_for_training_scatter_plots = 1
for train in [setosa_training, virginica_training, versicolor_training]:
    plt.scatter(train, [y_value_for_training_scatter_plots for i in range(len(train))])
    y_value_for_training_scatter_plots+=1

plt.title("Distribution of testing and training data")


def test(elem):
    virginica_t_statistic, virginica_p_value = stats.ttest_1samp(a=virginica_train_df, popmean=elem[0])
    setosa_t_statistic, setosa_p_value = stats.ttest_1samp(a=setosa_train_df, popmean=elem[0])
    versicolor_t_statistic, versicolor_p_value = stats.ttest_1samp(a=versicolor_train_df, popmean=elem[0])

    if elem[1] == 'setosa': 
        success = setosa_p_value > virginica_p_value and setosa_p_value > versicolor_p_value
    elif elem[1] == 'virginica':
        success = virginica_p_value > setosa_p_value and virginica_p_value > versicolor_p_value
    elif elem[1] == 'versicolor':
        success = versicolor_p_value > setosa_p_value and versicolor_p_value > virginica_p_value

    return success

complete_test = []
for v in [[setosa_testing, 'setosa'], [virginica_testing, 'virginica'], [versicolor_testing, 'versicolor']]:
    for element in v[0]:
        complete_test.append([element, v[1]])

correct = 0
for t in complete_test:
    if test(t):
        correct+=1

print(f"Scored {correct} out of {len(complete_test)}")
print(f"Accuracy = {correct/len(complete_test)}%")

plt.show()