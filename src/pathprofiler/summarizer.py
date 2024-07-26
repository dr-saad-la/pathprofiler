"""
    Directory summarizer module.
"""

import os
from pathlib import Path
from typing import Dict, Union, Any

from numba import jit
from .images import count_images as count_image_files
from .text import count_text_files
from .code import count_code_files
from .audio import count_audio_files
from .video import count_video_files
from .documents import count_document_files
from . import _check_path


def summarize_directory(
    directory: Union[str, Path], all_files: bool = False
) -> Dict[str, Any]:
    """
    Counts the number of image files and optionally all files in each subdirectory of the given directory.
    """
    directory = _check_path(directory)
    summary = {
        "total_images": count_image_files(directory),
        "total_text_files": count_text_files(directory),
        "total_code_files": count_code_files(directory),
        "total_audio_files": count_audio_files(directory),
        "total_video_files": count_video_files(directory),
        "total_document_files": count_document_files(directory),
    }

    return summary
