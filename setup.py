import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="steggar",
    version="0.0.1",
    author="...",
    author_email="dannislife6@gmail.com",
    description="Tool for steganography",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'src=src.console:main',
            ],
        },
    python_requires='>=3',
    install_requires=['numpy', 'cryptography', 'Pillow']
)
