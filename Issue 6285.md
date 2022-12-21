# Issue 6285: Wrong description of arcsin function

Issue created by migration from Trac.

Original creator: gmhossain

Original creation time: 2009-06-14 11:43:56

Description for "arcsin" wrongly says it is "The inverse of the hyperbolic sine function" !!


```
arcsin?

File:        /home/golam/foo/sage-4.0.1/local/lib/python2.5/site-packages/sage/functions/trig.py
Type:        <class 'sage.functions.trig.Function_arcsin'>
Definition:  arcsin(x, hold='False')
Docstring: 

        The inverse of the hyperbolic sine function.

        EXAMPLES::

            sage: arcsinh(0.5)
            0.481211825059603
            sage: arcsinh(1/2)
            arcsinh(1/2)
            sage: arcsinh(1 + 1.0*I)

```



---

Comment by gmhossain created at 2009-06-14 12:47:20

Changing keywords from "" to "arcsin, wrong description".


---

Comment by burcin created at 2009-06-14 13:02:20

Changing status from new to assigned.


---

Comment by burcin created at 2009-06-14 13:02:20

I fixed these as a part of #6244. This bug can be closed once #6244 is merged.


---

Comment by burcin created at 2009-06-14 13:02:20

Set assignee to burcin.


---

Comment by ncalexan created at 2009-06-14 22:20:26

Resolution: fixed
