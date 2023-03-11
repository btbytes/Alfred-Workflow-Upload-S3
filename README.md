# Alfred Workflow: Upload Image to AWS S3


Forked from [tonyxu-io/Alfred-Workflow-Upload-S3](https://github.com/tonyxu-io/Alfred-Workflow-Upload-S3) and modified to fit my preferences, primarily:

* use [Cloudflare R2](), an S3 API compatible storage solution
* use [Homebrew](https://brew.sh) installed `pngpaste` instead of using a binary


This workflow helps you upload image in your clipboard or local disk to S3 and put the public url of the image to your clipboard. This workflow is especially helpful if you are a markdown fan and you can easily get public url and use it in markdown document.


## Overview

This workflow is written in Python3. And used Boto3 as AWS client to upload image.


## Usage

Config Environment Variables:

- access_key: S3 access key
- secret_key: S3 access secret
- bucket_name: S3 bucket name. e.g. `my-bucket-name`
- bucket_uri: S3 bucket uri without trailing slash. e.g. `https://s3-us-west-1.amazonaws.com/my-bucket-name`

Upload image from clipboard:


```bash
upload
```

Upload image from local:

```bash
upload TYPE-FILENAME-HERE
```

## Tutorials

Check out [Tony's blogpost](https://tonyxu.io/posts/create-alfred-workflow-for-uploading-screenshot-to-s3/
) for the original tutorial.

