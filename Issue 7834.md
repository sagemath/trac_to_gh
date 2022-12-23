# Issue 7834: Implement conjugate() for RealDoubleElement

Issue created by migration from https://trac.sagemath.org/ticket/7834

Original creator: dagss

Original creation time: 2010-01-03 18:53:11

Assignee: AlexGhitza

This appears inconsistent, and is an actual problem for me:

```
sage: ZZ(4).conjugate()
4
sage: RR(4).conjugate()
4.00000000000000
sage: RDF(4).conjugate()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/uio/arkimedes/s07/dagss/.sage/temp/corcaroli.uio.no/12687/_uio_arkimedes_s07_dagss__sage_init_sage_0.py in <module>()

AttributeError: 'sage.rings.real_double.RealDoubleElement' object has no attribute 'conjugate'
```




---

Comment by dagss created at 2010-01-03 18:53:52

Changing status from new to needs_review.


---

Attachment


---

Comment by AlexGhitza created at 2010-01-03 22:37:29

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-01-03 22:37:29

Looks good to me.


---

Comment by mhansen created at 2010-01-04 02:03:38

Resolution: fixed
