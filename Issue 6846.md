# Issue 6846: follow up to #6751: fix warnings when building reference manual

Issue created by migration from https://trac.sagemath.org/ticket/6846

Original creator: mvngu

Original creation time: 2009-08-30 09:50:11

Assignee: tba

CC:  was cremona

The following section of the patch `trac_6751.patch` from #6751 results in two warnings when building the reference manual:

```
1202	            - QuadraticForm 
1203	 
1204	        This function computes the positive definition quadratic form 
1205	        obtained by letting G be the trace zero subspace of ZZ + 
1206	        2*self, which had rank 3, and restricting the pairing 
1207	           (x,y) = (x.conjugate()*y).reduced_trace() 
1208	        to G. 
```

The warning messages are:

```
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/algebras/quatalg/quaternion_algebra.py:docstring of sage.algebras.quatalg.quaternion_algebra:7: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/algebras/quatalg/quaternion_algebra.py:docstring of sage.algebras.quatalg.quaternion_algebra.QuaternionOrder.ternary_quadratic_form:11: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```




---

Comment by mvngu created at 2009-08-30 09:52:49

fix docstring warnings


---

Attachment

The patch `trac_6846-docstring.patch` should fix the reported warnings. It depends on #6751.


---

Comment by was created at 2009-08-30 21:51:59

Thanks!


---

Comment by mvngu created at 2009-08-31 08:05:27

Resolution: fixed
