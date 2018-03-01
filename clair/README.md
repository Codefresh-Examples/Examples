This example demonstrates how to scan an image using Clair, and keep the result as annotation on the image, and also persists the result in S3.

Clair is an open source Docker Image securitu scanning server. For more information see here: https://github.com/coreos/clair/

There's an open source CLI tool for clair, called 'klar' that you can use to integrate secrurity scan into your pipeline. This is wrapped in a plugin https://github.com/codefresh-io/plugins/tree/master/incubator/clair.
More info on klar: https://github.com/optiopay/klar

## Pipeline walkthrough:

1. build the Docker image
2. Scan using Clair
  - for more information see the Clair plugin: https://github.com/codefresh-io/plugins/tree/master/incubator/clair
  - the result is saved as a file into the workspace volume
  - on success or failure, the result is saved as image annotation called  `CLAIR_SECURITY` which is a boolean flag.
4. Push the generated report into s3, and link to the report as image annotation called `CLAIR_REPORT`.

## Pipeline variables:

name | value
---|---
CLAIR_ADDR|The address of the clair server
S3_BUCKETNAME|name of the s3 bucket
AWS_DEFAULT_REGION|AWS region for the s3 bucket (for example 'us-west-1')
AWS_ACCESS_KEY_ID|access key for your aws with permissions for the s3 bucket
AWS_SECRET_ACCESS_KEY|access key secret
