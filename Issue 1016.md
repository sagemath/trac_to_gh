# Issue 1016: [with patch] add max_level argument to flatten

Issue created by migration from https://trac.sagemath.org/ticket/1016

Original creator: jason

Original creation time: 2007-10-28 02:00:13

Assignee: cwitty

Currently flatten will only flatten a list all the way.  This patch adds a max_level argument that will only flatten up to a certain depth.  See the new doctests for examples.

This patch makes flatten a little slower because of bookkeeping.  However, if that's a problem, we can split the function into code paths depending on whether max_level is passed or not.  In this case, this version of flatten should run faster than the original version since a.pop(i) is slower than a[i:i+1]=[] (at least on my computer).

I import sys to get sys.maxint.  Is that the proper way to get the maximum integer?

Also, I found in testing this patch that Python has some very low and depressing limits on the number of levels in nested lists!



---

Comment by cwitty created at 2007-10-28 18:34:51

Resolution: fixed


---

Attachment
