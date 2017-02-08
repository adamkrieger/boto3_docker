"""File System Interaction"""
import os

def __full_rel_pair__(true_root, rel_root, name):
    full_path = os.path.join(rel_root, name)
    return full_path, full_path.lstrip(true_root)

def get_files_recursively(directory):
    """Returns filepaths recursively."""
    filepaths = [
        __full_rel_pair__(directory, root, name)
        for root, _, files in os.walk(directory)
        for name in files]

    return filepaths
