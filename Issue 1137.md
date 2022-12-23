# Issue 1137: matrix visualize_structure is completely broken on osx (at least 10.5) -- why no doctest to catch this!?

Issue created by migration from https://trac.sagemath.org/ticket/1137

Original creator: was

Original creation time: 2007-11-10 12:09:31

Assignee: was


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



---

Comment by mabshoff created at 2007-11-20 13:59:10

With 2.8.13.rc0 in bsd the above code works and outputs a png. So who can actually still reproduce this?

Cheers,

Michael


---

Comment by rlm created at 2007-12-02 00:42:29


```
sage: M = random_matrix(CC, 4)
sage: M.visualize_structure()
sage:
```

on OS 10.5.1. However,

```
sage: M

[ 1.00000000000000                 0  2.00000000000000 -2.00000000000000]
[ 2.00000000000000 -1.00000000000000  2.00000000000000  2.00000000000000]
[                0 -2.00000000000000  2.00000000000000                 0]
[-2.00000000000000 -1.00000000000000 -2.00000000000000  1.00000000000000]
```

and the output is all white.


---

Attachment

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



---

Comment by rlm created at 2007-12-03 03:21:01

This patch does not fix the OS X 10.4 problem, but it does fix some other bugs in the same function.


---

Comment by mabshoff created at 2007-12-15 14:10:48

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 14:10:48

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-16 14:27:11

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-12-16 14:27:11

Resolution changed from fixed to 


---

Comment by mabshoff created at 2007-12-16 14:27:11

Fixing the issue by updating libpng breaks other spkgs like R, so revert it until we can figure out how to solve it properly.

Cheers,

Michael


---

Comment by rlm created at 2008-02-10 03:05:22

Resolution: fixed
