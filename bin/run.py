import argparse
from flask import Flask, jsonify, request
import pathlib

from rawpathfinder.path_ops import find_existing_files, match_names_to_files



cli = argparse.ArgumentParser(description="Facade for Pipeator.")
cli.add_argument("--mountpoint",
                 default="/mnt/ms/",
                 help="Where is the folder mounted.")
cli.add_argument("--patterns",
                 nargs="+",
                 default=["*/rawdata/*/*/*.d"],
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

existing_files = find_existing_files(mountpoint, args.patterns)
assert existing_files, "No folders/files are found."


app = Flask(__name__)

@app.route("/")
def index():
    return "rawpathfinder operational"

@app.route("/find", methods=["POST"])
def find():
    if request.is_json:
        query = request.get_json()["query"]
        exisiting_files = find_existing_files(mountpoint, args.patterns)
        found_matches = match_names_to_files(query, exisiting_files)
        if args.debug:
            print(found_matches)
        return found_matches

app.run(debug=args.debug,
        host=args.host,
        port=args.port,
        threaded=args.notthreaded)

