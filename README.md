# tesstrain.py

Utilities for working with Tesseract >= 4 using artificial training data.

## About

This repository started as a standalone fork of the official/upstream code at https://github.com/tesseract-ocr/tesstrain/tree/main/src to allow easier packaging for PyPI.
In the meantime, it has undergone some more changes (especially modernization and code style), which are not available in the original version.

## Installation

This package requires the Tesseract training tools to be available on your system. Additionally, a supported Python version is required for running.

You can install this package from PyPI:

```bash
python -m pip install tesstrain
```

Alternatively, you may use `pip install .` to install the package from a source checkout.

## Running

* Use the terminal interface to directly interact with the tools: `python -m tesstrain --help`.
* Call it from your own code using the high-level interface `tesstrain.run()`.

## License

This package is subject to the terms of the Apache-2.0 license.
