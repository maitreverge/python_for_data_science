## The `__init__.py` file

This kind of file tells python that the directory should be treated as a package. It can be empty, or it can contain initialization code for the package.

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

```bash
python3 -m build
```
This will create a `dist` directory containing the built package files, such as `.whl` and `.tar.gz`.

