# Docker script for cltk

This repository contains **Dockerfile** for [cltk](http://cltk.org).


### Build
To build an image with docker:
- Clone the repository on your machine:
``` bash
$ git clone https://github.com/achaitanyasai/cltk_docker.git
$ cd cltk_docker
```
- Change proxy settings in <code>Dockerfile</code> if you are behind proxy server.
- Build image using:
```bash
$ sudo docker build -t cltk .
```
Wait for some time and once it's done, it should create an image with name cltk which contains cltk and it's corpora installed in it.

### Running
- Now run the image using:
```bash
$ sudo docker run -it cltk bash
```
Once it's done, it should open a bash shell as a root user. Now you can check whether cltk and it's corpora are installed or not using:
- Check python version:
```bash
$ python --version #Should display 3.5.1
Python 3.5.1
```
- Check whether cltk and it's corpora is installed or not:
```python
>>> import cltk
>>> from cltk.corpus.utils.importer import CorpusImporter
>>> corpus_importer = CorpusImporter('greek')  # e.g., or CorpusImporter('latin')
>>> corpus_importer.list_corpora
['greek_software_tlgu', 'greek_text_perseus', 'phi7', 'tlg', 'greek_proper_names_cltk', 'greek_models_cltk', 'greek_treebank_perseus', 'greek_lexica_perseus', 'greek_training_set_sentence_cltk', 'greek_word2vec_cltk']
```