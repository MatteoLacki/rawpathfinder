import pathlib
from typing import List, Dict


def find_existing_files(
        root: str,
        patterns: List[str]
    ) -> Dict[str, str]:
    """Find all paths.

    Arguements:
        root (str): The root of the project.
        patterns (list): The list of patterns to use when finding data.

    Results:
        dict: A mapping between name and the Unix path represented as a string.
    """
    root = pathlib.Path(root)
    return {p.name: p 
            for pattern in patterns 
            for p in root.glob(pattern)}


def match_names_to_files(
        query: List[str],
        found_files: Dict[str, str]
    ) -> Dict[str, str]:
    """Match query to paths.

    Arguments:
        query (list): A list of querried file names.
        found_files (dict): A mapping between file names and their paths.

    Result:
        dict: A mapping between querried files and their unix paths. If a file is not found, empty string is returned.
    """
    return {q: str(found_files.get(q, "")) for q in query}

