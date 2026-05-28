from setuptools import setup, find_packages

setup(
    name='hangul-speller',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyQt5>=5.15',
    ],
    python_requires='>=3.10',
)
