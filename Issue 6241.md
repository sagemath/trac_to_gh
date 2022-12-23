# Issue 6241: numerical noise (very easy to fix) on cicero (redhat 9) i686 32-bit

Issue created by migration from https://trac.sagemath.org/ticket/6241

Original creator: was

Original creation time: 2009-06-07 13:35:32

Assignee: was

Notice the 7 real part instead of 6 below:


```
Please see /home/wstein/build/cicero/sage-4.0.1/tmp/test.log for the complete log from this test.
[wstein@cicero sage-4.0.1]$ ./sage -t  "devel/sage/sage/rings/number_field/number_field.py"
sage -t  "devel/sage/sage/rings/number_field/number_field.py"
**********************************************************************
File "/home/wstein/build/cicero/sage-4.0.1/devel/sage/sage/rings/number_field/number_field.py", line 7295:
    sage: e = K.embeddings(CC)[0]; e
Expected:
    Ring morphism:
    From: Number Field in a with defining polynomial x^3 - 2
    To:   Complex Field with 53 bits of precision
    Defn: a |--> -0.629960524947436 - 1.09112363597172*I
Got:
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Field with 53 bits of precision
      Defn: a |--> -0.629960524947437 - 1.09112363597172*I

  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
**********************************************************************
1 items had failures:
   1 of  19 in __main__.example_180
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/build/cicero/sage-4.0.1/tmp/.doctest_number_field.py
         [37.9 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/rings/number_field/number_field.py"
Total time for all tests: 37.9 seconds
[wstein@cicero sage-4.0.1]$ cat /etc/issue
Fedora release 9 (Sulphur)
Kernel \r on an \m (\l)

```



---

Comment by was created at 2009-06-15 23:50:12

this is already merged into 4.0.2.rc1, but needs to be reviewed.  it's pretty trivial.


---

Attachment


---

Comment by craigcitro created at 2009-06-16 05:20:23

Yep, I can give that a positive review.


---

Comment by craigcitro created at 2009-06-16 05:20:57

Resolution: fixed
