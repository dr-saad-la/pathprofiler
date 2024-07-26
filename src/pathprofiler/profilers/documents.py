"""Summary
"""

from pathlib import Path
from typing import Union, List


def is_document_file(file_path: Union[str, Path]) -> bool:
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
    return file_path.suffix in [".pdf", ".docx", ".doc", ".pptx", ".xlsx", ".xls"]


def list_document_files(directory: Union[str, Path]) -> List[Path]:
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
    document_files = [file for file in directory.rglob("*") if is_document_file(file)]
    return document_files


def count_document_files(directory: Union[str, Path]) -> int:
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
    return len(list_document_files(directory))
