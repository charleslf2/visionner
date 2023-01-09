import numpy as np 
import cv2
import os
import matplotlib.pyplot as plt 
from rich.panel import Panel
from rich.console import Console


console=Console()


def Vision(path):

    isDirectory = os.path.isdir(path)
    print(isDirectory)
    if isDirectory==False:
        raise TypeError("The path should be a directory")
    else:
        print("your path is a directory")

    dataset=[]
    

    for file_name in os.listdir(path):
        img=cv2.imread(os.path.join(path, file_name))
        img=cv2.resize(img, (200,200))
        dataset.append(img)

    dataset=np.array(dataset)

    dataset_shape=dataset.shape


    # print the dataset shape 
    console.print(Panel.fit(f"{dataset_shape}", title="your dataset shape", title_align="center"))

    # show the datset with matplotlib

    plt.imshow(dataset[10])
    plt.show()

    return dataset