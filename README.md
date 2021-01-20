# Support-Vector-Machine  
Realize the Support Vector Machine (SVM) algorithm using Python and libsvm, and compare the results of different kernels or parameters.  
SVM can solve linear separable problems, but can not solve linear inseparable problems directly. For linear inseparable problems, if you want to use SVM algorithm, you have to do it with the help of kernel method. You have to use some kinds of kernel function to preprocess the data, that is, mapping the data to a high dimensional space. There are already some famous kernel functions, and this project tries the linear kernel and the Gaussian kernel with different parameters.  
Fistly, we use Watermelon Data Set 3.0 α shown as the Table 4.5 on page 89 of *Machine Learning* written by prof. Zhou Zhihua as our training data. Put the data into an excel file, and write a Python program to read the data and organize the data into the form that be used by libsvm. Then, use libsvm to train a SVM model with different kernels or parameters. Finally, get and compare the results. The tool svm-toy in libsvm can be used to visualize the results.  
# 支持向量机  
使用python和libsvm软件包实现了支持向量机，并比较了使用不同核或参数得到的结果。
