# Issue 6760: error in quaternion algebra ideal basis

Issue created by migration from https://trac.sagemath.org/ticket/6760

Original creator: robertwb

Original creation time: 2009-08-16 08:49:58

Assignee: tbd


```
sage: R.<i,j,k> = QuaternionAlgebra(-1, -13)        
sage: I = R.ideal([2+i, 3*i, 5*j, j+k]); I
Fractional ideal (2 + i, 3*i, j + k, 5*k)
sage: I.free_module()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/sage-4.0/local/lib/python2.6/site-packages/sage/algebras/quatalg/quaternion_algebra.py", line 1503, in free_module
    M = self.hermite_basis_matrix().row_module(ZZ)
AttributeError: 'QuaternionFractionalIdeal_rational' object has no attribute 'hermite_basis_matrix'
```



---

Attachment

I think this is the right fix, but someone more familiar with the code should take a look.


---

Comment by AlexGhitza created at 2009-11-15 10:19:53

Looks good to me.  I am adding a patch with a doctest (just the example that was given above).

Robert, if you're happy with the second patch, please change this to a positive review.


---

Attachment

apply after the previous patch


---

Comment by robertwb created at 2009-11-16 18:30:23

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-17 06:16:23

Resolution: fixed
