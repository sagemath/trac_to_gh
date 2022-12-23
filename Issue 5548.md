# Issue 5548: fix that _hnf_mod segfaults sage completely

Issue created by migration from https://trac.sagemath.org/ticket/5548

Original creator: was

Original creation time: 2009-03-17 11:53:49

Assignee: was

CC:  burcin jdemeyer


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



---

Comment by was created at 2009-03-17 11:54:23

(the problem is that the input matrix isn't square...)


---

Comment by git created at 2019-05-12 17:58:41

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by @black-stones created at 2019-05-12 18:00:20

Raised a ValueError if the matrix is not square, and made a doctest out of the sample code in the description.


---

Comment by @black-stones created at 2019-05-12 18:00:20

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2019-05-13 06:40:50

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2019-05-17 11:45:59

Resolution: fixed


---

Comment by slelievre created at 2019-05-19 23:22:50

Shouldn't the added doctest block start with a `TEST::` block header?


---

Comment by @black-stones created at 2019-05-25 15:33:49

Replying to [comment:13 slelievre]:
> Shouldn't the added doctest block start with a `TEST::` block header?

I believe that a line ending in `::` signifies the code following it is a doctest, it doesn't necessarily need to be `TEST::`. There are a few exceptions, like how `MATH::` indicates latex, but there are many doctests that say something like "This fixes trac X::", followed by a doctest.


---

Comment by slelievre created at 2019-05-27 00:08:22

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

Comment by jdemeyer created at 2019-05-27 08:21:39

I agree with Samual that there should have been a `TESTS:` block. I missed that during review. It's not a big problem though...


---

Comment by @black-stones created at 2019-05-28 23:54:27

I see, I didn't realize that the `TESTS::` header indicated a big block for all the tests, sorry for leaving that out. That being said, I did a quick search and found that there are some (very few) files that don't follow this...

* set_calculus_method() of sage-master/src/sage/manifolds/manifold.py
* from_tamari_sorting_tuple() of sage-master/src/sage/combinat/binary_tree.py ("EXEMPLES" instead of "EXAMPLES")
* __init__() of GenericGraphQuery in sage-master/src/sage/graphs/graph_database.py
* this file

My "quick search" was a bad Python script that has most likely left out other mistakes. Furthermore, some docstrings use "Examples" or "Tests" instead of the all uppercase version, and others have "Examples:" instead of "Examples::". I wasn't sure if they mattered so I didn't include them (also there were a lot of them).

This ticket is already closed, so let's not reopen it. Do you think it would be worth it to make a new ticket to search for and fix all these docstring mistakes?


---

Comment by slelievre created at 2019-05-29 00:08:18

A new ticket dedicated to fixing all missing or non-uppercase EXAMPLES and TESTS block headers would be nice.


---

Comment by jdemeyer created at 2019-05-29 08:36:29

If you want to fix those mistakes, great! Reviewing that should be trivial.
