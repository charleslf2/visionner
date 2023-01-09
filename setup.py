from setuptools import setup, find_packages

classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Development Status :: 4 - Beta"
]

setup(
    name="visionner",
    version="0.0.1",
    description="Visionner convert your image dataset into a numpy array ; more suitable for computer vision tasks",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/charleslf2/Visionner",
    project_urls={
        "Bug Tracker":"https://github.com/charleslf2/Visionner/issues"
    },
    author="Charles TCHANAKE",
    author_email="datadevfernolf@gmail.com",
    license="MIT",
    classifiers=classifiers,
    install_requires=["numpy", "opencv-python", "matplotlib", "rich"],
    packages=find_packages()
)