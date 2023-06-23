# Installation
- step 1 

```bash
git clone https://github.com/charleslf2/visionner
```  

- step 2

```bash
cd visionner
```
- step 3 

```bash
py setup.py install
```


# Usage

```python3

>>> from visionner.core import DatasetImporter

>>> your_dataset=DatasetImporter("path/to/your/dataset/", size=(28, 28))

```

```python3

>>> from visionner.core import SupervisedImporter

>>> features, labels= SupervisedImporter("path/to/your/dataset", categories=["cat", "dog"], size=(28,28))

```

```python3

### normalize your dataset

>>> from visionner.core import DatasetNormalizer

>>> your_normalized_dataset=DatasetNormalizer(your_dataset)

```

```python3

### create a trainset and a testset

>>> from visionner.core import TrainTestSpliter

>>> x_train, x_test=TrainTestSpliter(dataset, test_size=0.2)

```

```python3

### visualize the first image of your dataset

>>> import matplotlib.pyplot as plt 

>>> plt.imshow(your_dataset[0])
>>> plt.show()

```

```python3

### save your dataset

>>> from visionner.core import DatasetSaver

>>> DatasetSaver("my_saved_dataset", your_dataset)

```

```python3

### open your dataset

>>> from visionner.core import DatasetOpener

>>> my_saved_dataset=DatasetOpener("my_saved_dataset.npy") 

```
