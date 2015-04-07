# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="django-translate",
    version="1.0.3",
    author="Adam Zieliński",
    author_email="adam@sf2.guru",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/adamziel/django_translate",

    license="MIT",
    description="Non-gettext translations for django.",

    # Dependent packages (distributions)
    install_requires=[
        "python_translate"
    ],
)
