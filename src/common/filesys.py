"""File System Interaction"""
import os

def __full_rel_pair__(root, this_file_root, this_filename):
    full_path = os.path.join(this_file_root, this_filename)
    relative_path = full_path[len(root):]
    return full_path, relative_path

def get_files_recursively(directory):
    """Returns filepaths recursively."""
    filepaths = [
        __full_rel_pair__(directory, each_directory, each_filename)
        for each_directory, _, files in os.walk(directory)
        for each_filename in files]

    return filepaths
