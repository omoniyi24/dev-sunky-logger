import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devsunkylogger",
    version="0.0.2",
    author="Ilesanmi Omoniyi",
    author_email="omoniyi24@gmail.com",
    description="A log package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omoniyi24/dev-sunky-logger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)