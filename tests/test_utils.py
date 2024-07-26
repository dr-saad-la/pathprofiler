import unittest
from pathlib import Path
import os
import shutil

from src.pathprofiler.utils import (
    _check_file,
    make_dir,
    list_files,
    list_subdirs,
    get_file_size,
    get_file_modification_time,
    get_file_extension,
    get_filename_without_extension,
    read_file,
    write_file,
    delete_file,
)


class TestUtils(unittest.TestCase):

    def setUp(self):
        """Create a temporary directory and files for testing."""
        self.test_dir = Path("test_dir")
        self.test_file = self.test_dir / "test_file.txt"
        self.test_subdir = self.test_dir / "subdir"

        # Create test directory and files
        self.test_dir.mkdir(exist_ok=True)
        self.test_file.write_text("Hello, world!")
        self.test_subdir.mkdir(exist_ok=True)
        (self.test_subdir / "file_in_subdir.txt").write_text("This is a test.")

    def tearDown(self):
        """Remove the temporary directory and files after testing."""
        if self.test_dir.exists() and self.test_dir.is_dir():
            shutil.rmtree(self.test_dir)

    # def tearDown(self):
    #     """Remove the temporary directory and files after testing."""
    #     for item in self.test_dir.rglob('*'):
    #         if item.is_file():
    #             item.unlink()
    #         elif item.is_dir():
    #             try:
    #                 item.rmdir()
    #             except OSError:
    #                 pass  # Ignore errors if the directory is not empty
    #     try:
    #         self.test_dir.rmdir()
    #     except OSError:
    #         pass  # Ignore errors if the directory is not empty

    def test__check_file(self):
        self.assertEqual(_check_file(self.test_file), self.test_file)
        with self.assertRaises(ValueError):
            _check_file(self.test_dir)
        with self.assertRaises(TypeError):
            _check_file(123)

    def test_make_dir(self):
        new_dir = self.test_dir / "new_dir"
        make_dir(new_dir)
        self.assertTrue(new_dir.is_dir())
        with self.assertRaises(TypeError):
            make_dir(123)

    def test_list_files(self):
        files = list_files(self.test_dir)
        self.assertIn(self.test_file, files)
        self.assertNotIn(self.test_subdir, files)
        with self.assertRaises(ValueError):
            list_files(self.test_file)

    def test_list_subdirs(self):
        subdirs = list_subdirs(self.test_dir)
        self.assertIn(self.test_subdir, subdirs)
        self.assertNotIn(self.test_file, subdirs)
        with self.assertRaises(ValueError):
            list_subdirs(self.test_file)

    def test_get_file_size(self):
        self.assertEqual(get_file_size(self.test_file), len("Hello, world!"))
        with self.assertRaises(ValueError):
            get_file_size(self.test_dir)

    def test_get_file_modification_time(self):
        self.assertTrue(isinstance(get_file_modification_time(self.test_file), float))
        with self.assertRaises(ValueError):
            get_file_modification_time(self.test_dir)

    def test_get_file_extension(self):
        self.assertEqual(get_file_extension(self.test_file), ".txt")
        with self.assertRaises(ValueError):
            get_file_extension(self.test_dir)

    def test_get_filename_without_extension(self):
        self.assertEqual(get_filename_without_extension(self.test_file), "test_file")
        with self.assertRaises(ValueError):
            get_filename_without_extension(self.test_dir)

    def test_read_file(self):
        self.assertEqual(read_file(self.test_file), "Hello, world!")
        with self.assertRaises(ValueError):
            read_file(self.test_dir)

    def test_write_file(self):
        new_content = "New content"
        write_file(self.test_file, new_content)
        self.assertEqual(read_file(self.test_file), new_content)
        new_file = self.test_dir / "new_file.txt"
        write_file(new_file, new_content)
        self.assertEqual(read_file(new_file), new_content)

    def test_delete_file(self):
        new_file = self.test_dir / "new_file.txt"
        new_file.write_text("Content to delete")
        self.assertTrue(new_file.is_file())
        delete_file(new_file)
        self.assertFalse(new_file.exists())
        with self.assertRaises(ValueError):
            delete_file(self.test_dir)


if __name__ == "__main__":
    unittest.main()
