from setuptools import setup, find_packages

VERSION = '0.0.7' 
DESCRIPTION = "Turn raw image dataset into numpy array ; more suitable for deep learning tasks"

setup(
        name="visionner", 
        version=VERSION,
        author="charles TCHANAKE",
        author_email="datadevfernolf@gmail.com",
        url="https://github.com/charleslf2/visionner",
        description=DESCRIPTION,
        long_description_content_type="text/markdown",
        long_description=open("README.md","r",encoding="utf-8").read(),
        packages=find_packages(),
        install_requires=["numpy","opencv-python",
                          "matplotlib","rich"],  
        keywords=["Computer-vision",
        "preprocessing","Images","Dataset","visionner"],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
