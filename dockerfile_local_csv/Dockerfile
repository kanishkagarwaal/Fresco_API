FROM alpine:3.7

RUN mkdir /Fresco_API

RUN apk update \
  && apk add --no-cache python3 \
  && apk add libc-dev \
  && apk --no-cache --update-cache add gcc gfortran build-base python3-dev wget freetype-dev libpng-dev openblas-dev \	
  && apk add --no-cache subversion \
  && apk add curl bash binutils tar git \
  && python3 -m ensurepip \
  && git clone https://github.com/kanishkagarwaal/Fresco_API /Fresco_API \
  && pip3 install -r /Fresco_API/requirements.txt 	

VOLUME ["/Fresco_API"]

CMD cd /Fresco_API && git pull && python3 /Fresco_API/TestCassandraDb.py

