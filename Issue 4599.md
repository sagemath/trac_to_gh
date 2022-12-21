# Issue 4599: sage/schemes/elliptic_curves/ell_rational_field.py doctest failure due to missing "#optional"

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-23 22:12:06

Assignee: mabshoff

Jaap reported:

```
sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
************** ******************************************************** 
File "/home/jaap/downloads/sage-3.2.1.alpha0/devel/sage/sage/schemes/elliptic_cu rves/ell_rational_field.py", line 1183: 
     sage: EllipticCurve('14a1').three_selmer_rank() 
Exception raised: 
[...] 
     TypeError: Unable to start magma because the command 'magma -n' failed. 
********************************************************************** 
1 items had failures: 
    1 of   3 in __main__.example_29 
***Test Failed*** 1 failures. 
For whitespace errors, see the file /home/jaap/downloads/sage-3.2.1.alpha0/tmp/.doctest_ell_rational_field.py 
         [79.8 s] 
```



---

Comment by mabshoff created at 2008-11-23 22:38:54

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-24 23:03:47

Mmh, with #4600 the problem seems to disappear, but I am still posting a patch here.

Cheers,

Michael


---

Attachment

The patch worked for me:



```
[jaap`@`paix sage-3.2.1.alpha0]$ ./sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
	 [86.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 86.9 seconds

```



---

Comment by mabshoff created at 2008-11-24 23:36:20

Thanks Jaap. My previous comment about #4600 fixing this ticket is plain wrong since I did have the real Magma in $PATH.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-24 23:36:35

Merged in Sage 3.2.1.alpha1


---

Comment by mabshoff created at 2008-11-24 23:36:35

Resolution: fixed
