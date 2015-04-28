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
    $ redpen-flymake examples/sampledoc-ja.txt
    examples/sampledoc-ja.txt:1:0: warning: The length of the sentence (101) exceeds the maximum of 100. [SentenceLength]
    examples/sampledoc-ja.txt:1:83: warning: Found invalid symbol "，". [InvalidSymbol]
    examples/sampledoc-ja.txt:1:49: warning: Found repeated word "分散". [DoubledWord]
    examples/sampledoc-ja.txt:1:51: warning: Found repeated word "ソフトウェア". [DoubledWord]
    ...

1. FEATURES
===========

 * Python 3 safe
 * Simple-ish API

2. BUGS
=======

 * Requires Python 3.
 * Blindly assuming input and output in UTF-8.
 * Insanely hackish.

3. LICENSE
==========

The MIT license.  Please refer to the LICENSE.txt.
