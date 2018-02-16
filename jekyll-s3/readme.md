This example demonstrates how to generate a static website using Jekyll, and push the static files to S3 for hosting.

[Jekyll](http://jekyllrb.com) is a popolar static site generator that is backed by GitHub, and is mostly used for blog sites, and documentation sites. We at Codefresh use Jekyll for our documentaion site - [http://docs.codefresh.io](http://docs.codefresh.io).

Pipeline walkthrough:
1. build the site with jekyll
  - change permissions in order to allow jekyll to write the site and bundler to override Gemfile.lock
  - set the correct uel and baseurl in the `_config.yml`
  - build the site into the folder `_site`
2. push to s3
  - sync everything in `_site` into the bucket

Pipeline variables:

name | value
---|---
JEKYLL_URL|URL where you plan to host the site
JEKYLL_BASEURL|path relative to the baseurl where the site content will be
S3_BUCKETNAME|name of the bucket
AWS_DEFAULT_REGION|AWS region for the bucket (for example 'us-west-1')
AWS_ACCESS_KEY_ID|access key for your aws with permissions for the s3 bucket
AWS_SECRET_ACCESS_KEY|access key secret
