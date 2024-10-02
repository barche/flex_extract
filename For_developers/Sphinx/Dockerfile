FROM python:3.7-slim-bullseye
# install everything
RUN apt-get update -y \
 && apt-get install -y -qq texlive texlive-latex-extra pandoc build-essential \
 && apt-get clean all
ADD requirements.txt /requirements.txt
RUN pip install --no-cache -r requirements.txt
# build the documentation with sphinx?
#ADD ./Source /doc/Source
#ADD ./Makefile /doc/Makefile
WORKDIR /doc
#RUN make html