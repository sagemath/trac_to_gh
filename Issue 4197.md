# Issue 4197: weird ntl finite field modulus caching bug.

Issue created by migration from https://trac.sagemath.org/ticket/4197

Original creator: was

Original creation time: 2008-09-25 23:33:46

Assignee: somebody

CC:  robertwb

I thought we slayed this, but on eno we have this weird failure:


```
sage -t -long devel/sage/sage/rings/finite_field_ntl_gf2e.pyx**********************************************************************
File "/home/wstein/eno/build/sage-3.1.3.alpha1/tmp/finite_field_ntl_gf2e.py",
line 167:
   sage: k.modulus()
Expected:
   x^1024 + x^19 + x^6 + x + 1
Got:
   x^1024 + x^16 + x^15 + x^14 + x^13 + x^11 + x^10 + x^9 + x^7 + x^6 + x^2
**********************************************************************
1 items had failures:
  1 of  10 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file
/home/wstein/eno/build/sage-3.1.3.alpha1/tmp/.doctest_finite_field_ntl_gf2e.py
        [1.2 s]

This machine is:
[wstein@eno eno]$ cat /etc/issue
Fedora release 8 (Werewolf)
Kernel \r on an \m

[wstein@eno eno]$ uname -a
Linux eno 2.6.24.5-85.fc8 #1 SMP Sat Apr 19 11:18:09 EDT 2008 x86_64
x86_64 x86_64 GNU/Linux
```



---

Attachment


---

Comment by was created at 2008-09-25 23:37:24

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-09-26 00:32:15

Patch looks good to me. Positive review.

We ought to check why weakref all the sudden is causing those failures. Maybe Cython is involved?

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 00:34:40

Oops, now it gets picked up by the reports.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 04:12:23

Resolution: fixed


---

Comment by mabshoff created at 2008-09-26 04:12:23

Merged in Sage 3.1.3.alpha2
