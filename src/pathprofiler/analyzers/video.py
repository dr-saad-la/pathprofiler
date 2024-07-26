"""Summary
"""
from pathlib import Path
from typing import Union, List

def is_video_file(file_path: Union[str, Path]) -> bool:
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
    return file_path.suffix in ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv']

def list_video_files(directory: Union[str, Path]) -> List[Path]:
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
    video_files = [file for file in directory.rglob('*') if is_video_file(file)]
    return video_files

def count_video_files(directory: Union[str, Path]) -> int:
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
    return len(list_video_files(directory))