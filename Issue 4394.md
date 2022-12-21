# Issue 4394: Sage 3.1.4: magma related optional doctest failure in sage/rings/polynomial/polynomial_element.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-10-30 16:51:51

Assignee: was


```
mabshoff`@`iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx
sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/polynomial_element.py", line 2833:
    sage: g = magma(f); g              # optional -- requires Magma
Expected:
    y^3 - 17*y + 5
Got:
    $.1^3 - 17*$.1 + 5
**********************************************************************
1 items had failures:
```



---

Attachment


---

Comment by mabshoff created at 2008-10-31 20:21:07

Positive review. The patch makes the doctests pass:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ 
./sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx
sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx
	 [11.4 s]
 
----------------------------------------------------------------------
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 20:21:20

Merged in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-31 20:21:20

Resolution: fixed
