# Issue 5378: Sage 3.3: numerical noise in rings/polynomial/complex_roots.py on cicero & fulvia

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-26 02:40:47

Assignee: mabshoff

CC:  cwitty


```
sage -t  "devel/sage/sage/rings/polynomial/complex_roots.py"
**********************************************************************
File "/home/mariah/sage/sage-3.3-x86-Linux-fc-test/devel/sage/sage/rings/polynom
ial/complex_roots.py", line 271:
   sage: complex_roots(x^2 + 27*x + 181)
Expected:
   [(-14.61803398874990?..., 1), (-12.3819660112501...? + 0.?e-27*I, 1)]
Got:
   [(-12.3819660112501?, 1), (-14.61803398874990? + 0.?e-27*I, 1)]
```



---

Comment by mabshoff created at 2009-03-01 06:02:45

Hmm, the numerical noise of the imaginary part of the root causes the order of the roots for printing to be flipped. I am not sure what to do here except for picking another polynomial, but I have not looked into this in any detail since we might have this particular root for a good reason.

Cheers,

Michael


---

Comment by cwitty created at 2009-03-01 06:16:15

I don't remember anything special about that polynomial, so I'm fine with changing it.

Other possibilities would include changing the sorting.  One possibility would be to remove the code that puts real roots first; another possibility would be to special-case complex interval roots in the sorting, and say that if the imaginary part of a root is an interval that contains 0 then it should sort with the real roots.


---

Comment by mabshoff created at 2009-04-18 01:05:41

Move this to 3.4.1 since I am closing this as dupe of #5559.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 01:05:52

The following illustrates the problem and a potential solution:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: review
sage: from sage.rings.polynomial.complex_roots import complex_roots
sage: x = polygen(ZZ) 
sage: complex_roots(x^2 + 27*x + 181)
[(-12.3819660112501?, 1), (-14.61803398874990? + 0.?e-27*I, 1)]
sage: v=complex_roots(x^2 + 27*x + 181)
sage: sorted((v[0][0].real(),v[1][0].real()))
[-14.61803398874990?, -12.3819660112501?]
```

On another machine we get:

```
sage: from sage.rings.polynomial.complex_roots import complex_roots
sage:  x = polygen(ZZ)  
sage: complex_roots(x^2 + 27*x + 181)
[(-14.61803398874990? + 0.?e-27*I, 1), (-12.38196601125010? + 0.?e-27*I, 1)]
sage: v=complex_roots(x^2 + 27*x + 181)
sage: sorted((v[0][0].real(),v[1][0].real()))
[-14.61803398874990?, -12.38196601125010?]
```

Patch coming up.
| Sage Version 3.4.1.rc3, Release Date: 2009-04-16                   |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-04-19 01:47:03

Changing status from new to assigned.


---

Comment by rbeezer created at 2009-04-19 02:02:10

Builds and tests just fine.  Positive review.


---

Comment by mabshoff created at 2009-04-19 02:10:25

Resolution: fixed


---

Comment by mabshoff created at 2009-04-19 02:10:25

Merged in Sage 3.4.1.rc4.

Cheers,

Michael
