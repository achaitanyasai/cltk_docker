[![Build Status](https://travis-ci.org/cltk/cltk_docker.svg?branch=master)](https://travis-ci.org/cltk/cltk_docker)

# Docker for CLTK core software
This repository contains a Docker container for the [CLTK](http://cltk.org).


# Build
First, clone this repository:
``` bash
$ git clone https://github.com/cltk/cltk_docker.git
$ cd cltk_docker
```

Build the image:
```bash
$ docker build -t cltk .
```

# Running
To run the image:
```bash
$ docker run -it cltk
```

```python
>>> from cltk.corpus.utils.importer import CorpusImporter
>>> c = CorpusImporter('latin')
>>> c.list_corpora
['latin_text_perseus', 'latin_treebank_perseus', 'latin_text_lacus_curtius', 'latin_text_latin_library', 'phi5', 'phi7', 'latin_proper_names_cltk', 'latin_models_cltk', 'latin_pos_lemmata_cltk', 'latin_treebank_index_thomisticus', 'latin_lexica_perseus', 'latin_training_set_sentence_cltk', 'latin_word2vec_cltk', 'latin_text_antique_digiliblt', 'latin_text_corpus_grammaticorum_latinorum']
```

# Data Volumes

This `Dockerfile` uses three data volumes, which you can use to persist data across runs or map a directory from the Docker host:

* `/cltk_data`
* `/nltk_data`
* `/data`

So if you use e.g. `docker volume create cltk_data`, you can then use `docker run -ti -v cltk_data:/cltk_data ctlk`, and any corpora installed will persist when you use the same volume. If your Docker host has already installed corpora locally, you could instead use e.g. `docker run -ti -v $HOME/cltk_data:/cltk_data cltk`.

# Installing Corpora

This container also comes with a helper script, `install_corpora.py`, which can be used to install all corpora:

    docker run -ti -v cltk_data:/cltk_data cltk install_corpora.py

Or corpora for specific languages:

    docker run -ti -v cltk_data:/cltk_data cltk install_corpora.py greek latin
# License
MIT. See LICENSE.txt.
