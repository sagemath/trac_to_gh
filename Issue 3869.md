# Issue 3869: CremonaDatabase functions iter() and isogeny_classes() sort keys wrongly

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-08-15 08:43:49

Assignee: cremona

Keywords: elliptic curve database

Example:

```
sage: CDB=CremonaDatabase()    
sage: [[EllipticCurve(ai[0]).label() for ai in C] for C in CDB.isogeny_classes(1728)]

[['1728a1', '1728a2', '1728a3', '1728a4'],
 ['1728b1'],
 ['1728ba1'],
 ['1728bb1', '1728bb2', '1728bb3'],
 ['1728c1'],
 ['1728d1'],
 ['1728e1', '1728e2', '1728e3'],
 ['1728f1', '1728f2'],
 ['1728g1'],
 ['1728h1'],
 ['1728i1'],
 ['1728j1', '1728j2', '1728j3'],
 ['1728k1'],
 ['1728l1'],
 ['1728m1', '1728m2'],
 ['1728n1'],
 ['1728o1'],
 ['1728p1'],
 ['1728q1'],
 ['1728r1'],
 ['1728s1', '1728s2', '1728s3'],
 ['1728t1'],
 ['1728u1'],
 ['1728v1', '1728v2', '1728v3', '1728v4'],
 ['1728w1'],
 ['1728x1'],
 ['1728y1'],
 ['1728z1']]
```


The keys are strings like '1728a1',...,'1728z1','1728ba1',... and these a wrongly sorted by the standard sort function.  What this means is that when iterating through the database, the isogeny classes are not listed in the standard order a,b,...,z,ba,bb,...,bz,...

In the above example, classes ba and bb should come after class z, and not between classes b and c.



---

Attachment

The attached patch fixes this by defining a new cmp function for curve codes which gets it right.

This should apply to 3.1.

I have doctested the new functions, and also checked that ell_rational_field doctests ok.


---

Comment by mabshoff created at 2008-08-15 10:31:51

:)

Cheers,

Michael


---

Attachment

Looks good to me.

I added one more doctest; both patches should be applied.


---

Comment by cremona created at 2008-08-24 08:51:42

I like the extra doctest!  Thanks.


---

Comment by mabshoff created at 2008-08-25 02:58:29

Resolution: fixed


---

Comment by mabshoff created at 2008-08-25 02:58:29

Merged sage-trac3869.patch and trac3869-extra-doctest.patch in Sage 3.1.2.alpha1
