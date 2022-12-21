# Issue 4952: modulus issue in sage/rings/finite_field_ntl_gf2e.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-07 17:08:47

Assignee: was

The following was introduced by #4934:

```
cleo (ia64-Linux-rhel5-clisp-2.41)

**********************************************************************
File "/home/mariah/sage/sage-3.2.3-ia64-Linux-rhel5-clisp-2.41/devel/sage/sage/rings/finite_field_ntl_gf2e.pyx",
line 171:
    sage: k.modulus()
Expected:
    x^17 + x^16 + x^15 + x^10 + x^8 + x^6 + x^4 + x^3 + x^2 + x + 1
Got:
    x^17 + x^3 + 1
**********************************************************************

eno (x86_64-Linux-fc)

**********************************************************************
File "/home/mariah/sage/sage-3.2.3-x86_64-Linux-fc/devel/sage/sage/rings/finite_field_ntl_gf2e.pyx",
line 171:
    sage: k.modulus()
Expected:
    x^17 + x^16 + x^15 + x^10 + x^8 + x^6 + x^4 + x^3 + x^2 + x + 1
Got:
    x^17 + x^3 + 1
**********************************************************************
```



---

Comment by mabshoff created at 2009-02-10 05:53:12

I am no longer seeing this with the system compiler in 3.3.alpha6, but will try with gcc 4.3.3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-10 07:37:19

The issue has been fixed (or at least no longer happens) with Sage 3.3.alpha6 with the system gcc as well as gcc 4.3.3:

```
mabshoff`@`menas:~/build-3.3.alpha6/sage-3.3.alpha6-menas-gcc433> ./sage -t -long devel/sage/sage/rings/finite_field_ntl_gf2e.pyx
sage -t -long "devel/sage/sage/rings/finite_field_ntl_gf2e.pyx"
	 [5.2 s]
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-02-10 07:37:19

Resolution: fixed


---

Comment by mabshoff created at 2009-02-10 07:38:26

Hmm, to be 100% save I will also test eno and cleo with 3.3.rc0 using gcc 4.3.3.

Cheers,

Michael
