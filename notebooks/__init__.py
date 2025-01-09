import os


def get_parent_dir(current_dir, levels=1):
    """
    Returns the parent directory of the given directory,
    going up the specified number of levels.

    :param current_dir: The starting directory
    :param levels: The number of levels to go up
    :return: The resulting parent directory
    """
    for _ in range(levels):
        current_dir = os.path.dirname(current_dir)
    return current_dir
