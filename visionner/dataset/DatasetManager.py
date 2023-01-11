import numpy as np 
import cv2
import os
import matplotlib.pyplot as plt 
from rich.panel import Panel
from rich.console import Console

console=Console()



def display(dataset, title):
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
    path : a path that of your image dataset || should be a directory

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
    display(dataset, title="Your dataset info")

    return dataset
    

    
   

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
    display(normalize_dataset, title="Your normalized dataset info" )
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

    print("X_test number", x_test_number)
    x_test_number=int(x_test_number)

    print("X_test number", x_test_number)
    x_test=dataset[: x_test_number]
    x_train=dataset[x_test_number :]

    

    # display
    display(x_train, title="x-train shape")
    display(x_test, title="x-test shape")

    return x_train,x_test
    

    