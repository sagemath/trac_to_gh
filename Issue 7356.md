# Issue 7356: fixed latex representation for floats

Issue created by migration from Trac.

Original creator: robert.marik

Original creation time: 2009-10-30 09:12:06

Assignee: AlexGhitza

Floats have no LaTeX representation and are formated using str function. Thus output of latex(float(1e25)) is '1e+25' and not '1 \times 10^{25}'. 

The solution is to define function to handle this like the function below

```

def float_function(x):
    r"""
    Returns the LaTeX code for a float ``x``.

    INPUT: ``x`` - float number

    EXAMPLES::

        sage: from sage.misc.latex import float_function
        sage: float_function(float(123.05))
        '123.05'
        sage: float_function(float(3e-15))
        '3 \\times 10^{-15}'
        sage: float_function(float(3.2e25))
        '3.2 \\times 10^{25}'
        sage: float_function(float(3.2e+15))
        '3.2 \\times 10^{15}'

        The output is in some cases shorter than latex method for real numbers.

        sage: float_function(float(1e+15))
        '1 \\times 10^{15}'
    """
    s = str(x)
    parts = s.split('e')
    if len(parts) > 1:
        # scientific notation
        if parts[1][0] == '+':
            parts[1] = parts[1][1:]
        s = "%s \\times 10^{%s}" % (parts[0], parts[1])
    return s
```


Will post simple patch, provided it passes tests.


---

Attachment

The patch for 4.2 is attached. When running tests I got two errors not related to the change in this trac. The first one is solved in #6479.


```
sage -t  "devel/sage/sage/calculus/desolvers.py"
sage -t  "devel/sage/sage/interfaces/maxima.py"
```



---

Comment by robert.marik created at 2009-10-30 10:42:44

Changing status from new to needs_review.


---

Comment by robert.marik created at 2009-10-30 11:00:57


```
sage -t  "devel/sage/sage/interfaces/maxima.py"
```

This test passed as well. (Error has been introduced by my custom settings in maxima-init.lisp file)


---

Comment by robert.marik created at 2009-10-30 14:15:44

According to [this](http://groups.google.cz/group/sage-devel/browse_thread/thread/67657d52cbc5a915) thread, there is another patch for this with slightly different output: #7328


---

Comment by jhpalmieri created at 2009-11-06 06:01:20

Changing status from needs_review to needs_info.


---

Comment by jhpalmieri created at 2009-11-06 06:01:20

Should this be closed as a duplicate since #7328 has been closed with a positive review?


---

Comment by robert.marik created at 2009-11-07 21:27:37

Replying to [comment:4 jhpalmieri]:
> Should this be closed as a duplicate since #7328 has been closed with a positive review?

Perhaps yes, but the patch in this trac produces shorter output, so I think that this is better. The patch #7328 produces sometimes zeros which are not necessary at the end of decimal number.


---

Comment by robertwb created at 2009-11-20 05:23:08

Changing status from needs_info to needs_review.


---

Attachment

Use instead of other, applies on top of #7328


---

Comment by robertwb created at 2009-11-20 05:31:30

I agree, less digits should be printed. Floats are more like RDF than RR, so I've posted a patch that applies on top of #7328. The attached patch works fine to (though will conflict with 4.2.1).


---

Attachment

apply on top of latex-float-4.2.1.patch


---

Comment by robert.marik created at 2009-11-20 07:47:27

Seems good, thanks for fixing. Since one test failed, I fixed it in reviewers patch which should be installed on the top of latex-float-4.2.1.patch  

Tests are O.K. now. Positive review.


---

Comment by robert.marik created at 2009-11-20 07:47:27

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-22 07:56:21

Resolution: fixed
