# Issue 4572: [with patch, needs review] maxima output has misleading precision

Issue created by migration from https://trac.sagemath.org/ticket/4572

Original creator: robertwb

Original creation time: 2008-11-20 22:00:37

Assignee: burcin

Internally, maxima uses floating point numbers internally unless explicitly told to use bigfloats (which we don't, and there's only one global precision in maxima so it will be non-trivial to try and do this consistantly). This patch changes the parsing code to use RDF instead, which is a better reflection of the underlying precision.

In addition, this has the benefit of removing the trailing zeros in calculus expressions involving real numbers (as they didn't really contain any information). 


---

Attachment


---

Comment by mhansen created at 2008-11-21 17:18:27

Applies and passes tests.


---

Comment by mabshoff created at 2008-11-21 19:48:50

This patch seems to cause a boat load of small and annoying doctest failures:

```
        sage -t -long devel/sage/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/rings/real_rqdf.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/rings/real_double.pyx # 2 doctests failed
        sage -t -long devel/sage/sage/rings/real_mpfr.pyx # 2 doctests failed
        sage -t -long devel/sage/sage/rings/complex_double.pyx # 3 doctests failed
        sage -t -long devel/sage/sage/plot/plot.py # 1 doctests failed
        sage -t -long devel/sage/sage/misc/parser.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/misc/prandom.py # 1 doctests failed
        sage -t -long devel/sage/sage/matrix/tests.py # 1 doctests failed
        sage -t -long devel/sage/sage/interfaces/maxima.py # 3 doctests failed
        sage -t -long devel/sage/sage/functions/special.py # 7 doctests failed
        sage -t -long devel/sage/sage/functions/constants.py # 1 doctests failed
        sage -t -long devel/sage/sage/functions/piecewise.py # 3 doctests failed
        sage -t -long devel/doc/tut/tut.tex # 1 doctests failed
```

I will make 100% sure this can all be blamed on this patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-21 20:05:29

Yep, someone needs to fix those doctests :)

Cheers,

Michael


---

Attachment


---

Attachment

apply to docs repo


---

Comment by robertwb created at 2008-11-25 11:28:04

All doctest failures were due to precision printing differences. Apply all attached patches.


---

Comment by mabshoff created at 2008-11-25 11:39:02

Positive review to the doctest fixes, so a cumulative positive review :)

Cheers,

Michae


---

Comment by mabshoff created at 2008-11-25 12:29:26

Resolution: fixed


---

Comment by mabshoff created at 2008-11-25 12:29:26

Merged both patches in Sage 3.2.1.alpha1
