from setuptools import setup
import os

name = "plaid-stubs"
description = "Plaid stubs"

long_description = """
# Experimental Plaid type stubs

This package contains type stubs to provide more precise
static types and type inference for plaid-python, the official
python client library for the Plaid API.

## Installation

```
pip install plaid-stubs
```
""".strip()


def find_stub_files():
    result = []
    for root, _dirs, files in os.walk(name):
        for file in files:
            if file.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


setup(
    name=name,
    version="0.2",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    url="https://github.com/monarchmoney/plaid-stubs",
    install_requires=["mypy>=0.761", "typing-extensions>=3.7.4.1", "plaid-python>=3.7.0",],
    packages=[name],
    package_data={name: find_stub_files()},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
