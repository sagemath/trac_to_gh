# Issue 3288: linear_code -- memory errors in doctests -- need to be marked #long or otherwise fixed

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-23 17:33:26

Assignee: rlm

On a machine with arch linux and 1GB RAM:

```
sage -t  devel/sage/sage/coding/linear_code.py              **********************************************************************
File "/home/was/build/sage-3.0.2.rc0/tmp/linear_code.py", line 402:
    sage: for B in self_orthogonal_binary_codes(7,3):
       print B
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[1]>", line 1, in <module>
        for B in self_orthogonal_binary_codes(Integer(7),Integer(3)):###line 402:
    sage: for B in self_orthogonal_binary_codes(7,3):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 477, in self_orthogonal_binary_codes
        for N in self_orthogonal_binary_codes(n, k, d, M, BC, in_test=in_test):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 486, in self_orthogonal_binary_codes
        for child in BC.generate_children(BinaryCode(parent), nn, d):
      File "binary_code.pyx", line 3797, in sage.coding.binary_code.BinaryCodeClassifier.generate_children (sage/coding/binary_code.c:24498)
    MemoryError
**********************************************************************
File "/home/was/build/sage-3.0.2.rc0/tmp/linear_code.py", line 415:
    sage: for B in self_orthogonal_binary_codes(7,3,4):
       print B; print B.gen_mat()
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[2]>", line 1, in <module>
        for B in self_orthogonal_binary_codes(Integer(7),Integer(3),Integer(4)):###line 415:
    sage: for B in self_orthogonal_binary_codes(7,3,4):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 477, in self_orthogonal_binary_codes
        for N in self_orthogonal_binary_codes(n, k, d, M, BC, in_test=in_test):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 486, in self_orthogonal_binary_codes
        for child in BC.generate_children(BinaryCode(parent), nn, d):
      File "binary_code.pyx", line 3797, in sage.coding.binary_code.BinaryCodeClassifier.generate_children (sage/coding/binary_code.c:24498)
    MemoryError
**********************************************************************
File "/home/was/build/sage-3.0.2.rc0/tmp/linear_code.py", line 429:
    sage: for B in self_orthogonal_binary_codes(7,2,4):
       print B; print B.gen_mat()
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[3]>", line 1, in <module>
        for B in self_orthogonal_binary_codes(Integer(7),Integer(2),Integer(4)):###line 429:
    sage: for B in self_orthogonal_binary_codes(7,2,4):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 477, in self_orthogonal_binary_codes
        for N in self_orthogonal_binary_codes(n, k, d, M, BC, in_test=in_test):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 486, in self_orthogonal_binary_codes
        for child in BC.generate_children(BinaryCode(parent), nn, d):
      File "binary_code.pyx", line 3797, in sage.coding.binary_code.BinaryCodeClassifier.generate_children (sage/coding/binary_code.c:24498)
    MemoryError
**********************************************************************
File "/home/was/build/sage-3.0.2.rc0/tmp/linear_code.py", line 439:
    sage: for B in self_orthogonal_binary_codes(8, 4, equal=True):
        print B; print B.gen_mat()
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[4]>", line 1, in <module>
        for B in self_orthogonal_binary_codes(Integer(8), Integer(4), equal=True):###line 439:
    sage: for B in self_orthogonal_binary_codes(8, 4, equal=True):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 477, in self_orthogonal_binary_codes
        for N in self_orthogonal_binary_codes(n, k, d, M, BC, in_test=in_test):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 486, in self_orthogonal_binary_codes
        for child in BC.generate_children(BinaryCode(parent), nn, d):
      File "binary_code.pyx", line 3797, in sage.coding.binary_code.BinaryCodeClassifier.generate_children (sage/coding/binary_code.c:24498)
    MemoryError
**********************************************************************
1 items had failures:
   4 of   6 in __main__.example_6
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/was/build/sage-3.0.2.rc0/tmp/.doctest_linear_code.py
```



---

Comment by mabshoff created at 2008-05-24 00:14:11

According to top none of the coding style doctests use more than 400MB of RAM on a 64 bit box, so I am assuming this is caused by the issues from #3289 and #3285.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-24 00:57:58

This is not fixed by applying the patch from #3285 - I am valgrinding now.

Cheers,

Michael


---

Attachment

oops!


---

Comment by mabshoff created at 2008-05-24 01:57:39

The patch is the correct fix. On the affected box doctests now pass:

```
sage -t -long devel/sage/sage/coding/all.py
         [1.9 s]
sage -t -long devel/sage/sage/coding/binary_code.pyx
         [12.9 s]
sage -t -long devel/sage/sage/coding/code_bounds.py
         [3.7 s]
sage -t -long devel/sage/sage/coding/code_constructions.py
         [7.0 s]
sage -t -long devel/sage/sage/coding/guava.py
         [2.9 s]
sage -t -long devel/sage/sage/coding/linear_code.py
         [24.5 s]
sage -t -long devel/sage/sage/coding/sd_codes.py
         [1.9 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 54.8 seconds
```


Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-24 01:59:06

Resolution: fixed


---

Comment by mabshoff created at 2008-05-24 01:59:06

Merged in Sage 3.0.2.rc3
