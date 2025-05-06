FROM  ubuntu:latest

WORKDIR /app

RUN apt update && apt install -y git curl

RUN git clone https://github.com/Ararabots-UFMS/ssl-gui.git

RUN cd ssl-gui

RUN apt install -y npm

RUN cd /app/ssl-gui && npm install

RUN npm install -g n
RUN n latest
RUN n prune
RUN PATH="$PATH"

RUN rm -rf /var/lib/apt/lists/*