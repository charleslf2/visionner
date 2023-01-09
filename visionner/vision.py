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
    print(isDirectory)
    if isDirectory==False:
        raise TypeError("The path should be a directory")
    else:
        print("your path is a directory")

    dataset=[]
    

    for file_name in os.listdir(path):
        img=cv2.imread(os.path.join(path, file_name))
        img=cv2.resize(img, size)
        dataset.append(img)

    dataset=np.array(dataset)

    dataset_shape=dataset.shape


    console.print(Panel.fit(f"{dataset_shape}", title="your dataset shape", title_align="center"))
    print("Dataset\n", dataset)

    for i in range(10):
        plt.subplot(2, 5, i + 1)
        plt.title("dataset")
        #plt.colorbar()
        plt.imshow(dataset[i])
  
    plt.show()


    # Normalize
    if normalize==True:

        dataset=Normlization(dataset, dataset_shape)

    else:
        pass


    

    return dataset