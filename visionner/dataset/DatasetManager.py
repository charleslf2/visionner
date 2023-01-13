import numpy as np 
import cv2
import os
import matplotlib.pyplot as plt 
from rich.panel import Panel
from rich.console import Console
import random

console=Console()



def Displayer(dataset, title):
        dataset_shape=dataset.shape
        imagenumber=dataset_shape[0]
        width=dataset_shape[1]
        heigh=dataset_shape[2]
        chanel=dataset_shape[3]
        console.print(Panel.fit
        (f"Total Images --> {imagenumber} \nImage Width --> {width} \nImage Heigh --> {heigh} \nImage Channel --> {chanel}", 
        title=f"{title}", title_align="center"))

        plt.figure(figsize=(20, 10))
        for i in range(10):
            plt.subplot(2, 5, i + 1)
            plt.suptitle("First 10 images in your dataset")
            plt.imshow(dataset[i])

        plt.show()



def DatasetImporter(path, size=(28, 28)):

    """
    This function take an image dataset directory and transform it into a numpy array

    Params
    ======
    path : A path  of your images directory || should be a directory

    size : (28, 28) by default || specify the Width and the Heigh of your images  || should be a tuple 

    Usage
    =====
    ### import usefull package

    >>> from visionner.Dataset import DatasetManager
    >>> import matplotlib.pyplot as plt 

    ### basic usage

    >>> your_dataset=DatasetManager.DatasetImporter("path/to/your/dataset/", size=(28, 28))

    ### visualize the first image

    >>> plt.imshow(your_dataset[0])
    >>> plt.show()

    """


    isDirectory = os.path.isdir(path)

    if isDirectory==False:
        raise TypeError("The path should be a directory")

    dataset=[]
        

    for file_name in os.listdir(path):
        img=cv2.imread(os.path.join(path, file_name))
        img=cv2.resize(img, size)
        img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        dataset.append(img)

    dataset=np.array(dataset)

    #display
    Displayer(dataset, title="Your dataset info")

    return dataset
    


def SupervisedImporter(path, categories, size=(28, 28)):
    
    """
    This functions help you import your dataset for supervised learning tasks

    Params
    ======
    path : A path  of your images directory || should be a directory

    categories: The list of different labels categories || should be a List

    size : (28, 28) by default || specify the Width and the Heigh of your images  || should be a tuple 

    """

    isDirectory = os.path.isdir(path)
    isList=type(categories)==list

    if isDirectory==False:
        raise TypeError("The 'path' argument should be a directory")
    
    if isList==False:
        raise TypeError("The 'categories' argument should be a list")


    dataset=[]
    for category in categories:
        dir_path=os.path.join(path, category)
        class_num=categories.index(category)
        for file_name in os.listdir(dir_path):
            img=cv2.imread(os.path.join(dir_path, file_name))
            img=cv2.resize(img, size)
            img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            dataset.append([img, class_num])


    random.shuffle(dataset)

    X=[]
    y=[]

    for features, label in dataset:
        X.append(features)
        y.append(label)

    X=np.array(X)
    
    
    # display features

    Displayer(X, "Your dataset features info")

    # display label
   
    label_len=len(y)
    console.print(Panel.fit(f"Total Labels --> {label_len}", title="Your dataset Labels info", title_align="center"))
    console.print(Panel.fit(f"{y[: 10]}", title="First 10 labels in your dataset", title_align="center"))

    result=[]

    for category in categories:
        class_num=categories.index(category)
        result.append(f"{category} --> {class_num}")

    console.print(Panel.fit(f"{result}", title="Your labels indexes", title_align="center"))


    return X, y
    
    
    
def DatasetNormalizer(dataset):
    """
    This function return a normalized version of your dataset

    Params:
    ======
    dataset : a numpy array image dataset

    Usage:
    ======
    ### import usefull package

    >>> from visionner.Dataset import DatasetManager

    ### normalize your dataset

    >>> your_normalized_dataset=DatasetManager.DatasetNormalizer(dataset)

    ### visualize your dataset

    >>> print(your_normalized_dataset) 
     
    """

    dataset_shape=dataset.shape

    image_heigh_size=dataset_shape[1]

    image_chanel=dataset.shape[3]

    normalize_dataset=np.reshape(dataset, [-1, image_heigh_size, image_heigh_size, image_chanel])

    normalize_dataset=dataset.astype("float32")/255

    # display
    Displayer(normalize_dataset, title="Your normalized dataset info" )
    return normalize_dataset




def TrainTestSpliter(dataset, test_size=0.2):
    """
    This function return the x_train and the y_train of your dataset

    Params:
    =======
    dataset : a numpy array image dataset

    test_size : the size of your x_test

    Usage:
    ======
    ### import useful package

    >>> import visionner.Dataset.DatasetManager import TrainTestSpliter

    ### split your dataset

    >>> x_train, x_test=TrainTestSpliter(dataset, test_size=0.2)
    
    """
    dataset_shape=dataset.shape

    x_test_number=(dataset_shape[0]*test_size)

    x_test_number=int(x_test_number)    

    x_test=dataset[: x_test_number]
    x_train=dataset[x_test_number :]

    

    # display
    Displayer(x_train, title="x-train info")
    Displayer(x_test, title="x-test info")

    return x_train,x_test



    