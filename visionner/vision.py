import numpy as np 
import cv2
import os
import matplotlib.pyplot as plt 
from rich.panel import Panel
from rich.console import Console


console=Console()


def Vision(path, train_test_split=True):

    isDirectory = os.path.isdir(path)
    print(isDirectory)
    if isDirectory==False:
        raise TypeError("The path should be a directory")
    else:
        print("your path is a directory")

    dataset=[]
    

    for file_name in os.listdir(path):
        img=cv2.imread(os.path.join(path, file_name))
        img=cv2.resize(img, (200,250))
        dataset.append(img)

    dataset=np.array(dataset)

    dataset_shape=dataset.shape


    # print the dataset shape 
    console.print(Panel.fit(f"{dataset_shape}", title="your dataset shape", title_align="center"))

    # show the datset with matplotlib

    #plt.imshow(dataset[10])
    #plt.show()
    for i in range(10):
        plt.subplot(2, 5, i + 1)
        plt.imshow(dataset[i])
  
    plt.show()


    # train test split
    if train_test_split==True:
        image_heigh_size=dataset_shape[1]
        print("image hiegh size", image_heigh_size)
        # reshape

        #x_train=np.reshape(x_train, [-1, image_size, image_size, 3])
        #x_test=np.reshape(x_test, [-1, image_size, image_size, 3])
    else:
        pass
    return dataset