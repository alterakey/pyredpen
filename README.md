# PyRedPen: Sentence Checker Client #

Copyright (C) 2015 Takahiro Yoshimura <altakey@gmail.com>

This is a Python client for the RedPen.


0. HOW TO USE
=============

    $ pip install pyredpen
    $ redpen-validate examples/sampledoc-en.txt
    Found errors (4)
    $ redpen-flymake examples/sampledoc-en.txt
    examples/sampledoc-en.txt:1:0: warning: The number of words (32) exceeds the maximum of 30. [WordNumber]
    examples/sampledoc-en.txt:1:128: warning: Found repeated word "such". [DoubledWord]
    examples/sampledoc-en.txt:1:133: warning: Found repeated word "software". [DoubledWord]
	...

1. FEATURES
===========

 * Simple-ish API

2. BUGS
=======

 * Insanely hackish.
