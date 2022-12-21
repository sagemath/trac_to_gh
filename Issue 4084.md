# Issue 4084: plot(1/cos,-1,1) fails

Issue created by migration from Trac.

Original creator: jwmerrill

Original creation time: 2008-09-09 03:44:08

Assignee: jwmerrill

Plot works with symbolic functions, but not compositions or arithmetic involving them.


```
sage: plot(cos,-1,1) #works

sage: plot(1/cos,-1,1)
Traceback (most recent call last):
...
TypeError: float() argument must be a string or a number
```



---

Attachment

Hi,

this is fixed in 3.1.2.rc1-ish:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.2.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.2.rc0, Release Date: 2008-09-06                   |
| Type notebook() for the GUI, and license() for information.        |
sage: plot(1/cos,-1,1)

sage: 
Exiting SAGE (CPU time 0m0.63s, Wall time 0m4.01s).
Exiting spawned Maxima process.
```

Please post a patch that adds only the doctest. There are unrelated changes in the patch.

Cheers,

Michael


---

Attachment

4804_doctest_only.patch adds only doctests.  If accepted, only that patch should be applied.  This should not be accepted until the new doctests actually pass.

Thanks for the quick catch mhansen.  "Unrelated" might be a little strong, though I was bold in modifying implementation to make this work.  In any case, sounds like problem solved.

Cheers,

JM


---

Comment by mabshoff created at 2008-09-09 04:21:14

Replying to [comment:2 jwmerrill]:
> 4804_doctest_only.patch adds only doctests.  If accepted, only that patch should be applied.  This should not be accepted until the new doctests actually pass.

I rebased the patch against my current merge tree. 

> Thanks for the quick catch mhansen.  "Unrelated" might be a little strong, though I was bold in modifying implementation to make this work.  In any case, sounds like problem solved.

It wasn't mhansen ;). The changes in plot.py had *zero* to do with the ticket and the "fix" is canonically wrong since we just don't just wipe out low order bits preventatively.

> Cheers,
> 
> JM

Cheers,

Michael


---

Comment by jwmerrill created at 2008-09-09 04:23:42

Both points well taken.

Cheers,

JM


---

Comment by mabshoff created at 2008-09-09 04:41:57

With the patch applied doctests do pass. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-09 04:45:42

Resolution: fixed


---

Comment by mabshoff created at 2008-09-09 04:45:42

Merged rebased 4804_doctest_only.patch in Sage 3.1.2.rc1
