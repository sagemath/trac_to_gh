# Issue 9589: Doctest failures in nfactor_enumerable_word.py on 32-bit Linux

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-24 02:48:53

Assignee: sage-combinat

CC:  abmasse cremona jleroy leif slabbe

[Seen on 32-bit SUSE Linux by John Cremona](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/6b8cef45c9f5e56c#6b8cef45c9f5e56c):

```
sage -t -long "devel/sage/sage/combinat/words/nfactor_enumerable_word.py"
**********************************************************************
File "/local/jec/sage-4.5.2.alpha0/devel/sage/sage/combinat/words/nfactor_enumerable_word.py",
line 612:
    sage: for i in range(10):
        for u in w.bispecial_factors_iterator(i):
            print i,u
Expected:
    0 word:
    1 word: 1
    1 word: 0
    2 word: 10
    2 word: 01
    3 word: 101
    3 word: 010
    4 word: 0110
    4 word: 1001
    6 word: 100110
    6 word: 011001
    8 word: 10010110
Got:
    0 word:
    1 word: 1
    1 word: 0
    2 word: 10
    2 word: 01
    3 word: 101
    3 word: 010
    4 word: 0110
    4 word: 1001
    6 word: 011001
    6 word: 100110
    8 word: 10010110
**********************************************************************
File "/local/jec/sage-4.5.2.alpha0/devel/sage/sage/combinat/words/nfactor_enumerable_word.py",
line 630:
    sage: for u in w.bispecial_factors_iterator(): u
Expected:
    word:
    word: 1
    word: 0
    word: 10
    word: 01
    word: 101
    word: 010
    word: 0110
    word: 1001
    word: 100110
    word: 011001
    word: 10010110
Got:
    word:
    word: 1
    word: 0
    word: 10
    word: 01
    word: 101
    word: 010
    word: 0110
    word: 1001
    word: 011001
    word: 100110
    word: 10010110
```

[Leif Leonhardy sees the same on 32-bit Ubuntu](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/a932af7b005283b4#a932af7b005283b4).

These may be caused by #8604.


---

Comment by abmasse created at 2010-07-24 03:01:24

Hello !

I'm sorry about that... this is really a bad habit to have tests that depend too much on the implementation of an iterator that may differ from one platform to another.

I'll try to correct the problem tonight or at most tomorrow, if Sébastien doesn't correct it before me.


---

Comment by abmasse created at 2010-07-24 03:01:24

Changing status from new to needs_work.


---

Comment by abmasse created at 2010-07-24 14:03:23

Fixes doctest failing -- depends on #8604


---

Comment by abmasse created at 2010-07-24 14:06:22

Changing status from needs_work to needs_review.


---

Attachment

I uploaded a patch that should fix the problem.

I tested it on sage-4.5.1 and all tests passed. Needs review.


---

Comment by abmasse created at 2010-07-24 14:09:11

By the way, I'm not sure if Sébastien is available right now... But almost anyone can review this ticket, as it does not require any combinatorics on word background.


---

Comment by leif created at 2010-07-24 15:28:36


```sh
leif`@`californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ time ../../sage -t -long sage/combinat/words/
sage -t -long "devel/sage-9590/sage/combinat/words/alphabet.py"
	 [3.2 s]
sage -t -long "devel/sage-9590/sage/combinat/words/__init__.py"
	 [0.1 s]
sage -t -long "devel/sage-9590/sage/combinat/words/word.py" 
	 [3.3 s]
sage -t -long "devel/sage-9590/sage/combinat/words/finite_word.py"
	 [25.3 s]
sage -t -long "devel/sage-9590/sage/combinat/words/all.py"  
	 [0.1 s]
sage -t -long "devel/sage-9590/sage/combinat/words/paths.py"
	 [12.1 s]
sage -t -long "devel/sage-9590/sage/combinat/words/shuffle_product.py"
	 [3.2 s]
sage -t -long "devel/sage-9590/sage/combinat/words/word_infinite_datatypes.py"
	 [3.3 s]
sage -t -long "devel/sage-9590/sage/combinat/words/suffix_trees.py"
	 [6.7 s]
sage -t -long "devel/sage-9590/sage/combinat/words/word_content.py"
	 [3.2 s]
sage -t -long "devel/sage-9590/sage/combinat/words/word_options.py"
	 [3.0 s]
sage -t -long "devel/sage-9590/sage/combinat/words/infinite_word.py"
	 [3.0 s]
sage -t -long "devel/sage-9590/sage/combinat/words/nfactor_enumerable_word.py"
	 [8.4 s]
sage -t -long "devel/sage-9590/sage/combinat/words/morphism.py"
	 [3.9 s]
sage -t -long "devel/sage-9590/sage/combinat/words/word_datatypes.pyx"
	 [3.2 s]
sage -t -long "devel/sage-9590/sage/combinat/words/abstract_word.py"
	 [3.6 s]
sage -t -long "devel/sage-9590/sage/combinat/words/utils.py"
	 [3.1 s]
sage -t -long "devel/sage-9590/sage/combinat/words/words.py"
	 [3.4 s]
sage -t -long "devel/sage-9590/sage/combinat/words/word_generators.py"
	 [13.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 105.0 seconds

real	1m45.120s
user	1m34.414s
sys	0m9.101s
leif`@`californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ hg log | head -n 16
changeset:   14743:474058a85f79
tag:         tip
user:        Alexandre Blondin Masse < alexandre.blondin.masse at gmail.com>
date:        Sat Jul 24 09:59:44 2010 -0400
summary:     #9589 Doctest failure correction in nfactor_enumerable_word.py

changeset:   14742:ebb1e171e138
user:        Andrey Novoseltsev <novoselt`@`gmail.com>
date:        Fri Jul 23 23:09:59 2010 -0600
summary:     Trac 9590: Doctest failures in cone and toric_lattice_element.

changeset:   14741:af5f40a73eda
user:        Mitesh Patel <qed777`@`gmail.com>
date:        Wed Jul 21 20:13:55 2010 -0700
summary:     4.5.2.alpha0

leif`@`californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ 
```

(This is on Ubuntu 9.04 x86.)


---

Comment by leif created at 2010-07-24 15:28:36

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-26 01:36:30

Resolution: fixed
