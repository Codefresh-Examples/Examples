Welcome to Codefresh official examples repository!

Here you will find a curated collection of examples of different scenarios you can accomplish with Codefresh. These examples are also integrated in the product documentation and in the Codefresh application under the Examples section.

Each example is a directory in this repo. Inside the directory there can be any kind of files usefull for demonstrating the example. Additionally, each example directory must include 2 special files:
- `readme.md` that walks through the scenario and solution, should be writted as a tutorial.
- `codefresh.yaml` that is the pipeline yaml file/
- `cfexample.yaml` that marks this example for discovery by the Codefresh Examples section and also is a place to describe some metadata about the example.

## readme

1. start with a paragraph describing the scenario
2. specify the required pipeline variables in a table
3. walk through every step in the pipeline, explaining non-trivial commands


## cfexample.yaml

The `cfexample.yaml` file should follow the following structure:

```yaml
title: example1
description: just an example
sourceUrl: http://github.com/Codefresh-Examples/Examples/example1
baseUrl: http://github.com/Codefresh-Examples/Examples/example1
labels:
  - category1
icon: "icon.png"
body: readme.md #optioanl
codefreshfile: codefresh.yaml #optional
extraFiles:
  - codefresh.yaml
  - kubernetes-deployment.yaml
```

|field|required|default value|notes|
|---|---|---|---|
|title|yes|none||
|description|no|none||
|sourceUrl|no|current folder url|url to the source of the example|
|baseUrl|no|sourceUrl|url to prefix relative links in this yaml with|
|labels|no|none||
|icon|no|default icon|for display in Codefresh|
|body|no|./readme.md||
|codefreshfile|no|codefresh.yaml|the pipeline yaml file|
|extraFiles|no|none|files to highlight when browsing this example in Codefresh|

> Note: concatenating `baseUrl` with other relative URLs in the same yaml should result in a valid URL

## Contributions

Contributions are welcome! Feel free to submit pull requests.
If you find any issue with one of the example, or want to request an example, feel free to open an issue.