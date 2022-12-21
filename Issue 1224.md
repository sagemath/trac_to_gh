# Issue 1224: OSX 10.4 PPC failure in sage/rings/finite_field_ntl_gf2e.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-20 22:54:21

Assignee: malb


```
michael-abshoffs-ibook-g4:~/Desktop/sage-2.8.13.rc0 mabshoff$ ./sage -
t  devel/sage-main/sage/rings/finite_field_ntl_gf2e.pyx
sage -t  devel/sage-main/sage/rings/
finite_field_ntl_gf2e.pyx**********************************************************************
File "finite_field_ntl_gf2e.pyx", line 978:
    sage: int(a)
Expected:
    2
Got:
    33554432
**********************************************************************
File "finite_field_ntl_gf2e.pyx", line 980:
    sage: int(a^2 + 1)
Expected:
    5
Got:
    83886080
**********************************************************************
1 items had failures:
   2 of   3 in __main__.example_41
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_finite_field_ntl_gf2e.pyx
         [11.1 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/rings/finite_field_ntl_gf2e.pyx
Total time for all tests: 11.1 seconds
```



---

Comment by cwitty created at 2007-11-21 00:13:22

These are endianness problems (big-endian vs. little-endian): 83886080 is 0x05000000.


---

Comment by malb created at 2007-11-21 15:17:26

next attempt, patch updated


---

Attachment

Merged in 2.8.13.rc2.


---

Comment by mabshoff created at 2007-11-21 15:26:08

Resolution: fixed
