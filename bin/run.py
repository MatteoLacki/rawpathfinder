import argparse
from flask import Flask, jsonify, request
import pathlib

from rawpathfinder.path_ops import iter_glob, iter_match_query_patterns_to_paths



cli = argparse.ArgumentParser(description="Facade for Pipeator.")
cli.add_argument("--mountpoint",
                 default="/mnt/ms/",
                 help="Where is the folder mounted.")
cli.add_argument("--path_patterns",
                 nargs="+",
                 default=["*/rawdata/*/RAW/*.d", "*/rawdata/*/RAW/*.raw", "*/rawdata/*/ARCHIVIERT/*/*.d", "*/rawdata/*/ARCHIVIERT/*/*.d"],
                 help="Where is the folder mounted.")
cli.add_argument("--host", default="0.0.0.0",
                 help="Host in the IPv4 convention.")
cli.add_argument("--port", default=8958,
                 help="Port to listen to.")
cli.add_argument("--debug", action="store_true",
                 help="Run in debug mode.")
cli.add_argument("--notthreaded", action="store_false",
                 help="Run with single thread.")
args = cli.parse_args()


mountpoint = pathlib.Path(args.mountpoint)    
assert mountpoint.exists(), f"Mountpoint '{mountpoint}' does not exist."

try:
    next(iter_glob(args.mountpoint, args.path_patterns))
except StopIteration:
    raise Exception("No files/folders at the given location.")


app = Flask(__name__)

@app.route("/")
def index():
    return "rawpathfinder operational"

@app.route("/find", methods=["POST"])
def find():
    if request.is_json:
        query_patterns = request.get_json()["query"]
        if isinstance(query_patterns, str):
            query_patterns = [query_patterns]
        paths = set(iter_glob(args.mountpoint, args.path_patterns))
        found_matches = dict(iter_match_query_patterns_to_paths(query_patterns, paths))
        return found_matches

app.run(debug=args.debug,
        host=args.host,
        port=args.port,
        threaded=args.notthreaded)

