import xlrd
import matplotlib.pyplot as plt

from libsvm.commonutil import *
from libsvm.svm import *
from libsvm.svmutil import *

data_list = xlrd.open_workbook('Watermelon_Dataset_3.0alpha.xlsx')  # read data list
sheet1 = data_list.sheets()[0]  # there is only one sheet in the file

row_num = sheet1.nrows
sample_num = row_num - 1  # the total number of samples
# print(sample_num)

col_num = sheet1.ncols
attribute_num = col_num - 2  # the total number of attribute for each sample
# print(attribute_num)

# create data for libsvm in required form
category_list = []  # list the class of each sample
sample_list = []  # list the value of each attribute of each sample
for i in range(sample_num):
    # i = 0, 1, ..., (sample_num-1)
    category_list.append(sheet1.cell(i+1, 3).value)

    sample = {}
    sample[1] = sheet1.cell(i+1, 1).value
    sample[2] = sheet1.cell(i+1, 2).value
    sample_list.append(sample)
print('the category of each sample: \n', category_list)
print('the values of attributes of each sample: \n', sample_list)

# visualize the samples
density = []
sugar_content = []
for i in range(sample_num):
    # i = 0, 1, ..., (sample_num-1)
    density.append(sheet1.cell(i+1, 1).value)
    sugar_content.append(sheet1.cell(i + 1, 2).value)
# print(density)
# print(sugar_content)
scatter1 = plt.scatter(density[0:8], sugar_content[0:8], c='g')
scatter2 = plt.scatter(density[8:17], sugar_content[8:17], c='r')
plt.title('Scatter Plot of samples')
plt.xlabel('density')
plt.ylabel('sugar content')
plt.legend((scatter1, scatter2), ('good', 'bad'), loc = 'best')
# plt.show()


# use libsvm to train a model with different parameters
# use linear kernel
# options_linear_kernel = '-t 0 -c 100 -b 1'
# model_linear_kernel = svm_train(category_list, sample_list, options_linear_kernel)
# svm_save_model('svm_model_linear_kernel.txt', model_linear_kernel)

# use gaussian kernel, gamma = 0.001
# options_gaussian_kernel_gamma_0_001 = '-t 2 -g 0.001 -c 100 -b 1'
# model_gaussian_kernel = svm_train(category_list, sample_list, options_gaussian_kernel_gamma_0_001)
# svm_save_model('svm_model_gaussian_kernel_gamma_0_001.txt', model_gaussian_kernel)

# use gaussian kernel, gamma = 0.01
# options_gaussian_kernel_gamma_0_01 = '-t 2 -g 0.01 -c 100 -b 1'
# model_gaussian_kernel = svm_train(category_list, sample_list, options_gaussian_kernel_gamma_0_01)
# svm_save_model('svm_model_gaussian_kernel_gamma_0_01.txt', model_gaussian_kernel)

# use gaussian kernel, gamma = 0.1
# options_gaussian_kernel_gamma_0_1 = '-t 2 -g 0.1 -c 100 -b 1'
# model_gaussian_kernel = svm_train(category_list, sample_list, options_gaussian_kernel_gamma_0_1)
# svm_save_model('svm_model_gaussian_kernel_gamma_0_1.txt', model_gaussian_kernel)

# use gaussian kernel, gamma = 1
# options_gaussian_kernel_gamma_1 = '-t 2 -g 1 -c 100 -b 1'
# model_gaussian_kernel = svm_train(category_list, sample_list, options_gaussian_kernel_gamma_1)
# svm_save_model('svm_model_gaussian_kernel_gamma_1.txt', model_gaussian_kernel)

# use gaussian kernel, gamma = 10
# options_gaussian_kernel_gamma_10 = '-t 2 -g 10 -c 100 -b 1'
# model_gaussian_kernel = svm_train(category_list, sample_list, options_gaussian_kernel_gamma_10)
# svm_save_model('svm_model_gaussian_kernel_gamma_10.txt', model_gaussian_kernel)

# use gaussian kernel, gamma = 100
# options_gaussian_kernel_gamma_100 = '-t 2 -g 100 -c 100 -b 1'
# model_gaussian_kernel = svm_train(category_list, sample_list, options_gaussian_kernel_gamma_100)
# svm_save_model('svm_model_gaussian_kernel_gamma_100.txt', model_gaussian_kernel)

# use libsvm to test a sample
# category_test = [-1]
# sample_test = [{1: 0.719, 2: 0.103}]
# p_label, p_acc, p_val = svm_predict(category_test, sample_test, model, '-b 1')


