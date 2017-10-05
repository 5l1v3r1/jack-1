# -*- coding: utf-8 -*-

import subprocess

from jack import readers
from jack.core import SharedResources
from jack.io.embeddings import load_embeddings
from jack.util.vocab import Vocab
import numpy as np


def test_readme():
    args = ['python3', 'jack/train_reader.py', 'with', 'config=tests/test_conf/fastqa_test.yaml']
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    for line in str(err).split('\\n'):
        if 'Iter 1' in line:
            assert 'f1: 0.065' in line
        if 'Iter 2' in line:
            assert 'f1: 0.098' in line
        if 'Iter 3' in line:
            assert 'f1: 0.098' in line
        if 'Iter 4' in line:
            assert 'f1: 0.108' in line
    # fastqa_reader = readers.fastqa_reader()
    # fastqa_reader.setup_from_file("./fastqa_reader")
