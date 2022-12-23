# Issue 1525: Bipartite graphs

Issue created by migration from https://trac.sagemath.org/ticket/1525

Original creator: rlm

Original creation time: 2007-12-15 20:28:49

Assignee: was

There is a bug in the NetworkX function is_bipartite, which sometimes gives False positives. Due to this, a few examples in graph_generators.py give possibly bad output. I have labeled them with # random, and the following URL:

https://networkx.lanl.gov/ticket/132

Once this bug is fixed, and NX updated in Sage, someone needs to go fix those docstrings.


---

Comment by rlm created at 2007-12-15 20:29:08

Changing assignee from was to rlm.


---

Comment by rlm created at 2007-12-15 20:29:08

Changing component from algebraic geometry to graph theory.


---

Comment by rlm created at 2007-12-15 20:29:08

Changing priority from major to minor.


---

Comment by rlm created at 2008-01-13 21:49:11

OK, now the NX ticket is closed, so the next step is to upgrade NX downstream.


---

Comment by rlm created at 2008-01-14 00:27:09

spkg is here:
http://sage.math.washington.edu/home/rlmill/networkx-0.36.spkg


---

Attachment

Note that now these numbers are backed up by Sloane!


---

Comment by mhansen created at 2008-01-19 00:48:28

Looks good (and works) for me.


---

Comment by mabshoff created at 2008-01-19 19:49:12

An updated spkg with the content of doc/data removed, a new SPKG.txt and a hg repo can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha0/networkx-0.36.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-19 19:53:10

Merged in Sage 2.10.1.alpha0


---

Comment by mabshoff created at 2008-01-19 19:53:10

Resolution: fixed
