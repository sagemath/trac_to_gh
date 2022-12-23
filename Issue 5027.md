# Issue 5027: doctest failure for rings/polynomial/toy_d_basis.py

Issue created by migration from https://trac.sagemath.org/ticket/5027

Original creator: mhampton

Original creation time: 2009-01-19 16:13:02

Assignee: tbd

Keywords: groebner, toy, toy_d_basis

I get this failure on an intel mac:


```
sage -t  "devel/sage/sage/rings/polynomial/toy_d_basis.py"
**********************************************************************
File ".../devel/sage/sage/rings/polynomial/toy_d_basis.py", line 91:
    sage: d_basis(I)
Expected:
    [x + 170269749119, y + 2149906854, z + 735710619426, 282687803443]
Got:
    [x + 170269749119, y + 2149906854, z + 170335012540, 282687803443]
********************************************************************** 
```



---

Comment by mabshoff created at 2009-02-04 14:14:38

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-04 14:14:38

After chatting with malb we decided to dot out the constant since it is the same GBasis.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-04 14:14:38

Changing assignee from tbd to mabshoff.


---

Attachment


---

Comment by jsp created at 2009-02-05 15:09:14

After applying the patch:


```
sage -t  "devel/sage/sage/rings/polynomial/toy_d_basis.py"  
	 [9.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 9.5 seconds
[jaap@paix sage-3.3.alpha4]$ 

```


On fedora 9, 32 bits.

Jaap


---

Comment by mabshoff created at 2009-02-05 23:40:29

Merged in Sage 3.3.alpha6.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-05 23:40:29

Resolution: fixed
