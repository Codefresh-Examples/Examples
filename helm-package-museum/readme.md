This example demonstrates how to pakcge a Helm chart, and push the packge into a Helm repository based on Chart Museum.  
Chart Museum is a Helm repository server that has an HTTP API, pluggable backends, Authentication, and more. More about it [here](https://github.com/kubernetes-helm/chartmuseum).
For the sake of this example, we assume you already have a Chart Museum server pre-installed.

If you look at the accompanied `codefresh.yaml` file, you'll see it follow 3 steps:

1. helm_package: package the chart using the `helm package` command, and save the created file name for use in upcoming step. replace `mychart` with the path to the chart directory in the repository.
2. get_repo_url: In order to avoid hard-coding the repository URL into the pipeline, we will retrieve it from the Codefresh Helm integration. In this case we assume you have pre-configured our Chart Museum repository with Codefresh as described [here](https://docs.codefresh.io/v1.0/docs/add-helm-repository). We are using the Codefresh CLI to query Codefresh for the repo URL by it's name, so replace `myreponame` with the name you gave to your repository in Codefresh.
3. helm_push: call the Chart Museum HTTP api to submit the package. Chart Museum will take care of the rest (like building the Helm repository index.yaml file).

