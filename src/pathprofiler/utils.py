"""
Utility functions for validating paths, file and directory operations, and path manipulations.

This module provides utility functions to validate and manipulate file system paths for the pathprofiler library.
"""

from pathlib import Path
from typing import Union, List


def _check_path(path: Union[str, Path]) -> Path:
    """
    Validates the provided path. Ensures it is either a string or a Path object,
    exists, and is a directory.

    Args:
        path (Union[str, Path]): The path to validate, either as a string or a Path object.

    Returns:
        Path: The validated Path object.

    Raises:
        TypeError: If the provided path is neither a string nor a Path object.
        ValueError: If the path does not exist or is not a directory.
    """
    path = Path(path) if isinstance(path, str) else path

    if not isinstance(path, Path):
        raise TypeError("The provided path is neither a string nor a Path object.")

    if not path.is_dir():
        raise ValueError(f"The path {path} is not a valid directory.")

    return path


def _check_file(path: Union[str, Path]) -> Path:
    """
    Validates the provided path. Ensures it is either a string or a Path object,
    exists, and is a file.

    Args:
        path (Union[str, Path]): The path to validate, either as a string or a Path object.

    Returns:
        Path: The validated Path object.

    Raises:
        TypeError: If the provided path is neither a string nor a Path object.
        ValueError: If the path does not exist or is not a file.
    """
    path = Path(path) if isinstance(path, str) else path

    if not isinstance(path, Path):
        raise TypeError("The provided path is neither a string nor a Path object.")

    if not path.is_file():
        raise ValueError(f"The path {path} is not a valid file.")

    return path


def make_dir(path: Union[str, Path]) -> None:
    """
    Ensures the directory exists, creating it if necessary.

    Args:
        path (Union[str, Path]): The directory path to ensure.

    Raises:
        TypeError: If the provided path is neither a string nor a Path object.
    """
    path = Path(path) if isinstance(path, str) else path

    if not isinstance(path, Path):
        raise TypeError("The provided path is neither a string nor a Path object.")

    path.mkdir(parents=True, exist_ok=True)


def list_files(directory: Union[str, Path]) -> List[Path]:
    """
    Lists all files in the provided directory.

    Args:
        directory (Union[str, Path]): The directory to list files from.

    Returns:
        List[Path]: A list of file paths in the directory.

    Raises:
        ValueError: If the provided path is not a directory.
    """
    directory = _check_path(directory)
    return [item for item in directory.iterdir() if item.is_file()]


def list_subdirs(directory: Union[str, Path]) -> List[Path]:
    """
    Lists all subdirectories in the provided directory.

    Args:
        directory (Union[str, Path]): The directory to list subdirectories from.

    Returns:
        List[Path]: A list of subdirectory paths in the directory.

    Raises:
        ValueError: If the provided path is not a directory.
    """
    directory = _check_path(directory)
    return [item for item in directory.iterdir() if item.is_dir()]


def get_file_size(path: Union[str, Path]) -> int:
    """
    Returns the size of the file in bytes.

    Args:
        path (Union[str, Path]): The file path to get the size of.

    Returns:
        int: The size of the file in bytes.

    Raises:
        ValueError: If the provided path is not a file.
    """
    path = _check_file(path)
    return path.stat().st_size


def get_file_modification_time(path: Union[str, Path]) -> float:
    """
    Returns the last modification time of the file.

    Args:
        path (Union[str, Path]): The file path to get the modification time of.

    Returns:
        float: The last modification time of the file in seconds since the epoch.

    Raises:
        ValueError: If the provided path is not a file.
    """
    path = _check_file(path)
    return path.stat().st_mtime


def get_file_extension(path: Union[str, Path]) -> str:
    """
    Returns the file extension.

    Args:
        path (Union[str, Path]): The file path to get the extension of.

    Returns:
        str: The file extension.

    Raises:
        ValueError: If the provided path is not a file.
    """
    path = _check_file(path)
    return path.suffix


def get_filename_without_extension(path: Union[str, Path]) -> str:
    """
    Returns the filename without the extension.

    Args:
        path (Union[str, Path]): The file path to get the filename from.

    Returns:
        str: The filename without the extension.

    Raises:
        ValueError: If the provided path is not a file.
    """
    path = _check_file(path)
    return path.stem


def read_file(path: Union[str, Path]) -> str:
    """
    Reads the content of the file and returns it as a string.

    Args:
        path (Union[str, Path]): The file path to read from.

    Returns:
        str: The content of the file.

    Raises:
        ValueError: If the provided path is not a file.
    """
    path = _check_file(path)
    with path.open("r", encoding="utf-8") as file:
        return file.read()


def write_file(path: Union[str, Path], content: str) -> None:
    """
    Writes the provided content to the file.

    Args:
        path (Union[str, Path]): The file path to write to.
        content (str): The content to write to the file.
    """
    path = Path(path) if isinstance(path, str) else path
    with path.open("w", encoding="utf-8") as file:
        file.write(content)


def delete_file(path: Union[str, Path]) -> None:
    """
    Deletes the provided file.

    Args:
        path (Union[str, Path]): The file path to delete.

    Raises:
        ValueError: If the provided path is not a file.
    """
    path = _check_file(path)
    path.unlink()
