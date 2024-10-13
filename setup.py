from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="DynamicDocs",
    version="0.1.0",
    author="Samuel Santos",
    author_email="samuels.g.desouza@gmail.com",
    description="Uma biblioteca para manipulação dinâmica de documentos docx.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Especifica que o README é em Markdown
    url="https://github.com/seurepositorio/dynamicdoc",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'python-docx',
        # Outras dependências
    ],
)
