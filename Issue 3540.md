# Issue 3540: [with patch, needs review] Augment messes up the ncols for flat matrices.

Issue created by migration from https://trac.sagemath.org/ticket/3540

Original creator: rlm

Original creation time: 2008-07-01 19:27:28

Assignee: was

For example:

```
sage: M = Matrix(GF(2), 0, 0, 0)
sage: M
[]
sage: M.nrows()
0
sage: M.ncols()
0
sage: N = Matrix(GF(2), 0, 19, 0)
sage: N
[]
sage: N.nrows()
0
sage: N.ncols()
19
sage: W = M.augment(N)
sage: W
[]
sage: W.nrows()
0
sage: W.ncols()
0
```



---

Attachment

fixes SIGSEGV in first patch


---

Attachment

The original patch introduced a SIGSEGV which I've fixed in `trac-3540-augment-fix.patch`. Together with my fix I'll give it a positive review, so somebody needs to approve my fix.


---

Comment by rlm created at 2008-07-02 21:38:31

If I'm allowed to give malb's patch a positive review, I do.


---

Comment by mabshoff created at 2008-07-03 00:42:10

Replying to [comment:2 rlm]:
> If I'm allowed to give malb's patch a positive review, I do. 

Yes, since you know the code and his patch corrects an issue with your patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-03 02:53:08

Resolution: fixed


---

Comment by mabshoff created at 2008-07-03 02:53:08

Merged both patches in Sage 3.0.4.alpha2
