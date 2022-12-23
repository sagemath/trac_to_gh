# Issue 5423: Move calculus to new coercion model

Issue created by migration from https://trac.sagemath.org/ticket/5423

Original creator: robertwb

Original creation time: 2009-03-03 09:23:07

Assignee: robertwb




---

Attachment


---

Attachment


---

Comment by mhansen created at 2009-03-07 22:02:05

I've uploaded trac_5423.patch which is the original patch rebased against 3.4.rc1.


---

Comment by jason created at 2009-03-24 21:45:10

mhansen: did you review trac_5423.patch while you did the rebase?


---

Comment by was created at 2009-04-12 05:03:28

The following doctests fail after applying the rebased patch:

```
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/misc/citation.pyx", line 56:
    sage: get_systems('integrate(x^2, x)')
Expected:
    ['Maxima']
Got:
    ['MPFI', 'MPFR', 'Maxima']
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_0
***Test Failed*** 1 failures.
```


and

```
sage -t  devel/sage/sage/rings/complex_interval.pyx
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/rings/complex_interval.pyx", line 456:
    sage: sage_input(ComplexIntervalField(64)(2)^I, preparse=False, verify=True)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[3]>", line 1, in <module>
        sage_input(ComplexIntervalField(Integer(64))(Integer(2))**I, preparse=False, verify=True)###line 456:
    sage: sage_input(ComplexIntervalField(64)(2)^I, preparse=False, verify=True)
      File "complex_interval.pyx", line 432, in sage.rings.complex_interval.ComplexIntervalFieldElement.__pow__ (sage/rings/complex_interval.c:6298)
        return (self.log() * right).exp()
      File "element.pyx", line 1154, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10558)
      File "coerce.pyx", line 740, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7168)
    TypeError: unsupported operand parent(s) for '*': 'Complex Interval Field with 64 bits of precision' and 'Symbolic Ring'
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_14
```


Otherwise, this looks very good. 

The above is against sage-3.4.1.rc2.


---

Comment by robertwb created at 2009-05-18 21:51:23

Made obsolete by the Pynac switch.


---

Comment by mabshoff created at 2009-05-18 22:01:44

Resolution: invalid
