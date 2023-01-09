from setuptools import setup, find_packages



setup(
    name="visionner",
    version="0.0.1",
    description="the package you need for your custom Image dataset",
    install_requires=["numpy", "opencv-python", "matplotlib", "rich"],
    packages=find_packages()
)