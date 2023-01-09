# visionner
Visionner convert your image dataset into a numpy array ; more suitable for computer vision tasks.

#### Purpose of the package
+  The purpose of this package is to convert your image dataset into a numpy array wich is more suitable for Image processing , deep learning and computer vision tasks.


#### Features
+  Convert image folder into numpy array


### Getting Started
The package can be found on pypi hence you can install it using pip

#### Installation

```bash

pip install visionner

```
### Usage
```python

### import usefull package
>>> from visionner import Vision
>>> import matplotlib.pyplot as plt 

### basic usage
>>> your_dataset=Vision("path/to/your/dataset/", size=(28, 28), normalize=True)

### visualize the first image
>>> plt.imshow(your_dataset[0])
>>> plt.show()

```


### Contribution
Contribution are welcome.
Notice a bug ? let us know. Thanks you

### Author
+ Main Maitainer : Charles TCHANAKE
+ email : datadevfernolf@gmail.com 