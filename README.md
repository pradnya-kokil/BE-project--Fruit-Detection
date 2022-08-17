# BE-project--Fruit-Detection
Fruit and Vegetable identification system using efficient convolutional Neural Networks for transfer learning

Software and Libraries used :

Programming Language : Python 3.8
Model: VGG16
Software/ Package Manager : Anaconda-Jupyter notebook
Libraries : Keras & Machine Learning Libraries
Dataset: Fruits 360 Kaggle
Web Framework: Flask

Steps:

1. Firstly, we have imported the libraries and did data augmentation using ImageGenerator dataset.
2. After that we have performed transfer learning of VGG16 model to extract the feature of convolution layer.
3. We have trained our model on fully connected layer for our customized dataset(On train and test dataset).
4. Deployed our model into web app with flask.
4. And finally, tested the model and we have predicted the class of given image.

Result and Conclusion:

Hence, we detected several fruits and vegetables with a system accuracy of 91.3%.
The web app detects images when the image is uploaded directly or the URL of the fruits and vegetables is given.
It also gives calorie content per 100g of fruit or vegetables.
