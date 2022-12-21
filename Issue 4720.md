# Issue 4720: Numerical noise in test sage/rings/number_field/number_field_morphisms.pyx

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2008-12-05 21:57:48

Assignee: tbd

On Fedora 10, 32 bits in sage-3.2.2.alpha0 the following test failed:



```
Expecting:
     -0.500000000000000 + 0.866025403784439*I
**********************************************************************
File "/home/jaap/Download/sage-3.2.1.rc0/devel/sage/sage/rings/number_field/number_field_morphisms.pyx",
line 210, in __main__.example_10
Failed example:
     closest_root(x**Integer(3)-Integer(1), CDF.gen(0))###line
223:_sage_    >>> closest_root(x^3-1, CDF.0)
Expected:
     -0.500000000000000 + 0.866025403784439*I
Got:
     -0.500000000000000 + 0.866025403784438*I


```



Jaap




---

Comment by jsp created at 2008-12-05 22:08:14

Same failure on Fedora 9, 32 bits.

Jaap


---

Comment by jhpalmieri created at 2008-12-09 18:02:08

This patch fixes it for me.


---

Comment by jhpalmieri created at 2008-12-09 18:02:08

Changing keywords from "" to "numerical noise, number_field_morphism".


---

Attachment

Fine by me.


---

Comment by mabshoff created at 2008-12-10 07:25:44

This patch needs to be rebased:

```
sage-3.2.2.alpha1/devel/sage$ patch -p1 < trac_4720.patch 
patching file sage/rings/number_field/number_field_morphisms.pyx
Hunk #1 FAILED at 221.
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/number_field/number_field_morphisms.pyx.rej
```

I will look into it.

Cheers,

Michael


---

Attachment

rebased version of John's patch


---

Comment by mabshoff created at 2008-12-10 09:19:16

Resolution: fixed


---

Comment by mabshoff created at 2008-12-10 09:19:16

Merged trac_4720.patch in Sage 3.2.2.alpha1.

Note that trac_4276-nf-coerce-fixes3.patch renamed closest_root to matching_root which cause the merge trouble.

Cheers,

Michael
