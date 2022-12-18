FROM python:3.10.6

# install OS Modules
RUN apt update && \
	apt install telnet && \
	rm -rf /var/lib/apt/lists/*

# copy source code
RUN mkdir -p /data-copier
COPY ./src /data-copier/src
COPY requirements.txt /data-copier

# install application dependencies
RUN pip install -r /data-copier/requirements.txt