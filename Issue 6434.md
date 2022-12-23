# Issue 6434: [with patch, needs review] make a latex.py doctest more robust

Issue created by migration from https://trac.sagemath.org/ticket/6434

Original creator: jhpalmieri

Original creation time: 2009-06-27 17:35:01

Assignee: jhpalmieri

There are a pair of doctests in latex.py whose output contains the entire latex preamble, which means that any time anyone changes the preamble (for example in #6417), it screws up the doctest.  This patch replaces most of the preamble with "...".



---

Attachment


---

Comment by rlm created at 2009-07-04 00:53:11

Resolution: fixed
