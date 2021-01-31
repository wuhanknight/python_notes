# This is a sample Python script.
import numpy as np
import pandas as pd

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import nltk


from os import getcwd

filePath = f"{getcwd()}/../tmp2/"
print (filePath)

y_hat = [1,1,0] # list
test_y= np.array([[1],[1],[1]]) # array

print(y_hat)
print(test_y)
print(len(test_y))

accuracy = (y_hat == test_y.squeeze()).sum() / len(y_hat)
(y_hat == test_y).sum() / len(test_y)

freqs = {('good',1):3,('good',0):1}


freqs_2 = set([pair[0] for pair in freqs.keys() ])
freqs_3 = [pair[0] for pair in freqs.keys() ]

my_list = ['a','b','c']
my_list2 = ['a','f','c']
my_list3 = [my_list, my_list2 ]

df = pd.DataFrame([[1, 1.5],[1,2]], columns=['int', 'float'])
x = np.array([[11,12,13], [21,22, 23]])
x_row = np.array([1,2])
x_col = np.array([[1,2]])


np.random.seed(0)
planes_l = [np.random.normal(size=(2, 3))
            for aaa in range(3)]

best_words={}
my_dict = {'a':1, 'b':2, 'c':3}
for w in my_dict:
    best_words[w] = my_dict.get(w, 0)
dict_vals = my_dict.values()

A=pd.DataFrame([[1,2,3],[4,5,6,],[7,8,9]], index=['row1','row2','row3'], columns=['col1','col2','col3'])
B=np.array([[1,2,3],[4,5,6]])

set_1 = set(my_list)
set_2 = set(my_list2)

my_list4 = [('a'), ('b',), ('c','d')]