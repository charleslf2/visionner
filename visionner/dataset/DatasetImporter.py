import numpy as np 
import cv2
import os
import matplotlib.pyplot as plt 
from rich.panel import Panel
from rich.console import Console

console=Console()


def Normlization(dataset, dataset_shape):


    image_heigh_size=dataset_shape[1]

    #print("image hiegh size", image_heigh_size)

    image_chanel=dataset.shape[3]

    #print("Image chanel",image_chanel )

    # reshape

    normalize_dataset=np.reshape(dataset, [-1, image_heigh_size, image_heigh_size, image_chanel])

    normalize_dataset=dataset.astype("float32")/250


    normalize_dataset_shape=normalize_dataset.shape

            
    # print the dataset shape 
    console.print(Panel.fit(f"{normalize_dataset_shape}", title="You Normalized dataset shape", title_align="center"))


    #print("Normalize_dataset\n", normalize_dataset)

    # show the datset with matplotlib
    plt.figure()
    for i in range(10):
        plt.subplot(2, 5, i + 1)
        plt.suptitle("10 first image in your Normalized dataset")
        plt.imshow(normalize_dataset[i])

    plt.show()
    
    return normalize_dataset



def UnsupervisedImporter(path, size=(28, 28), normalize=True):
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
    >>> your_dataset=Vision("path/to/your/dataset/", size=(28, 28), normalize=True)

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