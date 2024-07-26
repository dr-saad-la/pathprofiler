"""Summary
"""

from pathlib import Path
from typing import Union, List


def is_text_file(file_path: Union[str, Path]) -> bool:
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
    return file_path.suffix in [".txt", ".csv", ".md", ".log", ".json", ".xml"]


def list_text_files(directory: Union[str, Path]) -> List[Path]:
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
    text_files = [file for file in directory.rglob("*") if is_text_file(file)]
    return text_files


def count_text_files(directory: Union[str, Path]) -> int:
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
    return len(list_text_files(directory))
