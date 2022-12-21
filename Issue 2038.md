# Issue 2038: plotting -- error message when failing to evaluate at a point is now sucky (it used to be good)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-03 20:00:23

Assignee: was

It used to be that this would give a sensible error message about the number of points at which evaluating the function failed (and what the first error was):


```
sage: plot(factorial,(2,10))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   3343             # if there is one extra arg, then it had better be a tuple
   3344             elif n == 1:
-> 3345                 G = self._call(funcs, *args, **kwds)
   3346             elif n == 2:
   3347             # if ther eare two extra args, then pull them out and pass them as a tuple

/Users/was/s/local/lib/python2.5/site-packages/sage/plot/plot.py in _call(self, funcs, xrange, parametric, polar, label, **kwds)
   3419         del options['plot_division']
   3420         while i < len(data) - 1:
-> 3421             if abs(data[i+1][1] - data[i][1]) > max_bend:
   3422                 x = (data[i+1][0] + data[i][0])/2
   3423                 try:

<type 'exceptions.TypeError'>: 'float' object is unsubscriptable
```


The exception of course should mention that:


```
sage: factorial(1.5)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/rings/arith.py in factorial(n, algorithm)
    273     Z = integer_ring.ZZ
    274     if algorithm == 'gmp':
--> 275         return Z(n).factorial()
    276     elif algorithm == 'pari':
    277         return Z(pari('%s!'%Z(n)))

/Users/was/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: Attempt to coerce non-integral RealNumber to Integer
```



---

Comment by was created at 2008-02-04 18:20:44

See also #2045.


---

Attachment


---

Comment by moretti created at 2008-02-08 00:05:04

Please review this fix.


---

Comment by moretti created at 2008-02-08 00:08:58

Actually, the fix that I posted only fixes http://trac.sagemath.org/sage_trac/ticket/2038 which was listed as a dupe of this bug, but in fact is not. I will fix the issue reported here and provide another fix.


---

Comment by moretti created at 2008-02-08 07:48:05

Check out empty_plot_list.patch; together with plot.patch it fixes both this ticket and http://trac.sagemath.org/sage_trac/ticket/2045.


---

Comment by ncalexan created at 2008-02-15 04:15:39

I can't tell what the issue was or what the corrected behaviour is, BECAUSE THERE ARE NO DOCTESTS.  I say do not apply.

The patch looks good, but I don't think it's been tested enough.  For example, what happens if there are *no* valid data points?


---

Comment by was created at 2008-03-12 05:01:39

This must get fixed.  This seems to be responsible for about 1/3 of bug/confusions on sage-support.


---

Comment by jason created at 2008-03-18 21:56:50

Yet another fix of this is up at #2517.  The various patches should be combined into one good patch.


---

Comment by jason created at 2008-03-18 22:00:03

Where is the "empty_plot_list.patch" that is referred to above?  Is the above plot.patch and the patch at #2517 the only patches that address this problem (and the ones that should be combined?)


---

Comment by jason created at 2008-03-19 01:50:38

This ticket is addressed now with #2517 and #2590 and should probably be marked a duplicate.


---

Comment by mabshoff created at 2008-03-19 02:17:28

Resolution: duplicate
