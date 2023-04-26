import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import temp # helper library

x = [1, 2, 3]

data = pd.read_csv('iris.csv')
setosa_data = data[data['Iris-setosa']=='Iris-setosa']
length_of_sepals = setosa_data['5.1'].values.tolist()
virginica_data = data[data['Iris-setosa']=='Iris-virginica']
virginica_length_of_sepals = virginica_data['5.1'].values.tolist()



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



t_statistic, p_value = stats.ttest_1samp(a=train_dataframe, popmean=avg)

print(t_statistic, p_value)

testing_y_vals = [2 for i in range(len(testing_data))]
training_y_vals = [3 for i in range(len(training_data))]

plt.scatter(testing_data, testing_y_vals, color='red')
plt.scatter(training_data, training_y_vals, color='blue')
# plt.scatter(avg, 1.5, color = 'purple')



mean = np.mean(training_data)
std_dev = np.std(training_data)

# create an array of x-values
x_values = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, len(training_data))

# calculate the corresponding y-values for the bell curve
y_values = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(-(x_values - mean)**2 / (2 * std_dev**2))
plt.plot(x_values, y_values, color='purple')
# plt.show()

# def test_val(test_value):
#     t_statistic, p_value = stats.ttest_1samp(a=train_dataframe, popmean=test_value)
#     print(f'Value at {test_value} = {p_value}')

# for i in testing_data:
#     test_val(i)



# do the same thing for iris-virginica
list_of_testing_indices=temp.generate_random_numbers(int(len(virginica_length_of_sepals)/5),0,len(virginica_length_of_sepals))
virginica_testing=[]
virginica_training=[]

for i in range(len(virginica_length_of_sepals)):
    if i in list_of_testing_indices:
        virginica_testing.append(virginica_length_of_sepals[i])
    else:
        virginica_training.append(virginica_length_of_sepals[i])


# create dataframes
virginica_test_df = pd.DataFrame({
    'iris virginica': virginica_testing
})
    
virginica_train_df = pd.DataFrame({
    'iris virginica': virginica_training
})

def compare_data_frames(test_value):
    virginica_t_statistic, virginica_p_value = stats.ttest_1samp(a=virginica_train_df, popmean=test_value)
    setosa_t_statistic, setosa_p_value = stats.ttest_1samp(a=train_dataframe, popmean=test_value)
    correct = setosa_p_value[0]<virginica_p_value[0]
    if correct:
        result = 'Success!'
    else:
        result = 'Failue :('
    print(f'Test Val = {test_value} Virginica: {virginica_p_value} Setosa: {setosa_p_value} {result}')

for i in virginica_testing:
    compare_data_frames(i)


virgin_train_y_vals = [0 for i in range(len(virginica_training))]
virgin_test_y_vals = [1 for i in range(len(virginica_testing))]


mean = np.mean(virginica_training)
std_dev = np.std(virginica_training)

# create an array of x-values
virgin_x_values = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, len(virginica_training))

# calculate the corresponding y-values for the bell curve
virgin_y_values = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(-(virgin_x_values - mean)**2 / (2 * std_dev**2))



plt.plot(virgin_x_values, virgin_y_values, color='green')


plt.scatter(virginica_testing, virgin_test_y_vals)
plt.scatter(virginica_training, virgin_train_y_vals)
plt.title("Distribution of testing and training data")


def test(elem):
    virginica_t_statistic, virginica_p_value = stats.ttest_1samp(a=virginica_train_df, popmean=elem[0])
    setosa_t_statistic, setosa_p_value = stats.ttest_1samp(a=train_dataframe, popmean=elem[0])

    if elem[1] == 'setosa': 
        success = setosa_p_value > virginica_p_value
    elif elem[1] == 'virginica':
        success = setosa_p_value < virginica_p_value
    return success


complete_test = []
for v in testing_data: 
    complete_test.append([v, 'setosa'])
for v in virginica_testing:
    complete_test.append([v, 'virginica'])

correct = 0
for t in complete_test:
    if test(t):
        correct+=1

print(f"Scored {correct} out of {len(complete_test)}")

plt.show()