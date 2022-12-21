# Issue 6745: quaternion algebras -- add computation of left and right orders associated to ideals

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-08-14 16:23:57

Assignee: tbd

A big gap in functionality for quaternion algebras right now is that one can't compute the left and right orders associated to ideals (the functions raise NotImplementedError).    I just designed a little algorithm and wrote code to do this for my research and will post a patch here soon. 

Just in case I misplace it, some demo code that works is the following:

```
def left_order(I):
    Q = O.quaternion_algebra()
    M = [matrix([(a*b).coefficient_tuple() for a in Q.basis()]) for b in I.basis()]
    B = I.basis_matrix()
    invs = [(B*m^(-1)).row_module(ZZ) for m in M]
    IS = invs[0].intersection(invs[1]).intersection(invs[2]).intersection(invs[3])
    ISB = [Q(v) for v in IS.basis()]
    return Q.quaternion_order(ISB)
```



---

Attachment

sage/algebras/quatalg/quaternion_algebra.py:1272


```
ALGORITHM: Let `b_1, b_2, b_3, b_3` be a basis for this 
```


(Typo, you want b_4). 

TabularUnified  sage/matrix/matrix_integer_dense.pyx:2310


```
if max(self._nrows, self._ncols) <= 50: 
```


I think you intended to have an `elif` here. 

Other than that, looks good to me. Also, while I was playing around with it trying it out, I found #6762 useful.


---

Comment by mvngu created at 2009-08-25 03:13:35

William: any words on the typos reported by Robert?


---

Comment by was created at 2009-08-30 21:58:09

Regarding Robert's comments:

* I posted a patch fixing the `b_3 |--> b_4` typo.

* The matrix_integer_dense.pyx is *not* a typo.  The issue is that I want to default to pari for small matrices, *unless* said small matrix has huge entries, so the logic is correct (i.e., if entries huge, still use padic).  I've put in some spaces and an {{{# endif} comment to maybe make that seem more intentional. 

So the attached patch changes no logic in the code, but changes/improves two comments.


---

Attachment

fix comments


---

Comment by robertwb created at 2009-08-31 16:09:43

Great. Positive review.


---

Comment by mvngu created at 2009-09-02 15:41:53

Merged both patches.


---

Comment by mvngu created at 2009-09-02 15:41:53

Resolution: fixed
