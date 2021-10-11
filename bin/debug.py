%load_ext autoreload
%autoreload 2
import re
import itertools
import pathlib

from rawpathfinder.path_ops import (
    iter_glob,
    iter_match_query_patterns_to_paths,
    iter_paths,
    iter_path_patterns
)


mountpoint = pathlib.Path("/mnt/ms")
general_path_pattern = "old/rawdata/gutamine/[ARCHIVIERT/*/*.d|RAW/*.d]"


list(iter_paths(mountpoint, iter_path_patterns(general_path_pattern)))



import requests
import pprint


res = requests.get(r"http://192.168.1.209:8959/search/old/rawdata/gutamine/[ARCHIVIERT/*/*.d|RAW/*.d]")

pprint.pprint(res.json())
