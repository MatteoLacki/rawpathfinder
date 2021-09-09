import argparse
import pathlib
import requests


cli = argparse.ArgumentParser(description="Facade for Pipeator.")
cli.add_argument("paths",
                 nargs="+",
                 help="Files or folder names.")
cli.add_argument("--host", default="0.0.0.0",
                 help="Host in the IPv4 convention.")
cli.add_argument("--port", default=8958,
                 help="Port to listen to.")

args = cli.parse_args()

res = requests.post(f"http://{args.host}:{args.port}/find", json={"query":args.paths})