import setuptools

setuptools.setup(
    name="PyCross",
    version="0.1",
        author="Sally Jiang",
    author_email="sally.jiang@yale.edu",
    description="Picross player in Python",
    packages=setuptools.find_packages(include=['createpicross','Game'])
    python_requires='>=3',
    install_requires=["numpy","matplotlib"]
)

# check preset images are in file: 

