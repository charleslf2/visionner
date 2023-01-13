# visionner
Visionner is a image dataset  toolkit

#### Purpose of the package
+ The purpose of this package is to provide machine learning engineer a image dataset toolkit

### Warning

Since Visionner still in alpha and under heavy development , expect to see many changes in the near futures.

#### Features
+ Convert image folder into numpy array
+ Import a dataset for unsupervised learning tasks
+ Import a dataset for supervised learning tasks
+ Normalize the dataset
+ Split the trainset and the testset


### Getting Started
The package can be found on pypi hence you can install it using pip

#### Installation

```bash

pip install visionner

```

### Usage
```python

### import usefull package
>>> from visionner.Dataset.DatasetManager import DatasetImporter, DatasetNormalizer, TrainTestSpliter
>>> import matplotlib.pyplot as plt 

### import your dataset
>>> your_dataset=DatasetImporter("path/to/your/dataset/", size=(28, 28))

### normalize your dataset
>>> your_normalized_dataset=DatasetNormalizer(your_dataset)

### create a trainset and a testset
>>>x_train, x_test=TrainTestSpliter(dataset, test_size=0.2)

### visualize the first image of your dataset
>>> plt.imshow(your_dataset[0])
>>> plt.show()

```


### Contribution
Contribution are welcome.
Notice a bug ? let us know. Thanks you

### Author
+ Main Maitainer : Charles TCHANAKE
+ email : datadevfernolf@gmail.com 

### Note 

If you get an unicode error like  this :

```
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

```

add **r** at the begining of your path like this:

```python
>>> your_dataset=Vision(r"path/to/your/dataset/", size=(28, 28), normalize=True)
```

### Warning

Since Visionner still in alpha and under heavy development , expect to see many changes in the near futures.