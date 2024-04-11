Welcome to tesstrain's documentation!
=====================================

Utilities for working with Tesseract >= 4 using artificial training data.

GitHub: `tesstrain_package <https://github.com/stefan6419846/tesstrain_package>`_

.. toctree::
   :maxdepth: 1

   api

About
-----

This repository contains a standalone fork of the official/upstream code at https://github.com/tesseract-ocr/tesstrain/tree/main/src to allow easier packaging for PyPI.


Installation
------------

This package requires the Tesseract training tools to be available on your system. Additionally, a supported Python version (at least 3.6) is required for running.

You can install this package from PyPI:

.. code:: bash

    python -m pip install tesstrain

Alternatively, you can use the package from source directly after installing the required dependencies.


Usage
-----

* Use the terminal interface to directly interact with the tools: ``python -m tesstrain --help``.
* Call it from your own code using the high-level interface ``tesstrain.run()``.


License
-------

This package is subject to the terms of the Apache-2.0 license.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
