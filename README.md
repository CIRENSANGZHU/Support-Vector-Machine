# Support-Vector-Machine  
Realize the Support Vector Machine (SVM) algorithm using Python and libsvm, and compare the results of different kernels or parameters.  
SVM can solve linear separable problems, but can not solve linear inseparable problems directly. For linear inseparable problems, if you want to use SVM algorithm, you have to do it with the help of kernel method. You have to use some kinds of kernel function to preprocess the data, that is, mapping the data to a high dimensional space. There are already some famous kernel functions, and this project tries the linear kernel and the Gaussian kernel with different parameters.  
Fistly, we use Watermelon Data Set 3.0 α shown as the Table 4.5 on page 89 of *Machine Learning* written by prof. Zhou Zhihua as our training data. Put the data into an excel file, and write a Python program to read the data and organize the data into the form that be used by libsvm. Then, use libsvm to train a SVM model with different kernels or parameters. Finally, get and compare the results. The tool svm-toy in libsvm can be used to visualize the results.  
# 支持向量机  
使用python和libsvm软件包实现了支持向量机，并比较了使用不同核或参数得到的结果。
支持向量机可以解决线性可分的问题，但不能直接解决线性不可分问题。对于线性不可分问题，如果想要使用支持向量机解决，那么需要用到核方法，使用某种核函数将训练数据映射到更高维的空间中去。目前已经有一些著名的和函数，本项目尝试了线性核与不同参数的高斯核。  
首先，使用周志华教授《机器学习》89页表4.5中的西瓜数据集3.0α作为训练数据，将数据写入excel文件，并编写Python代码，按照libsvm的数据格式从excel文件中读取数据。然后，利用libsvm软件包使用不同的核函数与参数训练支持向量机。最后得到结果并进行比较。libsvm软件包中的svm-toy可以用来对结果进行可视化。
