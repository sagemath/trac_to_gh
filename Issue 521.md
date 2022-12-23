# Issue 521: put a doctest for every single function schemes/elliptic_curves/monsky_washnitzer.py

Issue created by migration from https://trac.sagemath.org/ticket/521

Original creator: was

Original creation time: 2007-08-29 22:22:07

Assignee: dmharvey




---

Comment by mabshoff created at 2007-11-20 14:13:36


```
bsd:sage-2.8.13.rc0 mabshoff$ ./sage -coverage  devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py
----------------------------------------------------------------------
devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py: 5% (6 of 107)
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-12-26 02:52:38

While you are at it:

```
ERROR: Please define a s == loads(dumps(s)) doctest.
```


Cheers,

Michael


---

Comment by AlexGhitza created at 2008-01-24 23:46:41

Changing component from basic arithmetic to algebraic geometry.


---

Attachment


---

Comment by dmharvey created at 2008-01-28 01:35:58

I got started on writing doctests, see 521.patch. I'm not going to finish now, but still worth merging I guess. (Also there's a lot of code in there that robert wrote, which I'm not comfortable doctesting.)

The patch also makes some minor optimisations.


---

Comment by mabshoff created at 2008-02-15 22:10:06

I am getting some rejects with the current patch against 2.10.2.alpha0:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/devel/sage$ patch -p1 --dry-run < 521.patch\?format\=raw
patching file sage/schemes/elliptic_curves/monsky_washnitzer.py
patching file sage/schemes/elliptic_curves/monsky_washnitzer.py
Hunk #1 succeeded at 163 with fuzz 1 (offset -18 lines).
Hunk #2 succeeded at 200 (offset -52 lines).
Hunk #3 succeeded at 240 (offset -52 lines).
Hunk #4 succeeded at 267 (offset -52 lines).
Hunk #5 succeeded at 282 (offset -52 lines).
Hunk #6 succeeded at 311 (offset -52 lines).
Hunk #7 succeeded at 362 (offset -52 lines).
Hunk #8 succeeded at 381 (offset -52 lines).
Hunk #9 succeeded at 399 (offset -52 lines).
patching file sage/schemes/elliptic_curves/monsky_washnitzer.py
Hunk #1 FAILED at 380.
Hunk #2 succeeded at 300 (offset -89 lines).
Hunk #3 succeeded at 317 (offset -89 lines).
Hunk #4 succeeded at 334 (offset -89 lines).
Hunk #5 succeeded at 362 with fuzz 1 (offset -89 lines).
Hunk #6 FAILED at 383.
Hunk #7 succeeded at 476 (offset -90 lines).
2 out of 7 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/monsky_washnitzer.py.rej
```

Hopefully this can be easily fixed since we really ought to merge this patch.

Cheers,

Michael


---

Comment by dmharvey created at 2008-02-15 23:10:56

I will take a look. Should have a new patch by tomorrow.


---

Comment by dmharvey created at 2008-02-16 02:11:02

Ummm this is weird.

All of the following on 2.10.2.alpha0:

If I try patching using the command you used above, I get the same failure.

However, if I'm in the directory devel/sage/sage/schemes/elliptic_curves, and I just do `hg import 521.patch` then it works fine.


---

Comment by AlexGhitza created at 2008-02-17 02:30:30

patch rebased on sage-2.10.2.alpha0


---

Attachment


---

Comment by mabshoff created at 2008-02-17 17:10:25

Ok, Alex's rebase of David's patch raises the score to:

```
devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py: 23% (25 of 107)
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 17:12:05

Merged in Sage 2.10.2.alpha1. Even though the coverage is "only" up to 23% I am closing this. Please open another ticket if you come up with another patch to raise the doctest coverage.


---

Comment by mabshoff created at 2008-02-17 17:12:05

Resolution: fixed
