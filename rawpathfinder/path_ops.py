import fnmatch
import glob
import itertools
import pathlib
import re
from typing import Iterator, Iterable, Dict, Tuple, Set, List



def iter_glob(mountpoint: str, patterns: List[str]) -> Iterator[pathlib.Path]:
    mountpoint = pathlib.Path(mountpoint)
    for pattern in patterns:
        yield from mountpoint.glob(pattern)


def iter_match_query_patterns_to_paths(
        query_patterns: List[str],
        paths: Set[str]
    ) -> Iterator[Tuple[str]]:
    """Iterate over matches.

    Arguments:
        query_patterns (list): Patterns of file names to match.
        paths (set): All of the locations to choose from.

    Yield:
        tuple: pattern and unix path as string.
    """
    for query_pattern in query_patterns:
        for path in paths:
            if fnmatch.fnmatch(path.name, query_pattern):
                yield str(path), query_pattern


def iter_shuffle(A: List[str], B: List[str]) -> Iterator[str]:
    min_len = min(len(A),len(B))
    for a, b in zip(A[:min_len], B[:min_len]):
        yield a
        yield b
    if len(A) > len(B):
        yield from A[len(B):]
    else:
        yield from B[len(A):]


def iter_path_patterns(
    general_path_pattern: str,
    pattern_inside_brackets: re.Pattern = re.compile(r"\[(.*?)\]"),
    pattern: re.Pattern = re.compile(r"\[.*?\]")
) -> Iterator[str]:
    groups = re.findall(pattern_inside_brackets, general_path_pattern)
    split_groups = [g.split('|') for g in groups]
    other_strings = re.split(pattern, general_path_pattern)
    for choice in itertools.product(*split_groups, repeat=1):
        yield "".join(iter_shuffle(other_strings, choice))


def iter_paths(mountpoint: pathlib.Path, path_patterns: Iterable[str]):
    for glob_path_pattern in path_patterns:
        glob_pattern = str(mountpoint/glob_path_pattern)
        yield from glob.iglob(glob_pattern)


if __name__ == '__main__':
    import pathlib
    query = [
        "M210903_008_1_1_4704.d",
        "M210903_017_1_1_4713.d",
        "M210903_026_1_1_4722.d",
        "M210903_035_1_1_4731.d",
        "M210903_044_1_1_4740.d",
        "M210903_053_1_1_4749.d",
        "M210903_063_1_1_4759.d",
        "M210903_072_1_1_4768.d",
        "M210903_081_1_1_4777.d",
        "M210903_090_1_1_4786.d",
        "M210903_099_1_1_4795.d",
        "M210903_108_1_1_4804.d"
    ]

    import fnmatch

    query_patterns = [
        "M210903*",
        "M210803*",
        "M210903_063_1_1_4759.d",
        "M210903_072_1_1_4768.d",
        "M210903_081_1_1_4777.d",
        "M210903_090_1_1_4786.d",
        "M210903_099_1_1_4795.d",
        "M210903_108_1_1_4804.d"
    ]

    mountpoint = "/mnt/ms/"
    path_patterns = ["*/rawdata/*/*/*.raw", "*/rawdata/*/*/*.d"]
    paths = set(iter_glob(mountpoint, path_patterns))



    list(iter_match(query_patterns, paths))