from rich.console import Console
from matplotlib.pylab import plt 
import numpy as np
from rich.panel import Panel


console=Console()

def Normlization(dataset, dataset_shape):


    image_heigh_size=dataset_shape[1]
    print("image hiegh size", image_heigh_size)

    image_chanel=dataset.shape[3]

    print("Image chanel",image_chanel )

    # reshape

    normalize_dataset=np.reshape(dataset, [-1, image_heigh_size, image_heigh_size, image_chanel])

    normalize_dataset=dataset.astype("float32")/250


    normalize_dataset_shape=normalize_dataset.shape

            
    # print the dataset shape 
    console.print(Panel.fit(f"{normalize_dataset_shape}", title="Normalize dataset shape", title_align="center"))
    print("Normalize_dataset\n", normalize_dataset)

    # show the datset with matplotlib

    for i in range(10):
        plt.subplot(2, 5, i + 1)
        plt.title("Normalize dataset")
        #plt.colorbar()
        plt.imshow(normalize_dataset[i])
        plt.show()
    
    return normalize_dataset