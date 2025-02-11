from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="DynamicDoc",
    version="1.0.2",
    author="Samuel Santos",
    author_email="samuels.g.desouza@gmail.com",
    description="Uma biblioteca para manipulação dinâmica de documentos docx.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Especifica que o README é em Markdown
    url="https://github.com/SamuelSGSouza/Dynamic-Docs",
    packages=['DynamicDoc/'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'python-docx',
    ],
)