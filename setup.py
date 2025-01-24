from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="brainboost_data_tools_pipe_pii_package",
    version="0.1.0",
    author="Pablo Tomas Borda",
    author_email="pablotomasborda@gmail.com",
    description="A package for filtering and anonymizing personal data using Presidio.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/brainboost_data_tools_pipe_pii_package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "presidio-analyzer",
        "presidio-anonymizer",
    ]
)
