# Issue 4503: numerical noise in matrix_double_dense on intel mac os X 10.5: SVD

Issue created by migration from https://trac.sagemath.org/ticket/4503

Original creator: jhpalmieri

Original creation time: 2008-11-12 17:59:39

Assignee: somebody

CC:  jason

Keywords: numerical noise, matrix

(This has only been reported on intel macs running 10.4 or 10.5.)

From [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/fae59a9a9a53b8c0):


```
sage: m = matrix(RDF,3,2,range(6)); m

[0.0 1.0]
[2.0 3.0]
[4.0 5.0]
sage: U,S,V = m.SVD()
sage: U*S*V.transpose()   # random low order bits

[0.0 1.0]
[2.0 3.0]
[4.0 5.0]

max((U*S*V.transpose()-m).list())
1.7763568394e-15 
```


This leads to a doctest failure for `matrix_double_dense.py`.

Jason Grout suggests:

```
Okay, apparently the doctest just needs a looser bound; what you get is
still within reason for numerical issues.  Currently we see if that
maximum is < 1e-15.  Changing it to 1e-14 should fix this.
```

 


---

Attachment


---

Comment by jhpalmieri created at 2008-11-13 03:49:18

Here's a patch changing the doctest.  This fixes the problem on my mac.


---

Comment by mabshoff created at 2008-11-14 04:59:32

Positive review. Hopefully this will fix the dreaded numerical noise issue once and for all.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-14 17:18:08

Merged in Sage 3.2.rc1


---

Comment by mabshoff created at 2008-11-14 17:18:08

Resolution: fixed
