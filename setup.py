import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='opensea-wrapper',
    version='0.1.8',
    scripts=[],
    author="apinanyogaratnam",
    author_email="apinanapinan@icloud.com",
    description="opensea wrapper functions to use in your projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apinanyogaratnam/opensea-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
