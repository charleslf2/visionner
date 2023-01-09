import numpy as np 
import cv2
import os
import matplotlib.pyplot as plt 
from rich.panel import Panel
from rich.console import Console
from visionner.normalize import Normlization

console=Console()


def Vision(path, size=(28, 28), normalize=True):

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