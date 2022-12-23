# Issue 2584: printing bug with show()

Issue created by migration from https://trac.sagemath.org/ticket/2584

Original creator: craigcitro

Original creation time: 2008-03-18 11:51:35

Assignee: jason

This causes a bug when printing:


```
show([Matrix(ZZ,3,range(9)), Matrix(ZZ,3,range(9))])
```


Notice the extra ",". A list of one element doesn't have the same problem.


---

Comment by jason created at 2008-03-18 17:05:41

The bug is in the latex function:


```
sage: latex([Matrix(ZZ,3,range(9)), Matrix(ZZ,3,range(9))])
\begin{array}{l}[\left(\begin{array}{rrr}
0 & 1 & 2 \\
3 & 4 & 5 \\
6 & 7 & 8
\end{array}\right),\\
\left(\begin{array}{rrr}
0 & 1 & 2 \\
3 & 4 & 5 \\
6 & 7 & 8
\end{array}\right)],\\
\end{array}
```



---

Comment by jason created at 2008-03-18 18:42:53

Actually, the bug is in the list_function in latex.py in the case where the list string is too long.  I'll post a patch momentarily.


---

Attachment


---

Comment by jason created at 2008-03-18 18:59:03

I believe the above patch works, but I'm still building 2.10.4, so I haven't tested it yet.


---

Comment by jason created at 2008-03-18 20:31:19

The patch fixes the problem.


---

Comment by mabshoff created at 2008-03-18 20:44:19

Replying to [comment:4 jason]:
> The patch fixes the problem.

While the patch looks like the fix to this problem shouldn't we also add a doctest that verifies that the bug has been fixed? Not to be pedantic ... well, I am :=)

Great job Jason.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-03-18 22:54:34

I added some doctests; only the last patch should be applied. Positive review from me.


---

Comment by mabshoff created at 2008-03-19 00:32:35

Merged 2584.patch in Sage 2.11.alpha0 - thanks Mike for the doctest.


---

Comment by mabshoff created at 2008-03-19 00:32:35

Resolution: fixed


---

Comment by jason created at 2008-03-19 00:46:13

Thanks, Mike for adding the doctests.  The reason I didn't add doctests to test this fix was that the bug was only manifest in the notebook (in EMBEDDED_MODE).  However, I should have gone ahead and added doctests for the basic functionality anyway, even if they didn't test that the bug in question is fixed, just to get the doctest score up and do my part towards the 3.0 goals :)


---

Comment by jason created at 2008-03-19 00:46:13

Changing priority from minor to trivial.
