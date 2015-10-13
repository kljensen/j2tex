import setuptools

setuptools.setup(
    name="jinjaxelatex",
    version="0.1.0",
    url="https://github.com/kljensen/jinjaxelatex",

    author="Kyle Jensen",
    author_email="kljensen@gmail.com",

    description="Python script to create templated XeLaTeX documents",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)