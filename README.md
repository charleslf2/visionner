# Installation
- put the visionner.py file in your directory
  
- install the requirements.txt 

```bash
pip install -r requirements.txt
```

# Usage
```python3
### import your dataset (more suitable for dataset without labels)

>>> from visionner import DatasetImporter

>>> your_dataset=DatasetImporter("path/to/your/dataset/", size=(28, 28))

### import your supervised dataset (more suitable for dataset with labels)

>>> from visionner import SupervisedImporter

>>> features, labels= SupervisedImporter("path/to/your/dataset", categories=["cat", "dog"], size=(28,28))

### normalize your dataset

>>> from visionner import DatasetNormalizer

>>> your_normalized_dataset=DatasetNormalizer(your_dataset)

### create a trainset and a testset

>>> from visionner import TrainTestSpliter

>>> x_train, x_test=TrainTestSpliter(dataset, test_size=0.2)

### visualize the first image of your dataset

>>> import matplotlib.pyplot as plt 

>>> plt.imshow(your_dataset[0])
>>> plt.show()

### save your dataset

>>> from visionner import DatasetSaver

>>> DatasetSaver("my_saved_dataset", your_dataset)

### open your dataset

>>> from visionner import DatasetOpener

>>> my_saved_dataset=DatasetOpener("my_saved_dataset.npy") 
```
