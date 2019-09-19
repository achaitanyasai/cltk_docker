FROM python:3.7
MAINTAINER Kyle P. Johnson "kyle@kyle-p-johnson.com"
RUN apt-get update && apt-get install -y sudo
RUN pip install nose sklearn scipy pandas
RUN pip install cltk==0.1.110

ARG CLTK_UID="1000"
ARG CLTK_GID="100"

# Use the following two lines to use a local checkout of cltk instead of pip:
# ADD cltk /cltk
# RUN python setup.py install
COPY install_corpora.py /cltk/install_corpora.py
WORKDIR /cltk
RUN useradd -u $CLTK_UID --no-log-init -m -g $CLTK_GID cltk && echo 'cltk  ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/cltk
RUN mkdir /cltk_data /nltk_data /data && chown cltk:$CLTK_GID /cltk_data /nltk_data /data && chown -R cltk:$CLTK_GID /cltk
USER cltk
RUN cd ~ && ln -s /cltk_data && ln -s /nltk_data && ln -s /data
VOLUME /cltk_data /nltk_data /data
CMD ["python"]
