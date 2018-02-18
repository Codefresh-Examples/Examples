This example demonstrates how to build multiple versions of a Docker image in parallel.

Parallel execution is built into the [Codefresh CLI](http://cli.codefresh.io). We will leverage this feature in conjuntion with Docker's [build arguments], so run many pipelines in perallel, each building the same Dockerfile with different argument. The goal is to build Docker images for all the different versions of the Helm CLI tool (the result can be found on Docker Hub here: [https://hub.docker.com/r/codefresh/helm/](https://hub.docker.com/r/codefresh/helm/)).


## Pipeline walkthrough:

1. Codefresh docker build step, pointing to our dockerfile (see attached file), specifying the use of build argument called `HELM_VERSION`, which gets the value of a Codefresh Pipeline variable under the same name. 
2. Push the previously built image to Docker Hub, tagged with the correct version. 

## Invoking the pipeline:

We maintain a file of helm versions in the [format specified](http://cli.codefresh.io/pipelines/run-pipeline/#variable-file-var-file) by the Codefresh CLI (see attached file).

We then run the pipeline with the following command, pointing to the variables file:

```shell
codefresh run <pipeline-id> --branch master --variable-file ./helm-versions.yaml
```

(replace <pipeline-id> with the id of the pipeline)

## Pipeline variables:

name | value
---|---
HELM_VERSION|the version of helm to build
