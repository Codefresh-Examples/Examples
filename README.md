Welcome to Codefresh official examples repository!

Here you will find a curated collection of examples of different scenarios you can accomplish with Codefresh. These examples are also integrated in the product documentation and in the Codefresh application under the Examples section.

Each example is a directory in this repo. Inside the directory there can be any kind of file usefull for demonstrating the example. Additionally, each example directory must include 2 special files:
- `readme.md` that walks through the scenario and solution, should be writted as a tutorial.
- `cfexample.yaml` that marks this example for discovery by the Codefresh Examples section and also is a place to describe some metadata about the example.

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
body: readme.md
supportingFiles:
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
|supportingFiles|no|none|files to highlight when browsing this example in Codefresh|

## Contributions

Contributions are welcome! If you find any issue with one of the example, or want to request an example, feel free to open an issue.

