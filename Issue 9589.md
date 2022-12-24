# Issue 9589: Doctest failures in nfactor_enumerable_word.py on 32-bit Linux

archive/issues_009589.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  abmasse @JohnCremona jleroy @nexttime @seblabbe\n\n[Seen on 32-bit SUSE Linux by John Cremona](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/6b8cef45c9f5e56c#6b8cef45c9f5e56c):\n\n```\nsage -t -long \"devel/sage/sage/combinat/words/nfactor_enumerable_word.py\"\n**********************************************************************\nFile \"/local/jec/sage-4.5.2.alpha0/devel/sage/sage/combinat/words/nfactor_enumerable_word.py\",\nline 612:\n    sage: for i in range(10):\n        for u in w.bispecial_factors_iterator(i):\n            print i,u\nExpected:\n    0 word:\n    1 word: 1\n    1 word: 0\n    2 word: 10\n    2 word: 01\n    3 word: 101\n    3 word: 010\n    4 word: 0110\n    4 word: 1001\n    6 word: 100110\n    6 word: 011001\n    8 word: 10010110\nGot:\n    0 word:\n    1 word: 1\n    1 word: 0\n    2 word: 10\n    2 word: 01\n    3 word: 101\n    3 word: 010\n    4 word: 0110\n    4 word: 1001\n    6 word: 011001\n    6 word: 100110\n    8 word: 10010110\n**********************************************************************\nFile \"/local/jec/sage-4.5.2.alpha0/devel/sage/sage/combinat/words/nfactor_enumerable_word.py\",\nline 630:\n    sage: for u in w.bispecial_factors_iterator(): u\nExpected:\n    word:\n    word: 1\n    word: 0\n    word: 10\n    word: 01\n    word: 101\n    word: 010\n    word: 0110\n    word: 1001\n    word: 100110\n    word: 011001\n    word: 10010110\nGot:\n    word:\n    word: 1\n    word: 0\n    word: 10\n    word: 01\n    word: 101\n    word: 010\n    word: 0110\n    word: 1001\n    word: 011001\n    word: 100110\n    word: 10010110\n```\n\n[Leif Leonhardy sees the same on 32-bit Ubuntu](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/a932af7b005283b4#a932af7b005283b4).\n\nThese may be caused by #8604.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9589\n\n",
    "created_at": "2010-07-24T02:48:53Z",
    "labels": [
        "combinatorics",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Doctest failures in nfactor_enumerable_word.py on 32-bit Linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9589",
    "user": "@qed777"
}
```
Assignee: sage-combinat

CC:  abmasse @JohnCremona jleroy @nexttime @seblabbe

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

Issue created by migration from https://trac.sagemath.org/ticket/9589





---

archive/issue_comments_092725.json:
```json
{
    "body": "Hello !\n\nI'm sorry about that... this is really a bad habit to have tests that depend too much on the implementation of an iterator that may differ from one platform to another.\n\nI'll try to correct the problem tonight or at most tomorrow, if S\u00e9bastien doesn't correct it before me.",
    "created_at": "2010-07-24T03:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9589#issuecomment-92725",
    "user": "abmasse"
}
```

Hello !

I'm sorry about that... this is really a bad habit to have tests that depend too much on the implementation of an iterator that may differ from one platform to another.

I'll try to correct the problem tonight or at most tomorrow, if Sébastien doesn't correct it before me.



---

archive/issue_comments_092726.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-24T03:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9589#issuecomment-92726",
    "user": "abmasse"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_092727.json:
```json
{
    "body": "Fixes doctest failing -- depends on #8604",
    "created_at": "2010-07-24T14:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9589#issuecomment-92727",
    "user": "abmasse"
}
```

Fixes doctest failing -- depends on #8604



---

archive/issue_comments_092728.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-24T14:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9589#issuecomment-92728",
    "user": "abmasse"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092729.json:
```json
{
    "body": "Attachment [trac_9589-nfactor_doctest_fail-abm.patch](tarball://root/attachments/some-uuid/ticket9589/trac_9589-nfactor_doctest_fail-abm.patch) by abmasse created at 2010-07-24 14:06:22\n\nI uploaded a patch that should fix the problem.\n\nI tested it on sage-4.5.1 and all tests passed. Needs review.",
    "created_at": "2010-07-24T14:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9589#issuecomment-92729",
    "user": "abmasse"
}
```

Attachment [trac_9589-nfactor_doctest_fail-abm.patch](tarball://root/attachments/some-uuid/ticket9589/trac_9589-nfactor_doctest_fail-abm.patch) by abmasse created at 2010-07-24 14:06:22

I uploaded a patch that should fix the problem.

I tested it on sage-4.5.1 and all tests passed. Needs review.



---

archive/issue_comments_092730.json:
```json
{
    "body": "By the way, I'm not sure if S\u00e9bastien is available right now... But almost anyone can review this ticket, as it does not require any combinatorics on word background.",
    "created_at": "2010-07-24T14:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9589#issuecomment-92730",
    "user": "abmasse"
}
```

By the way, I'm not sure if Sébastien is available right now... But almost anyone can review this ticket, as it does not require any combinatorics on word background.



---

archive/issue_comments_092731.json:
```json
{
    "body": "\n```sh\nleif@californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ time ../../sage -t -long sage/combinat/words/\nsage -t -long \"devel/sage-9590/sage/combinat/words/alphabet.py\"\n\t [3.2 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/__init__.py\"\n\t [0.1 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/word.py\" \n\t [3.3 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/finite_word.py\"\n\t [25.3 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/all.py\"  \n\t [0.1 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/paths.py\"\n\t [12.1 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/shuffle_product.py\"\n\t [3.2 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/word_infinite_datatypes.py\"\n\t [3.3 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/suffix_trees.py\"\n\t [6.7 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/word_content.py\"\n\t [3.2 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/word_options.py\"\n\t [3.0 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/infinite_word.py\"\n\t [3.0 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/nfactor_enumerable_word.py\"\n\t [8.4 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/morphism.py\"\n\t [3.9 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/word_datatypes.pyx\"\n\t [3.2 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/abstract_word.py\"\n\t [3.6 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/utils.py\"\n\t [3.1 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/words.py\"\n\t [3.4 s]\nsage -t -long \"devel/sage-9590/sage/combinat/words/word_generators.py\"\n\t [13.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 105.0 seconds\n\nreal\t1m45.120s\nuser\t1m34.414s\nsys\t0m9.101s\nleif@californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ hg log | head -n 16\nchangeset:   14743:474058a85f79\ntag:         tip\nuser:        Alexandre Blondin Masse < alexandre.blondin.masse at gmail.com>\ndate:        Sat Jul 24 09:59:44 2010 -0400\nsummary:     #9589 Doctest failure correction in nfactor_enumerable_word.py\n\nchangeset:   14742:ebb1e171e138\nuser:        Andrey Novoseltsev <novoselt@gmail.com>\ndate:        Fri Jul 23 23:09:59 2010 -0600\nsummary:     Trac 9590: Doctest failures in cone and toric_lattice_element.\n\nchangeset:   14741:af5f40a73eda\nuser:        Mitesh Patel <qed777@gmail.com>\ndate:        Wed Jul 21 20:13:55 2010 -0700\nsummary:     4.5.2.alpha0\n\nleif@californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ \n```\n\n(This is on Ubuntu 9.04 x86.)",
    "created_at": "2010-07-24T15:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9589#issuecomment-92731",
    "user": "@nexttime"
}
```


```sh
leif@californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ time ../../sage -t -long sage/combinat/words/
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
leif@californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ hg log | head -n 16
changeset:   14743:474058a85f79
tag:         tip
user:        Alexandre Blondin Masse < alexandre.blondin.masse at gmail.com>
date:        Sat Jul 24 09:59:44 2010 -0400
summary:     #9589 Doctest failure correction in nfactor_enumerable_word.py

changeset:   14742:ebb1e171e138
user:        Andrey Novoseltsev <novoselt@gmail.com>
date:        Fri Jul 23 23:09:59 2010 -0600
summary:     Trac 9590: Doctest failures in cone and toric_lattice_element.

changeset:   14741:af5f40a73eda
user:        Mitesh Patel <qed777@gmail.com>
date:        Wed Jul 21 20:13:55 2010 -0700
summary:     4.5.2.alpha0

leif@californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ 
```

(This is on Ubuntu 9.04 x86.)



---

archive/issue_comments_092732.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-24T15:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9589#issuecomment-92732",
    "user": "@nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-26T01:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9589#issuecomment-92733",
    "user": "@dandrake"
}
```

Resolution: fixed
