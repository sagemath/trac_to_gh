# Issue 6303: sage-4.0.2.rc0 test failure

Issue created by migration from https://trac.sagemath.org/ticket/6303

Original creator: was

Original creation time: 2009-06-15 17:04:45

Assignee: tbd


```
Built fine, 2 test failyres on 32-bit Suse:  the singular.pyx issue
already reported, and

**********************************************************************
File "/local/jec/sage-4.0.2.rc0/devel/sage/sage/rings/number_field/number_field_element.pyx",
line 2092:
   sage: [L(6).valuation(P) for P in L.primes_above(6)]
Expected:
   [2, 2, 4]
Got:
   [4, 2, 2]
**********************************************************************

That is on old issue: L.primes_above(6) tries to sort the primes but
```



---

Comment by cremona created at 2009-06-15 17:08:45

A patch is on its way...

John


---

Comment by cremona created at 2009-06-15 19:02:34

Applies to 4.0.2.rc0


---

Attachment

As I said on sage-devel, this patch does two things: (1) fix the doctest so it does not depend on the ordering of primes_above() output; (2) fix primes_above to it (partially) orders its output as its docstring describes.


---

Comment by ncalexan created at 2009-06-15 19:39:01

Good for me on sage.math and OS X 10.5.


---

Comment by jsp created at 2009-06-15 19:55:21

Note that this failure was reported on 32 bit linux. So I don't see it is any good to report it good for sage.math or OS X 10.5.


```
sage -t  "devel/sage/sage/rings/number_field/number_field_element.pyx"
	 [24.4 s]
 
----------------------------------------------------------------------
All tests passed!
```


On Fedora 9, 32 bit.

So also a positive review from here.

Jaap


---

Comment by cremona created at 2009-06-15 20:15:11

Thanks Jaap -- I did test my patch on both 32-bit and 64-bit linuxes!


---

Comment by jsp created at 2009-06-15 20:35:04

Sure John, I didn't expect less :-)!

Jaap


---

Comment by was created at 2009-06-15 23:56:39

merged into 4.0.2.rc1


---

Comment by was created at 2009-06-15 23:56:39

Resolution: fixed


---

Comment by was created at 2009-06-16 00:01:57

Actually this patch breaks several doctests in `devel/sage/sage/schemes/elliptic_curves/ell_number_field.py`.


---

Comment by was created at 2009-06-16 00:01:57

Changing status from closed to reopened.


---

Comment by was created at 2009-06-16 00:01:57

Resolution changed from fixed to 


---

Comment by craigcitro created at 2009-06-16 07:14:46

The failures in `ell_number_field.py` are just coming from the new sort order for the `primes_above` method. I'm attaching a second patch which fixes these doctests.


---

Comment by craigcitro created at 2009-06-16 07:41:00

Unfortunately, the output order varies from system to system. So the second patch above won't help ... deleting it now.


---

Comment by cremona created at 2009-06-16 08:16:22

Apologies sine it was my "trivial" patch which caused the problems.  The whole point of the ordering of the output of ideals_above was to make it machine-independent!  Hence by dismay when I saw that my earlier code had been removed - -perhaps by someone who noted that it was not perfect yet.  I'm working on it!


---

Attachment

Actually, I just tried this again on two different machines (32 bit OSX and sage.math), and it seems to work fine with the second patch. (Nick tried this on 32 bit OSX and had trouble, but I can't reproduce that.) If someone gets this to fail, let me know what arch/OS.


---

Comment by cremona created at 2009-06-16 08:57:55

Applied both patches ok to 4.0.2.rc0, all tests pass in both elliptic_curves and number_fields directories, on both 32 and 64 bit linux.


---

Comment by craigcitro created at 2009-06-17 23:55:45

Resolution: fixed
