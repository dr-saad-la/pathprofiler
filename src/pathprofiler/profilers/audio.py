"""Summary
"""

from pathlib import Path
from typing import Union, List


def is_audio_file(file_path: Union[str, Path]) -> bool:
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
    return file_path.suffix in [".mp3", ".wav", ".aac", ".flac", ".ogg"]


def list_audio_files(directory: Union[str, Path]) -> List[Path]:
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
    audio_files = [file for file in directory.rglob("*") if is_audio_file(file)]
    return audio_files


def count_audio_files(directory: Union[str, Path]) -> int:
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
    return len(list_audio_files(directory))
