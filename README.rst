=============
Path profiler
=============


.. image:: https://img.shields.io/pypi/v/pathprofiler.svg
        :target: https://pypi.python.org/pypi/pathprofiler

.. image:: https://img.shields.io/travis/dr-saad-la/pathprofiler.svg
        :target: https://travis-ci.com/dr-saad-la/pathprofiler

.. image:: https://readthedocs.org/projects/pathprofiler/badge/?version=latest
        :target: https://pathprofiler.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/dr-saad-la/pathprofiler/shield.svg
     :target: https://pyup.io/repos/github/dr-saad-la/pathprofiler/
     :alt: Updates



`pathprofiler` is a Python package designed to analyze and summarize the contents of directories. It provides utilities for validating paths, performing file and directory operations, extracting metadata, and categorizing files by type.

Features
--------

- **Path Validation**: Ensure paths exist and are of the correct type (file or directory).
- **File Operations**: Read, write, and delete files.
- **Directory Operations**: Create, list, and delete directories.
- **Metadata Extraction**: Get file size, modification time, and extensions.
- **Categorization**: Identify and count different file types within directories.

Installation
------------

You can install `pathprofiler` using `pip`:

.. code-block:: bash

    pip install pathprofiler

Usage
-----

Basic Example
^^^^^^^^^^^^^

.. code-block:: python

    from pathprofiler import utils

    # Validate a directory path
    directory = utils._check_path('/path/to/directory')

    # List all files in a directory
    files = utils.list_files(directory)
    print(f'Files: {files}')

    # List all subdirectories
    subdirs = utils.list_subdirectories(directory)
    print(f'Subdirectories: {subdirs}')

    # Get file size
    file_size = utils.get_file_size('/path/to/file.txt')
    print(f'File size: {file_size} bytes')

    # Read file content
    content = utils.read_file('/path/to/file.txt')
    print(f'File content: {content}')

    # Write to a file
    utils.write_file('/path/to/newfile.txt', 'Hello, World!')

    # Delete a file
    utils.delete_file('/path/to/newfile.txt')

Advanced Usage
^^^^^^^^^^^^^^

Create a Directory
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    utils.create_directory('/path/to/new_directory')

Get File Metadata
~~~~~~~~~~~~~~~~~

.. code-block:: python

    file_path = '/path/to/file.txt'

    # Get file size
    size = utils.get_file_size(file_path)
    print(f'Size: {size} bytes')

    # Get file modification time
    mod_time = utils.get_file_modification_time(file_path)
    print(f'Modification time: {mod_time}')

    # Get file extension
    extension = utils.get_file_extension(file_path)
    print(f'Extension: {extension}')

    # Get filename without extension
    filename = utils.get_filename_without_extension(file_path)
    print(f'Filename: {filename}')

Contributing
------------

Contributions are welcome! Please read the `CONTRIBUTING`_ guidelines before starting.

License
-------

This project is licensed under the MIT License. See the `LICENSE`_ file for details.

Contact
-------

If you have any questions or suggestions, please open an issue on GitHub.

Authors
-------

- `Dr Saad Laouadi <https://github.com/dr-saad-la>`_

Acknowledgements
----------------

- `pylint <https://www.pylint.org/>`_
- `black <https://black.readthedocs.io/en/stable/>`_
- `flake8 <https://flake8.pycqa.org/en/latest/>`_
- `pycodestyle <https://pycodestyle.pycqa.org/en/latest/>`_
- `pathlib <https://docs.python.org/3/library/pathlib.html>`_

Example Projects
----------------

Check out the `examples`_ directory for more usage examples.

Documentation
-------------

Detailed documentation is available in the `docs`_ directory or online at `Read the Docs <https://pathprofiler.readthedocs.io>`_.

.. _CONTRIBUTING: CONTRIBUTING.rst
.. _LICENSE: LICENSE
.. _examples: examples/
.. _docs: docs/


Python library that profile a directory and returns a description of the content of a directory.


* Free software: MIT license
* Documentation: https://pathprofiler.readthedocs.io.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
