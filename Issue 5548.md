# Issue 5548: fix that _hnf_mod segfaults sage completely

archive/issues_005548.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @burcin @jdemeyer\n\n\n```\nteragon:algebras wstein$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: a = random_matrix(ZZ,16,4)\nsage: a._hnf_mod(100)\n| Sage Version 3.4, Release Date: 2009-03-11                         |\n| Type notebook() for the GUI, and license() for information.        |\n\n------------------------------------------------------------\nUnhandled SIGFPE: An unhandled floating point exception occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5548\n\n",
    "created_at": "2009-03-17T11:53:49Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.8",
    "title": "fix that _hnf_mod segfaults sage completely",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5548",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @burcin @jdemeyer


```
teragon:algebras wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = random_matrix(ZZ,16,4)
sage: a._hnf_mod(100)
| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


Issue created by migration from https://trac.sagemath.org/ticket/5548





---

archive/issue_comments_043069.json:
```json
{
    "body": "(the problem is that the input matrix isn't square...)",
    "created_at": "2009-03-17T11:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43069",
    "user": "https://github.com/williamstein"
}
```

(the problem is that the input matrix isn't square...)



---

archive/issue_comments_043070.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2019-05-12T17:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43070",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_043071.json:
```json
{
    "body": "Raised a ValueError if the matrix is not square, and made a doctest out of the sample code in the description.",
    "created_at": "2019-05-12T18:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43071",
    "user": "https://github.com/black-stones"
}
```

Raised a ValueError if the matrix is not square, and made a doctest out of the sample code in the description.



---

archive/issue_comments_043072.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2019-05-12T18:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43072",
    "user": "https://github.com/black-stones"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_043073.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2019-05-13T06:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43073",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_043074.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2019-05-17T11:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43074",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_005793.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2019-05-17T11:45:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5548#event-5793"
}
```



---

archive/issue_comments_043075.json:
```json
{
    "body": "Shouldn't the added doctest block start with a `TEST::` block header?",
    "created_at": "2019-05-19T23:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43075",
    "user": "https://github.com/slel"
}
```

Shouldn't the added doctest block start with a `TEST::` block header?



---

archive/issue_comments_043076.json:
```json
{
    "body": "Replying to [comment:13 slelievre]:\n> Shouldn't the added doctest block start with a `TEST::` block header?\n\nI believe that a line ending in `::` signifies the code following it is a doctest, it doesn't necessarily need to be `TEST::`. There are a few exceptions, like how `MATH::` indicates latex, but there are many doctests that say something like \"This fixes trac X::\", followed by a doctest.",
    "created_at": "2019-05-25T15:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43076",
    "user": "https://github.com/black-stones"
}
```

Replying to [comment:13 slelievre]:
> Shouldn't the added doctest block start with a `TEST::` block header?

I believe that a line ending in `::` signifies the code following it is a doctest, it doesn't necessarily need to be `TEST::`. There are a few exceptions, like how `MATH::` indicates latex, but there are many doctests that say something like "This fixes trac X::", followed by a doctest.



---

archive/issue_comments_043077.json:
```json
{
    "body": "Although the code does get tested even without a TEST header, my understanding of the\n[documentation strings section](http://doc.sagemath.org/html/en/developer/coding_basics.html#documentation-strings)\nof Sage's [coding basics](http://doc.sagemath.org/html/en/developer/coding_basics.html)\nis that testable examples in docstrings are usually placed inside \"TEST\" or \"TESTS\"\nor \"EXAMPLE\" or \"EXAMPLES\" blocks, which can go either\n\n```\nTESTS::\n\n    sage: 1 + 1\n    2\n    sage: 1 + 2\n    3\n```\n\nor\n\n```\nTESTS:\n\nWe test that one plus one is two::\n\n    sage: 1 + 1\n    2\n\nWe test that one plus two is three::\n\n    sage: 1 + 2\n    3\n```\n\n(or similarly for TEST, EXAMPLE, EXAMPLES).\n\nIn addition, TEST and TESTS sections being meant more for developers\nthan users, they get removed when building the documentation, unless\none sets a dedicate environment variable:\n\n```\nSAGE_DOCBUILD_OPTS=\"--include-tests-blocks\"\n```\n\nto keep them in.\n\nAre there any doctests in docstrings elsewhere in the Sage sources that are\nnot introduced by an EXAMPLE, EXAMPLES, TEST or TESTS header?",
    "created_at": "2019-05-27T00:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43077",
    "user": "https://github.com/slel"
}
```

Although the code does get tested even without a TEST header, my understanding of the
[documentation strings section](http://doc.sagemath.org/html/en/developer/coding_basics.html#documentation-strings)
of Sage's [coding basics](http://doc.sagemath.org/html/en/developer/coding_basics.html)
is that testable examples in docstrings are usually placed inside "TEST" or "TESTS"
or "EXAMPLE" or "EXAMPLES" blocks, which can go either

```
TESTS::

    sage: 1 + 1
    2
    sage: 1 + 2
    3
```

or

```
TESTS:

We test that one plus one is two::

    sage: 1 + 1
    2

We test that one plus two is three::

    sage: 1 + 2
    3
```

(or similarly for TEST, EXAMPLE, EXAMPLES).

In addition, TEST and TESTS sections being meant more for developers
than users, they get removed when building the documentation, unless
one sets a dedicate environment variable:

```
SAGE_DOCBUILD_OPTS="--include-tests-blocks"
```

to keep them in.

Are there any doctests in docstrings elsewhere in the Sage sources that are
not introduced by an EXAMPLE, EXAMPLES, TEST or TESTS header?



---

archive/issue_comments_043078.json:
```json
{
    "body": "I agree with Samual that there should have been a `TESTS:` block. I missed that during review. It's not a big problem though...",
    "created_at": "2019-05-27T08:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43078",
    "user": "https://github.com/jdemeyer"
}
```

I agree with Samual that there should have been a `TESTS:` block. I missed that during review. It's not a big problem though...



---

archive/issue_comments_043079.json:
```json
{
    "body": "I see, I didn't realize that the `TESTS::` header indicated a big block for all the tests, sorry for leaving that out. That being said, I did a quick search and found that there are some (very few) files that don't follow this...\n\n* set_calculus_method() of sage-master/src/sage/manifolds/manifold.py\n* from_tamari_sorting_tuple() of sage-master/src/sage/combinat/binary_tree.py (\"EXEMPLES\" instead of \"EXAMPLES\")\n* __init__() of GenericGraphQuery in sage-master/src/sage/graphs/graph_database.py\n* this file\n\nMy \"quick search\" was a bad Python script that has most likely left out other mistakes. Furthermore, some docstrings use \"Examples\" or \"Tests\" instead of the all uppercase version, and others have \"Examples:\" instead of \"Examples::\". I wasn't sure if they mattered so I didn't include them (also there were a lot of them).\n\nThis ticket is already closed, so let's not reopen it. Do you think it would be worth it to make a new ticket to search for and fix all these docstring mistakes?",
    "created_at": "2019-05-28T23:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43079",
    "user": "https://github.com/black-stones"
}
```

I see, I didn't realize that the `TESTS::` header indicated a big block for all the tests, sorry for leaving that out. That being said, I did a quick search and found that there are some (very few) files that don't follow this...

* set_calculus_method() of sage-master/src/sage/manifolds/manifold.py
* from_tamari_sorting_tuple() of sage-master/src/sage/combinat/binary_tree.py ("EXEMPLES" instead of "EXAMPLES")
* __init__() of GenericGraphQuery in sage-master/src/sage/graphs/graph_database.py
* this file

My "quick search" was a bad Python script that has most likely left out other mistakes. Furthermore, some docstrings use "Examples" or "Tests" instead of the all uppercase version, and others have "Examples:" instead of "Examples::". I wasn't sure if they mattered so I didn't include them (also there were a lot of them).

This ticket is already closed, so let's not reopen it. Do you think it would be worth it to make a new ticket to search for and fix all these docstring mistakes?



---

archive/issue_comments_043080.json:
```json
{
    "body": "A new ticket dedicated to fixing all missing or non-uppercase EXAMPLES and TESTS block headers would be nice.",
    "created_at": "2019-05-29T00:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43080",
    "user": "https://github.com/slel"
}
```

A new ticket dedicated to fixing all missing or non-uppercase EXAMPLES and TESTS block headers would be nice.



---

archive/issue_comments_043081.json:
```json
{
    "body": "If you want to fix those mistakes, great! Reviewing that should be trivial.",
    "created_at": "2019-05-29T08:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5548#issuecomment-43081",
    "user": "https://github.com/jdemeyer"
}
```

If you want to fix those mistakes, great! Reviewing that should be trivial.
