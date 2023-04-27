import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = '0.0.3'

deps = [
    'pandas',
    'numpy',
    'plotly',
    'xlwings'
]

setuptools.setup(
    name="eqparse", 
    version=version,
    author="Michael Sweeney",
    author_email="michael.samuel.sweeney@gmail.com",
    description="reads SIM and HSR files produced by eQUEST simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simularis/eqparse",
    packages=setuptools.find_packages(),
    install_requires=deps,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)