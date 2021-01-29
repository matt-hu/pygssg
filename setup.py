import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygssg",
    version="0.0.1",
    author="Matt H",
    author_email="matt.hu1@outlook.com",
    description="A wrapper for gssg",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matt-hu/pygssg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ],
    python_requires='>=3.6',
)