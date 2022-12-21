# Issue 4560: SR and containment broken

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-11-20 01:35:11

Assignee: burcin

CC:  mhansen

This is bad


```
sage: sqrt(2) in CC
False
```



---

Attachment


---

Comment by burcin created at 2009-01-23 08:00:39

Though seeing `SymbolicEquation` in parent.pyx is very scary at first, this is a good solution. :)


---

Comment by mabshoff created at 2009-01-23 08:31:14

The above patch causes the following doctest failure in tut.tex:

```
There is one subtlety in defining complex numbers: as mentioned above,
the symbol \code{i} represents a square root of \minusone, but it is a
\emph{formal} square root of \minusone; it is not in the complex numbers.
Calling \code{CC(i)} returns the complex square root of \minusone.
%link
\begin{verbatim}
sage: i in CC
False
```

now returns true. After some discussion with William it was decided to change the doctest.

Cheers,

Michael


---

Attachment

Documentation fix


---

Comment by mabshoff created at 2009-01-29 02:46:13

Rebased verison of Roed's patch


---

Comment by mabshoff created at 2009-01-29 02:46:54

Resolution: fixed


---

Attachment

Merged 4560-doc.patch and trac_4560.patch in Sage 3.3.alpha3.

Cheers,

Michael
