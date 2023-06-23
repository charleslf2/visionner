from setuptools import setup, find_packages

VERSION = '0.0.6' 
DESCRIPTION = 'manipulate your image dataset easly'

setup(
        name="visionner", 
        version=VERSION,
        author="charles TCHANAKE",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        #long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["numpy","opencv-python",
                          "matplotlib","rich"],  
        keywords=['python'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
