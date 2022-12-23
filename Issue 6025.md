# Issue 6025: Sage 3.4.2: doctest failure in sage/libs/pari/gen.pyx on 64 bit OSX

Issue created by migration from https://trac.sagemath.org/ticket/6025

Original creator: mabshoff

Original creation time: 2009-05-12 07:10:05

Assignee: mabshoff


```
sage -t -long "devel/sage/sage/libs/pari/gen.pyx"           
**********************************************************************
File "/Users/mabshoff/sage-3.4.2-64/devel/sage/sage/libs/pari/gen.pyx", line 8945:
    sage: pari.finitefield_init(7,2)
Exception raised:
    Traceback (most recent call last):
      File "/Users/mabshoff/sage-3.4.2-64/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mabshoff/sage-3.4.2-64/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mabshoff/sage-3.4.2-64/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_291[4]>", line 1, in <module>
        pari.finitefield_init(Integer(7),Integer(2))###line 8945:
    sage: pari.finitefield_init(7,2)
    RuntimeError
**********************************************************************
File "/Users/mabshoff/sage-3.4.2-64/devel/sage/sage/libs/pari/gen.pyx", line 8950:
    sage: pari.finitefield_init(2,3)
Exception raised:
    Traceback (most recent call last):
      File "/Users/mabshoff/sage-3.4.2-64/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mabshoff/sage-3.4.2-64/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mabshoff/sage-3.4.2-64/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_291[5]>", line 1, in <module>
        pari.finitefield_init(Integer(2),Integer(3))###line 8950:
    sage: pari.finitefield_init(2,3)
    RuntimeError
**********************************************************************
1 items had failures:
   2 of   6 in __main__.example_291
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/mabshoff/sage-3.4.2-64/tmp/.doctest_gen.py
	 [19.0 s]
```



---

Attachment

As William pointed out on the mailing list, this code isn't used anywhere -- so we're just killing the function. The problem is that on 64 bit OSX, a value getting returned loses its top 4 bytes. This is clearly weird, but since this pari function is known to be buggy, we'll just not use it for now and cross our fingers.


---

Comment by mabshoff created at 2009-05-13 17:42:54

Ok, good to go.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-13 18:00:57

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-13 18:00:57

Resolution: fixed
