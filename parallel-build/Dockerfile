FROM codefresh/cfbase

ARG HELM_VERSION

WORKDIR /tmp

RUN curl -L "https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz" -o helm.tar.gz \
    && tar -zxvf helm.tar.gz \
    && mv ./linux-amd64/helm /usr/local/bin/helm \
    && rm -rf /tmp/*

WORKDIR ~

ENTRYPOINT ["helm"]
