import numpy as np 
import cv2
import os
import matplotlib.pyplot as plt 
from rich.panel import Panel
from rich.console import Console
import random
from rich.tree import Tree
from rich import print

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

        if imagenumber>10:
            for i in range(10):
                plt.subplot(2, 5, i + 1)
                plt.suptitle("First 10 images in your dataset")
                plt.imshow(dataset[i])

            plt.show()

        elif imagenumber<1:
            plt.imshow(dataset[1])
            plt.show()


def issupported(path):
    issupported=True
    filename,file_ext=os.path.splitext(path)
    support_list=['.jpg','.jpeg','.png','.JPG','.jfif']

    if file_ext in support_list:
        issupported=True
    else:
        print(f"{file_ext} is not supported" )
        issupported=False
    return issupported


def reshape_it(dataset):
    if len(dataset.shape)==1:
        dataset=np.reshape(dataset,
                   (1,dataset.shape[0],dataset.shape[1],dataset.shape[2]))
        print(dataset.shape)
    else:
        pass
    return dataset


def DatasetImporter(path, size=(28, 28)):

    isDirectory = os.path.isdir(path)

    if isDirectory==False:
        raise TypeError("The path should be a directory")

    dataset=[]
        

    for file_name in os.listdir(path):
        if issupported(file_name):
            img=cv2.imread(os.path.join(path, file_name))
            img=cv2.resize(img, size)
            img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            dataset.append(img)
        else:
            pass

    dataset=np.array(dataset)
    
    print(dataset.shape)

    #display
    Displayer(dataset, title="Your dataset info")

    return dataset
    


def SupervisedImporter(path, categories, size=(28, 28)):
    
    print("Your dataset should look like this : ")

    tree=Tree("Your Dataset directory",guide_style="bold")

    Category1=tree.add("Category 1")
    Category2=tree.add("Category 2")
    Category1.add("Image_01")
    Category1.add("Image_02")
    Category1.add("Image_03")

    Category2.add("Image_01")
    Category2.add("Image_02")
    Category2.add("Image_03")

    print(tree)

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
            if issupported(file_name):
                img=cv2.imread(os.path.join(dir_path, file_name))
                img=cv2.resize(img, size)
                img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                dataset.append([img, class_num])
            else:
                pass


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


    img_row=dataset.shape[1]
    img_col=dataset.shape[2]
    channel=dataset.shape[3]

    dataset=dataset.astype('float32')/255

    norm_dataset=dataset.reshape(dataset.shape[0], img_row, img_col, channel)

    # display
    Displayer(norm_dataset, title="Your normalized dataset info" )
    return norm_dataset



def TrainTestSpliter(dataset, test_size=0.2):

    isList=type(dataset)==list
    
    dataset_shape=0

    if isList==True:

        dataset_shape=len(dataset)

        print("dataset shape =",dataset_shape)

        x_test_number=(dataset_shape*test_size)

        x_test_number=int(x_test_number)    

        x_test=dataset[: x_test_number]

        x_train=dataset[x_test_number :]


    else:
        dataset_shape=dataset.shape


        print("dataset shape =",dataset_shape)

        x_test_number=(dataset_shape[0]*test_size)

        x_test_number=int(x_test_number)    

        x_test=dataset[: x_test_number]

        x_train=dataset[x_test_number :]

        # display
        Displayer(x_train, title="x-train info")
        Displayer(x_test, title="x-test info")

    return x_train,x_test


def DatasetSaver(dataset_name, dataset):
        np.save(dataset_name, dataset)

       

def DatasetOpener(dataset_name:str):
   dataset= np.load(dataset_name + ".npy")
   return dataset
