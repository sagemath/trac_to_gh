# Issue 4752: list_plot3d crashes sage with some exact input

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-12-10 21:11:34

Assignee: was

Keywords: list_plot3d, graphics

The following is an example of the problem (which was first noticed by "Snark" on the IRC sage-devel channel):

```
sage: pts =[(-4/5, -2/5, -2/5), (-4/5, -2/5, 2/5), (-4/5, 2/5, -2/5), (-4/5, 2/5, 2/5), (-2/5, -4/5, -2/5), (-2/5, -4/5, 2/5), (-2/5, -2/5, -4/5), (-2/5, -2/5, 4/5), (-2/5, 2/5, -4/5), (-2/5, 2/5, 4/5), (-2/5, 4/5, -2/5), (-2/5, 4/5, 2/5), (2/5, -4/5, -2/5), (2/5, -4/5, 2/5), (2/5, -2/5, -4/5), (2/5, -2/5, 4/5), (2/5, 2/5, -4/5), (2/5, 2/5, 4/5), (2/5, 4/5, -2/5), (2/5, 4/5, 2/5), (4/5, -2/5, -2/5), (4/5, -2/5, 2/5), (4/5, 2/5, -2/5), (4/5, 2/5, 2/5)]
sage: show(list_plot3d(pts))

------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

python(2829) malloc: *** error for object 0xed2f1f0: incorrect checksum for freed object - object was probably modified after being freed, break at szone_error to debug
python(2829) malloc: *** set a breakpoint in szone_error to debug
```


It doesn't crash if the pts are converted to numerical values, although the interpolated surface looks bad no matter which interpolation setting is used.  The example points are on a sphere.


---

Comment by was created at 2008-12-16 16:39:41

See also #4815 that is a dup of this, but has a traceback.


---

Comment by was created at 2008-12-17 02:24:31

Josh Kantor remarks:

```
Yeah, thats borked. Incidentally those test points include the top and bottom of the sphere so that will never look good. Even using only the top oints it looks crappy.

Over the summer as part of the internship I learned how to do meshless interpolation easily using a technique called Radial basis functions. I attached something I wrote from scratch that works well with those points. I'll have to work it into a patch.

It may be that in the upgrade of scipy that something changed with the the scipy packages we are using, I'll have to check that, if not I'll replace that with something from scratch.
```



---

Attachment

The segfault problem is because scipy just doesn't like multiple points with the same x,y coordinates and different z coordinates. The attached patch fixes that.

```
sage: pts =[(-4/5, -2/5, -2/5), (-4/5, -2/5, 2/5), (-4/5, 2/5, -2/5), (-4/5, 2/5, 2/5), (-2/5, -4/5, -2/5), (-2/5, -4/5, 2/5), (-2/5, -2/5, -4/5), (-2/5, -2/5, 4/5), (-2/5, 2/5, -4/5), (-2/5, 2/5, 4/5), (-2/5, 4/5, -2/5), (-2/5, 4/5, 2/5), (2/5, -4/5, -2/5), (2/5, -4/5, 2/5), (2/5, -2/5, -4/5), (2/5, -2/5, 4/5), (2/5, 2/5, -4/5), (2/5, 2/5, 4/5), (2/5, 4/5, -2/5), (2/5, 4/5, 2/5), (4/5, -2/5, -2/5), (4/5, -2/5, 2/5), (4/5, 2/5, -2/5), (4/5, 2/5, 2/5)]
sage: show(list_plot3d(pts))
```

I still intend to add the radial basis stuff, but this fixes the segfault


now raises an exception while


```
sage: pts =[(-4/5, -2/5, -2/5), (-4/5, -2/5, 2/5), (-4/5, 2/5, -2/5), (-4/5, 2/5, 2/5), (-2/5, -4/5, -2/5), (-2/5, -4/5, 2/5), (-2/5, -2/5, -4/5), (-2/5, -2/5, 4/5), (-2/5, 2/5, -4/5), (-2/5, 2/5, 4/5), (-2/5, 4/5, -2/5), (-2/5, 4/5, 2/5), (2/5, -4/5, -2/5), (2/5, -4/5, 2/5), (2/5, -2/5, -4/5), (2/5, -2/5, 4/5), (2/5, 2/5, -4/5), (2/5, 2/5, 4/5), (2/5, 4/5, -2/5), (2/5, 4/5, 2/5), (4/5, -2/5, -2/5), (4/5, -2/5, 2/5), (4/5, 2/5, -2/5), (4/5, 2/5, 2/5)]
sage: pts=[a in pts if a[2]>0]
sage: show(list_plot3d(pts))
```

works.


---

Comment by jkantor created at 2008-12-17 06:30:39

what I mean is the first code block raises an exception the second plots.


---

Attachment

patch to list_plot3d


---

Comment by jkantor created at 2008-12-17 07:48:45

2nd patch applied on top of first adds a doctest to demonstrate segfault does not occur it just catches the exception thrown.

Also I added a check that there are more than three points which is required for the interpolation. This is the issue with 4818.


---

Attachment


---

Comment by was created at 2008-12-17 07:57:19

REFEREE REPORT:

There are two problems:

1. A typo: "differet"

2. The illustrations of exceptions being raised are formatted incorrectly.  There's are thousands of examples in the sage doctests.  Find one and copy it.


---

Comment by jkantor created at 2009-01-23 04:10:12

addresses referree comments rebased against 3.2.3


---

Attachment

The 4752_patch fixes the issues raised by the referee and is rebased against 3.2.3


---

Comment by mabshoff created at 2009-02-02 04:21:27

William,

can you re-review this patch? Josh updated it, but I guess he forgot to change the status.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-07 06:42:35

This one ought to go into 3.3, so I am moving it.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-07 06:42:55

Oops, 3.3 now.

Cheers,

Michael


---

Comment by mhansen created at 2009-02-08 23:27:00

Looks good to me.


---

Comment by mabshoff created at 2009-02-09 08:06:55

4752_patch.patch needs to be rebased since the first hunk failed:

```
sage-3.3.rc0/devel/sage$ patch -p1 < trac_4752_patch.patch 
patching file sage/plot/plot3d/list_plot3d.py
Hunk #1 FAILED at 98.
Hunk #2 succeeded at 179 (offset 10 lines).
Hunk #3 succeeded at 199 (offset 10 lines).
1 out of 3 hunks FAILED -- saving rejects to file sage/plot/plot3d/list_plot3d.py.rej
```


Cheers,

Michael


---

Attachment

This is a rebase version of Josh's patch. The problem was trivial since only doctests had been added to the docstring. Apply only this patch.


---

Comment by mabshoff created at 2009-02-09 08:20:55

We need a doctest fix for this one:

```
sage -t -long "devel/sage/sage/plot/plot3d/list_plot3d.py"  
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/plot/plot3d/list_plot3d.py", line 119:
    sage: show(list_plot3d(pts,interpolation_type='nn'))
Expected:
    Traceback (most recent call last):
    ...
    ValueError: We need at least 3 points to perform the interpolation
Got nothing
**********************************************************************
```


Cheers,

Michael


---

Comment by jhpalmieri created at 2009-02-12 04:00:32

The error message about needing at least 3 points occurs in the function list_plot3d_tuples, which isn't even called unless there are at least 3 points.  So I just deleted this part of the doctest.  Hope that's okay.


---

Comment by jhpalmieri created at 2009-02-12 06:08:03

Never mind, here's a patch which keeps the doctest.  This one is better, so I'm replacing the old one.  It also fixes some typos and such in the old docstring.


---

Attachment

apply this on top of trac_4752_patch.2.patch


---

Comment by mabshoff created at 2009-02-14 02:32:24

4752-doctest.patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 09:15:29

Resolution: fixed


---

Comment by mabshoff created at 2009-02-14 09:15:29

Merged  trac_4752_patch.2.patch and 4752-doctest.patch in Sage 3.3.rc1.

Cheers,

Michael
