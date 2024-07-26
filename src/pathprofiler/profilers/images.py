"""Summary
"""

from pathlib import Path
from PIL import Image
from typing import Union, List


def is_image(file_path: Union[str, Path]) -> bool:
    """Summary

    Parameters
    ----------
    file_path : Union[str, Path]
        Description

    Returns
    -------
    bool
        Description
    """
    try:
        Image.open(file_path).verify()
        return True
    except (IOError, SyntaxError):
        return False


def list_images(directory: Union[str, Path]) -> List[Path]:
    """Summary

    Parameters
    ----------
    directory : Union[str, Path]
        Description

    Returns
    -------
    List[Path]
        Description
    """
    directory = Path(directory)
    images = [file for file in directory.rglob("*") if is_image(file)]
    return images


def count_images(directory: Union[str, Path]) -> int:
    """Summary

    Parameters
    ----------
    directory : Union[str, Path]
        Description

    Returns
    -------
    int
        Description
    """
    return len(list_images(directory))
