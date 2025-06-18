## The `__init__.py` file

This kind of file tells python that the directory should be treated as a package. It can be empty, or it can contain initialization code for the package.

When you import a package in Python, the __init__.py file in that package is executed. This file determines what symbols (functions, classes, variables) are exposed when someone imports your package.

```python
from .count_in_list import count_in_list

__all__ = ['count_in_list']
```

This does two important things:

1 - Import and Re-export:

The line from `.count_in_list import count_in_list` imports the `count_in_list` function from the `count_in_list.py` file in the same directory (that's what the . prefix means).
By importing it at the package level, you're "lifting" this function up to be directly accessible from the package namespace.

2 - Define Public API:

The __all__ list explicitly declares which symbols should be exported when someone uses from ft_package import *.
While not strictly necessary for your specific import case, it's good practice as it clearly documents your package's public API.

## The `pyproject.toml` file
This file is used to define the package metadata and dependencies. It is a modern replacement for `setup.py` and `setup.cfg`. Here is an example of what it might look like:

```toml
[project]
name = "my_package"
version = "0.1.0"
description = "A sample Python package"
authors = [
	{ name = "Your Name", email = "test@test.com" }
]
dependencies = [
	"requests>=2.25.1",
	"numpy>=1.19.5"
]
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

## Building the package
To build the package, you can use the following command:

Install the build tools if you haven't already:

```bash
pip install build
```

Then, run the build command in the root directory of your package (where `pyproject.toml` is located):

```bash
python -m build
```

This will create a `dist` directory containing the built package files, such as `.whl` and `.tar.gz`.

## Making

