from rawpathfinder.path_ops import iter_glob, iter_match_query_patterns_to_paths


mountpoint = "/mnt/ms/"
path_patterns = [
    "*/rawdata/*/RAW/*.d", 
    "*/rawdata/*/RAW/*.raw",
    "*/rawdata/*/ARCHIVIERT/*/*.d",
    "*/rawdata/*/ARCHIVIERT/*/*.d"
]


query_patterns = ["G210115*.d"]
paths = set(iter_glob(mountpoint, path_patterns))
found_matches = dict(iter_match_query_patterns_to_paths(query_patterns, paths))

