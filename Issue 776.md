# Issue 776: kernel of linear homomorphism fails

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-10-01 21:28:02

Assignee: was


```
V=VectorSpace(QQ,3)
id=V.Hom(V)(identity_matrix(QQ,3))
null=V.Hom(V)(0*identity_matrix(QQ,3))
id.kernel()
```

produces

```
<type 'exceptions.TypeError'>: entries must be coercible to a list or integer
```




---

Attachment

fixes the bug


---

Comment by was created at 2007-10-01 21:44:35

Resolution: fixed


---

Attachment


---

Comment by was created at 2007-10-02 03:08:29

I screwed up fixing this.   Apply the correct_fix.patch after the other.  Now this is fixed.
