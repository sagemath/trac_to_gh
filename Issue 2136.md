# Issue 2136: matrix visualize_structure is completely broken on osx (at least 10.5) -- why no doctest to catch this!?

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-02-10 03:06:18

Assignee: was

This ticket is a migration of #1137. There was a patch associated with the ticket, that was merged in to the library, but it was not related to the original issue. Below is a reproduction of the original description.


```
sage: sr = mq.SR(2,1,1,4,gf2=True)
sage: sr
SR(2,1,1,4)
sage: F,s = sr.polynomial_system()
sage: F
Polynomial System with 104 Polynomials in 36 Variables
sage: gb = F.groebner_basis()
sage: Ideal(gb).variety()
[{x101: 0, x100: 0, x103: 1, x102: 0, k103: 1, x202: 0, x203: 1, x200: 1, x201: 1, w100: 0, w101: 0, w102: 0, w103: 1, k102: 1, k203: 0, k202: 1, k201: 0, k200: 1, s001: 0, s000: 1, s003: 1, s002: 1, k001: 1, k000: 0, k003: 1, k002: 0, w203: 0, w202: 0, w201: 1, w200: 0, s100: 1, s101: 0, s102: 0, s103: 0, k100: 1, k101: 1}]
sage: s
{k001: 1, k000: 0, k003: 1, k002: 0}
sage: A,v = F.coefficient_matrix()
sage: A.visualize_structure()
Traceback (most recent call last):
...
ImportError: dlopen(/Users/was/s/local/lib/python2.5/site-packages/_gd.so, 2): Library not loaded: /Users/was/Desktop/sage-2.8.10.rc1/local/lib/libpng.3.dylib
  Referenced from: /Users/was/s/local/lib/python2.5/site-packages/_gd.so
  Reason: image not found
```


Todo:

   1. Make a doctest that would catch this
   2. Fix the problem. 

Robert WB's comments:
I can't get this to work at all on OS X 10.4 (intel)


```
sage: sage: M.visualize_structure()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "matrix2.pyx", line 2853, in sage.matrix.matrix2.Matrix.visualize_structure
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/gd.py", line 10, in <module>
    import _gd
<type 'exceptions.ImportError'>: dlopen(/Users/robert/sage/current/local/lib/python2.5/site-packages/_gd.so, 2): Symbol not found: _png_get_rowbytes
  Referenced from: /Users/robert/sage/current/local/lib//libgd.2.dylib
  Expected in: flat namespace
```


Mabshoff's comment:

Fixing the issue by updating libpng breaks other spkgs like R, so revert it until we can figure out how to solve it properly.


---

Comment by malb created at 2008-08-18 19:39:33

This is the same issue as #3324.


---

Comment by mabshoff created at 2008-12-05 04:49:01

Changing component from linear algebra to doctest.


---

Comment by mabshoff created at 2008-12-05 04:49:01

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-12-05 04:49:01

This has worked for a while:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sr = mq.SR(2,1,1,4,gf2=True)
sage: F,s = sr.polynomial_system()
sage: 
sage: gb = F.groebner_basis()
sage: Ideal(gb).variety()
| Sage Version 3.2.1.alpha2, Release Date: 2008-11-26                |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: Ideal(gb).variety()
[{s001: 0, s103: 1, s101: 1, x103: 1, s000: 1, x101: 0, k003: 0, k100: 0, k001: 0, k200: 0, x200: 0, k202: 0, x202: 0, w102: 1, w100: 0, w201: 0, s002: 0, w203: 1, k101: 1, s102: 0, s100: 1, x102: 0, x100: 1, k002: 1, k000: 0, x201: 0, k201: 0, x203: 1, k203: 0, k103: 0, w103: 0, k102: 0, w101: 0, w200: 0, s003: 1, w202: 0}]
sage: 
sage: A,v = F.coefficient_matrix()
sage: A.visualize_structure()
sage: 
Exiting SAGE (CPU time 0m0.99s, Wall time 0m56.28s).
Exiting spawned Singular process.
```

So let's add a doctest and get this ticket closed unless there already is such a doctest. (which I believe there is).

malb?

Cheers,

Michael


---

Comment by malb created at 2009-01-22 07:47:29

The bug is fixed and #3321 re-enables doctests for this function. I vote for closing this ticket.


---

Comment by mabshoff created at 2009-01-22 10:49:00

Replying to [comment:4 malb]:
> The bug is fixed and #3321 re-enables doctests for this function. I vote for closing this ticket.

I concur. Fixed via #3321.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-22 10:49:00

Resolution: fixed
