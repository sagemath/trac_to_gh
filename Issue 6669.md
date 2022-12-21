# Issue 6669: Homomorphisms from matrix groups don't have to have matrix groups as codomain

Issue created by migration from Trac.

Original creator: mraum

Original creation time: 2009-08-03 20:36:35

Assignee: mraum

CC:  mhansen alexghitza

This is an error which occurs if one tries to construct coercing from a matrix group into an algebra. The current implementation of homomorphisms with domain a matrix group require the codomain to be a matrix group, too.
 

```
/home/martin/sage-4.1_compiled/local/lib/python2.6/site-packages/sage/categories/homset.pyc in Hom(X, Y, cat)
     64     """
     65     if hasattr(X, '_Hom_'):
---> 66         return X._Hom_(Y, cat)
     67 
     68     global _cache

/home/martin/sage-4.1_compiled/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in _Hom_(self, G, cat)
    230             raise NotImplementedError
    231         if not is_MatrixGroup(G):
--> 232             raise TypeError, "G (=%s) must be a matrix group."%G
    233         import homset
    234         return homset.MatrixGroupHomset(self, G)

TypeError: G (=Group algebra of group "General Linear Group of degree 3 over Finite Field of size 7" over base ring Integer Ring) must be a matrix group.
```




---

Comment by mraum created at 2009-10-22 16:50:07

Changing status from new to needs_review.


---

Attachment


---

Comment by AlexGhitza created at 2009-11-15 10:01:20

Changing status from needs_review to needs_work.


---

Comment by AlexGhitza created at 2009-11-15 10:01:20

This looks good, applies cleanly and passes long tests under sage-4.2.  I will test on sage-4.2.1 as soon as sage.math binaries are available.

One thing needs to be fixed: please add some doctests with examples of homomorphisms between matrix groups, and from matrix groups to other types of groups.  (I do realise that the method patched here did not have doctests to start with.)


---

Attachment

Patch with doctests.


---

Comment by robertwb created at 2009-11-20 05:17:06

Yep, doctests look fine.


---

Comment by robertwb created at 2009-11-20 05:17:06

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2009-11-20 05:17:28

Looks good to me.


---

Comment by robertwb created at 2009-11-20 05:17:28

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-20 05:30:12

Resolution: fixed
