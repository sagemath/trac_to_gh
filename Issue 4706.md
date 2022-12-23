# Issue 4706: fix race condition between doctest creation and running

Issue created by migration from https://trac.sagemath.org/ticket/4706

Original creator: mabshoff

Original creation time: 2008-12-05 01:37:01

Assignee: mabshoff

With high -tp numbers (i.e. 16) on sage.math one will see similar issues to the one below:

```
sage -t -long devel/sage/sage/libs/symmetrica/symmetrica.pyx
  File "/scratch/mabshoff/release-cycle/sage-3.2.alpha0/tmp/.doctest_symmetrica.py", line 29
    >>> test_integer(Integer(1))###line 539:_sage_    >>> test_integer(1)
    ^
IndentationError: unexpected indent
```


This is likely a race condition between creating the file running the doctest. The issue is not specific to -tp. 

A potential solution might be to create all .doctest_$FOO files and then start running them. This might also fix the problem with 

```
sage -t -long devel/sage/sage/symbolic/constants.pyx
	 [0.1 s]
```

in Sage 3.2.1+ which is caused by no doctests being executed since (a) either there are no doctests in that file or (b) we are running optional doctests only.

Cheers,

Michael


---

Attachment

I think this is an old ticket which can be closed and has been fixed in the mean time. At least during the parralel builds I did (and I did quite a few this sage days already) I never saw this message.


---

Comment by mderickx created at 2011-08-23 21:09:08

Changing status from new to needs_review.


---

Comment by mhansen created at 2011-12-17 20:46:58

Resolution: invalid


---

Comment by mhansen created at 2011-12-17 20:46:58

I tihnk this can be closed as well.
