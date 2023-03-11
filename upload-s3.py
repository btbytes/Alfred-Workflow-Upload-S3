#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import os
import sys
import atexit
from subprocess import call
from workflow import Workflow


def capture():
    file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S.png")
    if sys.argv[1] != "":
        # Image path is expected if additional argument
        # is found and will be verified by Alfred file filter
        file_path = sys.argv[1]
    else:
        # Get image from clipboard
        file_path = os.path.join("/tmp", file_name)
        atexit.register(
            lambda x: os.remove(x) if os.path.exists(x) else None, file_path
        )
        save = call(["./pngpaste", file_path])
        if save == 1:
            # Image not found in clipboard
            print("No image found in clipboard")
            sys.exit()
    return file_path, file_name


def main(wf):
    import boto3

    fpath, fname = capture()
    bucket = os.getenv("bucket_name")
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("access_key"),
        aws_secret_access_key=os.getenv("secret_key"),
    )
    s3.upload_file(fpath, bucket, fname, ExtraArgs={"ContentType": "image/png"})
    output = "%s/%s" % (os.getenv("bucket_uri"), fname)
    print(output, end="")


if __name__ == "__main__":
    wf = Workflow(libraries=["./lib"])
    sys.exit(wf.run(main))
