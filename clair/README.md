This example demonstrates how to scan an image using Clair, keep the result as annotation on the image, and also persists the scan result in S3.

Clair is an open source Docker Image securitu scanning server from CoreOS. For more information see here: https://github.com/coreos/clair/

We use the open source CLI tool for clair, called 'klar'. For more information see the [plugin page](https://github.com/codefresh-io/plugins/tree/master/incubator/clair)
and the project page: https://github.com/optiopay/klar

## Pipeline walkthrough:

1. build the Docker image
2. Scan using Clair
  - the result is saved as a file into the workspace volume
  - on success or failure, the result is saved as image annotation called  `CLAIR_SECURITY` which is a boolean flag.
4. Push the generated report into s3, and keep a link to the report as image annotation called `CLAIR_REPORT`.

## Pipeline variables:

name | value
---|---
CLAIR_ADDR|The address of the clair server
S3_BUCKETNAME|name of the s3 bucket
AWS_DEFAULT_REGION|AWS region for the s3 bucket (for example 'us-west-1')
AWS_ACCESS_KEY_ID|access key for your aws with permissions for the s3 bucket
AWS_SECRET_ACCESS_KEY|access key secret
