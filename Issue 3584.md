# Issue 3584: cython.py -- randomness in doctests

Issue created by migration from https://trac.sagemath.org/ticket/3584

Original creator: was

Original creation time: 2008-07-07 15:21:02

Assignee: failure

On Debian 64-bit vmware:

```
sage -t  devel/sage/sage/misc/cython.py                     **********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/cython.py", line 109:
    sage: pyx_preparse("")
Expected:
    ('\ninclude "interrupt.pxi"  # ctrl-c interrupt block support\ninclude "stdsage.pxi"  # ctrl-c interrupt block support\n\ninclude "cdefs.pxi"\n',
    ['mpfr',
    'gmp',
    'gmpxx',
    'stdc++',
    'pari',
    'm',
    'curvesntl',
    'g0nntl',
    'jcntl',
    'rankntl',
    'gsl',
    'cblas',
    'atlas',
    'ntl',
    'csage'],
    ['.../local/include/csage/',
    '.../local/include/',
    '.../local/include/python2.5/',
    '.../devel/sage/sage/ext/',
    '.../devel/sage/',
    '.../devel/sage/sage/gsl/'],
    'c',
    [])
Got:
    ('\ninclude "interrupt.pxi"  # ctrl-c interrupt block support\ninclude "stdsage.pxi"  # ctrl-c interrupt block support\n\ninclude "cdefs.pxi"\n', ['mpfr', 'gmp', 'gmpxx', 'stdc++', 'pari', 'm', 'curvesntl', 'g0nntl', 'jcntl', 'rankntl', 'gsl', 'gslcblas', 'atlas', 'ntl', 'csage'], ['/home/was/build/sage-3.0.4.alpha2/local/include/csage/', '/home/was/build/sage-3.0.4.alpha2/local/include/', '/home/was/build/sage-3.0.4.alpha2/local/include/python2.5/', '/home/was/build/sage-3.0.4.alpha2/devel/sage/sage/ext/', '/home/was/build/sage-3.0.4.alpha2/devel/sage/', '/home/was/build/sage-3.0.4.alpha2/devel/sage/sage/gsl/'], 'c', [])
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/cython.py", line 138:
    sage: libs
Expected:
    ['foo', 'mpfr',
    'gmp', 'gmpxx',
    'stdc++',
    'pari',
    'm',
    'curvesntl', 'g0nntl', 'jcntl', 'rankntl',
    'gsl', 'cblas', 'atlas',
    'ntl',
    'csage']
Got:
    ['foo', 'mpfr', 'gmp', 'gmpxx', 'stdc++', 'pari', 'm', 'curvesntl', 'g0nntl', 'jcntl', 'rankntl', 'gsl', 'gslcblas', 'atlas', 'ntl', 'csage']
**********************************************************************
1 items had failures:
   2 of   7 in __main__.example_1
```



---

Comment by craigcitro created at 2008-07-07 18:31:39

Changing status from new to assigned.


---

Attachment

The attached patch fixes the doctest, and adds another that's slightly better. I also did a bit of cleanup in the file. 

I added a docstring to `parse_keywords`, and also made one minor change to that function. (It used to always add a `#` right before the keyword, so I had it check to see if it was already on a line containing a hash. I could be convinced this isn't worth it.)


---

Comment by craigcitro created at 2008-07-07 18:31:39

Changing assignee from failure to craigcitro.


---

Comment by was created at 2008-07-07 21:49:03

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 21:51:31

Merged in Sage 3.0.4.rc0
