# Issue 3737: backslash in verbatim environment in tut.tex breaks doctest

Issue created by migration from https://trac.sagemath.org/ticket/3737

Original creator: jhpalmieri

Original creation time: 2008-07-29 03:47:59

Assignee: failure

Keywords: latex, verbatim, backslash

I would like to include lines like these in tut.tex:

```
\begin{verbatim}
sage: A = Matrix([[1,2,3],[3,2,1],[1,1,1]])
sage: Y = vector([0,-4,-1])
sage: A \ Y
(-2, 1, 0)
\end{verbatim}
```

When I include these, doctesting fails on tut.tex, giving an error about something 500 lines away, and giving an error after half a second, whereas if these lines are removed, doctesting finishes successfully in about 30 seconds. 

I would guess that the problem is the backslash in the verbatim environment.




---

Comment by mhansen created at 2008-09-19 07:10:47

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-19 07:10:47

Changing assignee from failure to mhansen.


---

Comment by jhpalmieri created at 2008-09-19 14:52:22

This might become moot with the Sphinx versions of the documentation -- I noticed that the new version of the tutorial at [http://sage.math.washington.edu/home/mhansen/doc-sphinx/](http://sage.math.washington.edu/home/mhansen/doc-sphinx/) includes an example like the one above, so if doctesting and the live version work, then once the Sphinx versions are the official documentation for the distribution, we can consider this issue solved.


---

Comment by mhansen created at 2009-01-24 10:00:29

Yep, this is fine in the Sphinx documentation.


---

Comment by jhpalmieri created at 2009-02-21 23:41:08

This can be closed.


---

Comment by mabshoff created at 2009-02-24 19:57:10

Fixed by the ReST merge in 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 19:57:10

Resolution: fixed
