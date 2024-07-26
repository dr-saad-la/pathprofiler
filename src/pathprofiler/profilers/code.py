"""Summary
"""

from pathlib import Path
from typing import Union, List


def is_code_file(file_path: Union[str, Path]) -> bool:
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
    return file_path.suffix in [
        ".py",
        ".js",
        ".java",
        ".cpp",
        ".c",
        ".cs",
        ".go",
        ".rs",
        ".rb",
        ".php",
        ".html",
        ".css",
    ]


def list_code_files(directory: Union[str, Path]) -> List[Path]:
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
    code_files = [file for file in directory.rglob("*") if is_code_file(file)]
    return code_files


def count_code_files(directory: Union[str, Path]) -> int:
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
    return len(list_code_files(directory))
