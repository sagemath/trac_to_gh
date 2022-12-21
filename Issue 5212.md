# Issue 5212: [with patch, needs review] bug with numbers in names in sage.structure.parent_gens.normalize_names

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-02-09 04:20:51

Assignee: somebody

Keywords: numbers in names normalize_names

Try `PolynomialRing(QQ, 2, 'alpha0')` for hilarity.


---

Attachment


---

Comment by mabshoff created at 2009-02-09 12:26:34

With this patch applied to my current 3.3.rc0 merge tree all doctests pass.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-11 06:05:03

Merged in Sage 3.3.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-11 06:05:03

Resolution: fixed
