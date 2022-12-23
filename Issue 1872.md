# Issue 1872: serious bug in pickling elliptic curves

Issue created by migration from https://trac.sagemath.org/ticket/1872

Original creator: was

Original creation time: 2008-01-20 22:22:44

Assignee: was


```
sage: E = EllipticCurve('185c1')
sage: E.gens()
[(-5/4 : 3/8 : 1)]
sage: loads(dumps(E))
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/was/papers/bsdalg/newdata/heegner_index_rank1/data/<ipython console> in <module>()

/Users/was/papers/bsdalg/newdata/heegner_index_rank1/data/sage_object.pyx in sage.structure.sage_object.loads()

/Users/was/papers/bsdalg/newdata/heegner_index_rank1/data/sage_object.pyx in sage.structure.sage_object.loads()

/Users/was/s/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.py in make_point(X, v)
    648     # It looks like there's generic code to do this, but it's been commented out. 
    649     #
    650     # Here we create a new (equivalent) parent manually. 
--> 651     del X._Scheme__ring_point_homset
    652     return EllipticCurvePoint_field(X, v)

<type 'str'>: (<type 'exceptions.AttributeError'>, AttributeError("'EllipticCurve_rational_field' object has no attribute '_EllipticCurve_generic__ainvs'",))

```



---

Attachment

this fixes the problem


---

Comment by was created at 2008-01-21 06:35:30

The patch simply deletes some functions, deletes some commented out code, and names a variable something meaningful instead of meaningless.


---

Comment by mabshoff created at 2008-01-21 09:37:59

Resolution: fixed


---

Comment by mabshoff created at 2008-01-21 09:37:59

Merged in Sage 2.10.1.alpha0
