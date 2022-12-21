# Issue 8963: Make tableau row_stabilizer return group of perms involving all elements of the tableau

Issue created by migration from Trac.

Original creator: jdc

Original creation time: 2010-05-14 15:32:55

Assignee: sage-combinat

CC:  sage-combinat-devel@googlegroups.com

The row_stabilizer method of a tableau ignores elements of the tableau which are alone in their row, and this can cause problems.  For example,


```
sage: t = Tableau([[1,2],[3]])
sage: rs = t.row_stabilizer()
sage: PermutationGroupElement([(1,2),(3,)]) in rs
False
sage: rs.one().list()
[1, 2]
```


The expected output is "True" and "[1, 2, 3]".

I will attach a patch fixing this in a few minutes.


---

Attachment

The attached patch also adds a method called entries() which returns a list containing the entries of the tableau.  All tests pass and coverage for tableau.py is 100%.  The patch is based on sage-4.4.


---

Comment by mvngu created at 2010-05-15 02:56:31

Changing status from new to needs_review.


---

Comment by saliola created at 2010-06-12 17:10:33

Looks good to me.

Applies cleanly to sage-4.4.4.alpha0, all tests pass.


---

Comment by saliola created at 2010-06-12 17:10:33

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 01:44:45

Resolution: fixed
