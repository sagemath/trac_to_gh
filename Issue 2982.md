# Issue 2982: Itanium (RHEL 5) -- weird problem in code_construction.py

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-21 03:23:24

Assignee: mabshoff


```
sage -t  devel/sage/sage/coding/code_constructions.py       **********************************************************************
File "/home/wstein/sage-3.0.rc0/tmp/code_constructions.py", line 1121:
    sage: C.minimum_distance()
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[4]>", line 1, in <module>
        C.minimum_distance()###line 1121:
    sage: C.minimum_distance()
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 1269, in minimum_distance
        return hamming_weight(min_wt_vec(Gstr,F))
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 243, in min_wt_vec
        c = [gfq_gap_to_sage(cg[j],F) for j in range(1,n+1)]
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 778, in gfq_gap_to_sage
        K = FiniteField(q, F.variable_name())
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/rings/finite_field.py", line 240, in FiniteField
        raise ValueError, "order of finite field must be a prime power"
    ValueError: order of finite field must be a prime power
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_22
***Test Failed*** 1 failures.
```



---

Comment by mabshoff created at 2008-04-21 04:34:22

This will be fixed by #2984.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-21 06:54:49

Resolution: fixed


---

Comment by mabshoff created at 2008-04-21 06:54:49

Fixed by merging #2984.
