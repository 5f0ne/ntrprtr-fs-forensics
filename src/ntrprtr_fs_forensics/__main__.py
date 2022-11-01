import os
import sys
from shutil import copytree, ignore_patterns

import argparse

from ntrprtr_fs_forensics.Controller import Controller

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", "-m", choices=["copy"], required=True, help="The tool to use")
    # config
    parser.add_argument("--path", "-p", type=str, default="", help="Path for local copy of ntrprtr configuration files")
    args = parser.parse_args()

    c = Controller()
    c.printHeader()

    if(args.mode == "copy"):
        sourceDir = os.path.dirname(__file__)
        targetDir = os.path.join(args.path, "ntrprtr-fsf-config")

        if(not os.path.isdir(targetDir)):
            os.mkdir(targetDir)
            copytree(os.path.join(sourceDir, "ext"), os.path.join(targetDir, "ext"), ignore=ignore_patterns('__pycache__', '*.py'))
            copytree(os.path.join(sourceDir, "fat"), os.path.join(targetDir, "fat"), ignore=ignore_patterns('__pycache__', '*.py'))
            copytree(os.path.join(sourceDir, "ntfs"), os.path.join(targetDir, "ntfs"), ignore=ignore_patterns('__pycache__', '*.py'))
            copytree(os.path.join(sourceDir, "gpt"), os.path.join(targetDir, "gpt"), ignore=ignore_patterns('__pycache__', '*.py'))
            copytree(os.path.join(sourceDir, "mbr"), os.path.join(targetDir, "mbr"), ignore=ignore_patterns('__pycache__', '*.py'))
            print("")
            print("ntrprtr file system forensics configurations copied successfully: " + targetDir)
            print("")
            c.printExecutionTime()
        else:
            print("")
            print("Directory already exists: " + targetDir)
            print("")
            c.printExecutionTime()
            exit()

    


if __name__ == "__main__":
    sys.exit(main())
