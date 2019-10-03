FROM ubuntu:16.04

MAINTAINER DIDARUL ""

RUN apt -y update &&\
    apt -y install python3 python3-pip &&\
    apt -y install libgtk2.0-dev 

RUN python3 -m pip install --upgrade pip

RUN apt-get install -y --fix-missing \
	build-essential \
	cmake \
	gfortran \
	wget \
	curl \
	graphicsmagick \
	libgraphicsmagick1-dev \
	libatlas-dev \
	libavcodec-dev \
	libavformat-dev \
	libgtk2.0-dev \
	libjpeg-dev \
	liblapack-dev \
	libswscale-dev \
	pkg-config \
	software-properties-common \
	zip

# Google tesseract
RUN add-apt-repository ppa:alex-p/tesseract-ocr &&\
	apt-get update &&\
	apt install -y tesseract-ocr &&\
	apt install -y libtesseract-dev


ADD ./python_requirements.txt /
RUN python3 -m pip install -r python_requirements.txt


# ADD ../app /
ENTRYPOINT ["bash","/app/start_flask.sh"]
