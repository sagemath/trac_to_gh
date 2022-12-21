# Issue 3762: remove quaddouble from sage -- not used, source of pain, mpfr is better

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-02 20:16:11

Assignee: mabshoff

CC:  cwitty

Note -- also close #3079.

I wonder -- should quaddouble should be moved to be an optional spkg?  That will be weird, since the actual support for quaddouble is all over the sage install (in all the coercions code, etc.). 


---

Comment by was created at 2008-08-02 21:27:20


```

My real_roots.pyx uses a couple of functions from quaddouble:
fpu_fix_start and fpu_fix_end.  (partitions_c.cc also uses these
functions.)  These are found in the quaddouble source in src/fpu.cpp
and include/fpu.h

Probably the right fix is to copy only those two files into c_lib/.  I
can do that, but I'll need some help with configuration.  (The main
thing is that the files want a preprocessor symbol X86 to be defined
iff we're using an x86-family processor.)

Carl
```



---

Attachment

adds a test code wrapper for sage


---

Attachment

makes qd dependance of partitions optional


---

Comment by robertwb created at 2009-01-22 09:49:11

I removed the quad-double dependancy from the partitions counting code, but there seems to be a significant speed regression :(.


---

Attachment


---

Attachment

This removes all sage dependancies on quaddouble, but leaves it in to be deprecated for a while. 

Some issues that need to be dealt with are (1) the speed regression in partitions and (2) whether the fix for real_roots would better be extracting fpu_fix from the qd autoconf script. Perhaps if qd is present, we could detect it and compile the above with the qd routines.


---

Comment by was created at 2009-01-24 02:50:08

1. I applied this to sage-3.3.alpha1 on sage.math and got:

```
The following tests failed:

        sage -t  devel/sage/sage/rings/complex_field.py # 1 doctests failed
        sage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 164.0 seconds
wstein`@`sage:/scratch/wstein/sage-3.3.alpha1$  
```


We have:

```
sage -t  devel/sage/sage/structure/sage_object.pyx**********************************************************************
File "/scratch/wstein/sage-3.3.alpha1/devel/sage-main/sage/structure/sage_object.pyx", line 682:
    sage: sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data i
n a more recent format.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data 
in a more recent format.
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Successfully unpickled 448 objects.
    Failed to unpickle 0 objects.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_16
***Test Failed*** 1 failures.

sage -t  devel/sage/sage/rings/complex_field.py
**********************************************************************
File "/scratch/wstein/sage-3.3.alpha1/devel/sage-main/sage/rings/complex_field.py", line 105:
    sage: C(RR.log2(), RR.e())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[7]>", line 1, in <module>
        C(RR.log2(), RR.e())###line 105:
    sage: C(RR.log2(), RR.e())
    AttributeError: 'sage.rings.real_mpfr.RealField' object has no attribute 'e'
**********************************************************************
1 items had failures:

```




2. Performance on sage.math:

```
BEFORE:
sage: time k = number_of_partitions(10^8)
CPU times: user 2.48 s, sys: 0.00 s, total: 2.48 s
Wall time: 2.49 s
sage: time k = number_of_partitions(10^9)
CPU times: user 22.85 s, sys: 0.00 s, total: 22.85 s
Wall time: 22.85 s


AFTER:
sage: time k = number_of_partitions(10^8)
CPU times: user 3.29 s, sys: 0.00 s, total: 3.29 s
Wall time: 3.29 s
sage: time k = number_of_partitions(10^9)
CPU times: user 35.68 s, sys: 0.00 s, total: 35.68 s
Wall time: 35.71 s
```


3. I read all the code in the patches, and am fine with it. 

Positive review if the two doctest issues above are fixed. 

NOTE: you should not delete the quaddouble package, since this code still links it in.  That will have to happen in a few months after Deprecation.


---

Attachment


---

Comment by robertwb created at 2009-01-24 03:10:01

Attach all 5 patches in order. 

Followup for speed regression at #5084 and fpu_fix at #5085.


---

Comment by mabshoff created at 2009-01-28 13:48:38

Merged all five patches in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 13:48:38

Resolution: fixed
