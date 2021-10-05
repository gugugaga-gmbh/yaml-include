FROM python:3

USER root

COPY . /root

RUN \
	set -xe \
	&& apt update \
	&& apt install -y \
		python3-pip \
	&& pip3 install pyyaml-include \
    && chmod +x /root/entrypoint.sh

WORKDIR /app

ENTRYPOINT ["/root/entrypoint.sh"]
