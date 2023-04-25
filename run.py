import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import temp # helper library

x = [1, 2, 3]

data = pd.read_csv('iris.csv')
setosa_data = data[data['Iris-setosa']=='Iris-setosa']
length_of_sepals = setosa_data['5.1'].values.tolist()

# get testing and training data
size_of_testing_data = int(len(length_of_sepals)/5) # 20%
print(size_of_testing_data)

testing_indices = temp.generate_random_numbers(size_of_testing_data, 0, len(length_of_sepals))
training_data = []
testing_data = []

for i in range(len(length_of_sepals)):
    if not i in testing_indices:
        training_data.append(length_of_sepals[i])
    else:
        testing_data.append(length_of_sepals[i])

train_dataframe = pd.DataFrame({
    'setosa length': training_data
})

test_dataframe = pd.DataFrame({
    'setosa length': testing_data
})

avg = sum(training_data)/len(training_data)



t_statistic, p_value = stats.ttest_1samp(a=train_dataframe, popmean=testing_data[0])

print(t_statistic, p_value)

testing_y_vals = [2 for i in range(len(testing_data))]
training_y_vals = [1 for i in range(len(training_data))]

plt.scatter(testing_data, testing_y_vals)
plt.scatter(training_data, training_y_vals)
plt.show()

def test_val(test_value):
    t_statistic, p_value = stats.ttest_1samp(a=train_dataframe, popmean=test_value)
    print(f'Value at {1} = {p_value}')

for i in testing_data:
    test_val(i)