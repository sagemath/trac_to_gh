# Issue 2738: [with patch, positive review] LaTeX description environment in docstrings

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-03-31 14:34:25

Assignee: tba

Add support for:

```
"""
Computes Foo using one of the following algorithms:
\begin{description}
\item[Bar] cool algorithm.
\end{description}
"""
```



---

Attachment


---

Comment by mabshoff created at 2008-03-31 15:06:27

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-31 15:07:40

Merged in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-03-31 15:07:40

Resolution: fixed
