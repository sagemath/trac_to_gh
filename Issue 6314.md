# Issue 6314: optional doctest failure -- many failures in linear_codes related to wtdist

Issue created by migration from https://trac.sagemath.org/ticket/6314

Original creator: was

Original creation time: 2009-06-16 14:43:05

Assignee: tbd


```
sage -t -long --optional devel/sage/sage/coding/linear_code.py
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/lib/gap-4.4.10/pkg/guava3.6/bin/leon/wtdist: not found
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/lib/gap-4.4.10/pkg/guava3.6/bin/leon/wtdist: not found
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/lib/gap-4.4.10/pkg/guava3.6/bin/leon/wtdist: not found
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/coding/linear_code.py", line 2188:
    sage: C.spectrum(method="leon")   # requires optional GAP package Guava
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_44[10]>", line 1, in <module>
        C.spectrum(method="leon")   # requires optional GAP package Guava###line 2188:
    sage: C.spectrum(method="leon")   # requires optional GAP package Guava
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 2236, in spectrum
        raise RuntimeError("Problem calling Leon's wtdist program.")
    RuntimeError: Problem calling Leon's wtdist program.
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/coding/linear_code.py", line 2196:
    sage: C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_44[14]>", line 1, in <module>
        C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava###line 2196:
    sage: C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 2236, in spectrum
        raise RuntimeError("Problem calling Leon's wtdist program.")
    RuntimeError: Problem calling Leon's wtdist program.
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/coding/linear_code.py", line 2200:
    sage: C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_44[16]>", line 1, in <module>
        C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava###line 2200sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/lib/gap-4.4.10/pkg/guava3.6/bin/leon/wtdist: not found
:
    sage: C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 2236, in spectrum
        raise RuntimeError("Problem calling Leon's wtdist program.")
    RuntimeError: Problem calling Leon's wtdist program.
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/coding/linear_code.py", line 2204:
    sage: C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_44[18]>", line 1, in <module>
        C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava###line 2204:
    sage: C.spectrum() == C.spectrum(method="leon")   # requires optional GAP package Guava
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 2236, in spectrum
        raise RuntimeError("Problem calling Leon's wtdist program.")
    RuntimeError: Problem calling Leon's wtdist program.
**********************************************************************
1 items had failures:
   4 of  19 in __main__.example_44
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_linear_code.py
	 [22.0 s]
```



---

Attachment

applies to 4.0.2.rc1


---

Comment by wdj created at 2009-06-16 23:46:25

Patch applies fine to 4.0.2.rc1 and passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds 
sage -docbuild constructions html (resp., pdf) went fine and sage -t -long --optional devel/sage/sage/coding/linear_code.py passes.


---

Comment by wdj created at 2009-06-17 23:16:20

From an email:

> You should make a ticket for fixing that problem too and put a link to it from 6314. - William

The guava binaries are now currently being compiled properly due to a problem in the "newest-version gap" script (in the gap_packages*.spkg spkg-install script). This is fixed in http://trac.sagemath.org/sage_trac/ticket/6352.


---

Comment by rlm created at 2009-06-21 12:42:14

This is an easy review- the patch is simple, applies, and tests pass with or without the optional flag.


---

Comment by rlm created at 2009-06-24 09:59:47

Resolution: fixed
