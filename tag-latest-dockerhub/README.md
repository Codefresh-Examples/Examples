This example demonstrates a pipeline that tags the latest version of an image in Docker Hub with the 'latest' tag. 

The original image must have been buit with Codefresh, so that it's available in Codefresh's embedded registry.

The example uses a general purpose script at: [https://gist.github.com/itaysk/c023de03fe74dd3d5db336b7f9699b6b] (https://gist.github.com/itaysk/c023de03fe74dd3d5db336b7f9699b6b) that does the following:

1. call the Docker Hub api, asking for all the tag information for the given image
2. extract tag values, disregard the 'latest' tag.
3. sort and keep the last line. 

 The latest tag is determined using the `sort` command, and is subject to it's semantics. We have found that it worked fine for [Semantic Versioning (SemVer)](https://semver.org/) tags that are widely used.

## Pipeline walkthrough

1. Run a simple script that returns that latest version. The result is being sevad in a variable that is being made availble for the next step using the `cf_export` command.
2. find the image with the determined latest version in Codefresh's embedded Docker regisrty, and push it to Docker Hub with the 'lastet' tag.

## Pipeline Variables

name|value
---|---
DOCKERHUB_REPO|name of the repository in DockerHub to operate on
DOCKERHUB_IMAGE|name of the image in the repository specifies to operate on
CFCR_REPO|name of the repository in codefresh where the matching image was built
CFCR_IMAGE| name of the image as it was built in codefresh

## Example

Assuming my image was build using Codefresh and named in Codefresh "comany-internal/theimage", and was pushed to DockerHub as "company-external/productname", the following configuration will tag the latest image:

name|value
---|---
DOCKERHUB_REPO|company-external
DOCKERHUB_IMAGE|productname
CFCR_REPO|comany-internal
CFCR_IMAGE|theimage