[![Build Status](https://travis-ci.org/cltk/cltk_docker.svg?branch=master)](https://travis-ci.org/cltk/cltk_docker)

# Docker for CLTK core software
This repository contains a Docker container for the [cltk](http://cltk.org).


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
$ docker run -it cltk bash
```

This will enter you into the shell as a root user. To check installation:

```python
>>> from cltk.corpus.utils.importer import CorpusImporter
>>> c = CorpusImporter('latin')
>>> c.list_corpora
['latin_text_perseus', 'latin_treebank_perseus', 'latin_text_lacus_curtius', 'latin_text_latin_library', 'phi5', 'phi7', 'latin_proper_names_cltk', 'latin_models_cltk', 'latin_pos_lemmata_cltk', 'latin_treebank_index_thomisticus', 'latin_lexica_perseus', 'latin_training_set_sentence_cltk', 'latin_word2vec_cltk', 'latin_text_antique_digiliblt', 'latin_text_corpus_grammaticorum_latinorum']
```
