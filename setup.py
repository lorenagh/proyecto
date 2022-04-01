import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SelfCareBot",
    version="0.0.1",
    author="Lore, Fran y Nico",
    # author_email="autor@ejemplo.com",
    description="Bot de autocuidado",
    long_description='Te recomienda qué hacer según tu estado de ánimo y cómo va tu día',
    long_description_content_type="text/markdown",
    url="https://github.com/lorenagh/selfcare_bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
