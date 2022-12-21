# Issue 6159: Implement real_part for CDF and CC

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-05-30 15:46:42

Assignee: somebody


```
sage: CC(I).real_part()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/jason/.sage/temp/littleone/9440/_home_jason__sage_init_sage_0.py in <module>()

AttributeError: 'sage.rings.complex_number.ComplexNumber' object has no attribute 'real_part'


sage: CDF(I).real_part()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/jason/.sage/temp/littleone/9440/_home_jason__sage_init_sage_0.py in <module>()

AttributeError: 'sage.rings.complex_double.ComplexDoubleElement' object has no attribute 'real_part'
```


but 


```
sage: (3+I).real_part()
3

```



---

Comment by AlexGhitza created at 2009-07-13 14:02:52

Done in the attached patch.  I even threw in imag_part() for free.


---

Attachment


---

Comment by AlexGhitza created at 2009-07-13 14:03:33

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-07-13 14:03:33

Changing assignee from somebody to AlexGhitza.


---

Comment by burcin created at 2009-07-17 14:08:18

Looks good.


---

Comment by mvngu created at 2009-07-18 13:17:20

After a first merge of the patch `trac_6159.patch` and running full doctests on the Sage library, I got this failure:

```
sage -t -long devel/sage-exp/sage/modules/vector_double_dense.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-exp/sage/modules/vector_double_dense.pyx", line 656:
    sage: v.stats_kurtosis()
Expected:
    -1.23
Got:
    doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?
    -1.23
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_29
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_vector_double_dense.py
	 [2.6 s]
```

I then unmerged that patch, and all doctests passed. As another attempt, I merged `trac_6159.patch` a second time, ran all doctests in the Sage library, and they passed.


---

Comment by mvngu created at 2009-07-18 13:24:44

Resolution: fixed
