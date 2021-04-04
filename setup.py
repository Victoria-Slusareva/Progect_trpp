from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bookshop_database_sva",
    version="1.0",
    author="Слюсарева Виктория",
    description="Информационная система книжного магазина",
    long_description=long_description,
    url="https://github.com/Victoria-Slusareva/Progect_trpp",
    packages=find_packages(),
    classifiers=[
        "Язык программирования :: Python :: 3.9",
        "Модуль для создания GUI :: PyQt5 :: 5.15.4"
    ],
    python_requires='>=3.9',
)
