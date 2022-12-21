# Issue 2201: [with patch, needs review] doctest failure on 2.10.2.alpha0: number_field.py

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-02-18 01:24:56

Assignee: craigcitro

CC:  jsp

Jaap reported the following doctest failure on sage-devel:


```
jaap`@`paix sage-2.10.2.alpha0]$ ./sage -t  devel/sage-main/sage/rings/number_field/number_field.py
sage -t  devel/sage-main/sage/rings/number_field/number_field.py**********************************************************************
File "number_field.py", line 2087:
    sage: F.reduced_basis()
Expected:
    [1, alpha, alpha^2 - 15*alpha + 1, alpha^3 - 16*alpha^2 + 469*alpha + 267109]
Got:
    [1, alpha, alpha^2 - 15*alpha, alpha^3 - 16*alpha^2 + 469*alpha + 267109]
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_60
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_number_field.py
         [33.8 s]
exit code: 256
```


This is due to different precision getting used to compute an embedding somewhere -- the fix was to add an optional `prec` argument, which is useful in its own right, and then make the doctests call with a specific precision. 


---

Attachment


---

Comment by craigcitro created at 2008-02-18 01:26:12

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-02-18 01:26:12

I just realized that this patch is against 2.10.1 + patches from 1085 -- I don't think this should cause any trouble, since it only touches one file, but if it does, I'll rebase it.


---

Comment by jsp created at 2008-02-18 11:43:20

Couldn't apply the patch tos sage-2.10.2.alpha.

Jaap


---

Comment by jsp created at 2008-02-18 12:49:39

Just applied the patch by hand and it works:


```

[jaap`@`paix sage-2.10.2.alpha0]$ ./sage -t  devel/sage-main/sage/rings/number_field/number_field.py
sage -t  devel/sage-main/sage/rings/number_field/number_field.py
         [21.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 21.3 seconds

```



---

Comment by mabshoff created at 2008-02-18 13:34:28

Resolution: fixed


---

Comment by mabshoff created at 2008-02-18 13:34:28

Merged in Sage 2.10.2.alpha1


---

Comment by mabshoff created at 2008-02-18 17:04:47

FYI: This patch fixes the doctest issue on sage.math, too.

Cheers,

Michael
