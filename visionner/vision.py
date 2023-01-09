import numpy as np 
import cv2
import os
import matplotlib.pyplot as plt 
from rich.panel import Panel
from rich.console import Console
from visionner.normalize import Normlization

console=Console()


def Vision(path, size=(28, 28), normalize=True):
    """
    This function take an image dataset directory and transform it into a numpy array

    Params
    ======
    path : a path that of your image dataset || should be a directory

    size : (28, 28) by default || specify the Width and the Heigh of your images  || should be a tuple 

    normlize : True by default || Normalize your image dataset || should be True or False 

    Usage
    =====
    ### import usefull package
    >>> from visionner import Vision
    >>> import matplotlib.pyplot as plt 

    ### basic usage
    >>> your_dataset=Vision("path/to/your/dataset/", size=(28, 28), normlize=True)

    ### visualize the first image
    >>> plt.imshow(your_dataset[0])
    >>> plt.show()

    """

    isDirectory = os.path.isdir(path)

    #print(isDirectory)

    if isDirectory==False:
        raise TypeError("The path should be a directory")
    else:
        pass
        #print("your path is a directory")

    dataset=[]
    

    for file_name in os.listdir(path):
        img=cv2.imread(os.path.join(path, file_name))
        img=cv2.resize(img, size)
        dataset.append(img)

    dataset=np.array(dataset)

    dataset_shape=dataset.shape


    console.print(Panel.fit(f"{dataset_shape}", title="Your dataset shape", title_align="center"))


    #print("Dataset\n", dataset)

    # Normalize
    if normalize==True:

        dataset=Normlization(dataset, dataset_shape)

    else:

        for i in range(10):
            plt.subplot(2, 5, i + 1)
            plt.suptitle("20 fisrt image in your Dataset")
            plt.imshow(dataset[i])

        plt.title("dataset")
        plt.show()


    return dataset