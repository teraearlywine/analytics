import sys
import os


def get_root_directory():
    # Assuming the notebook is in the 'notebooks' directory, add the parent directory to sys.path
    project_root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    if project_root not in sys.path:
        sys.path.append(project_root)
    return project_root
