# Issue 6330: optional doctest failure -- constructions number fields doctest failures

Issue created by migration from https://trac.sagemath.org/ticket/6330

Original creator: was

Original creation time: 2009-06-16 15:07:43

Assignee: tbd


```
sage -t -long --optional devel/sage/doc/en/constructions/number_fields.rst
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/number_fields.rst", line 33:
    sage: [(k.degree(), k.disc()) for k in J.unramified_outside([2])] # requires optional database
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[2]>", line 1, in <module>
        [(k.degree(), k.disc()) for k in J.unramified_outside([Integer(2)])] # requires optional database###line 33:
    sage: [(k.degree(), k.disc()) for k in J.unramified_outside([2])] # requires optional database
    NameError: name 'J' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/number_fields.rst", line 42:
    sage: [k.disc() for k in J.unramified_outside([2],2)] # requires optional database
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        [k.disc() for k in J.unramified_outside([Integer(2)],Integer(2))] # requires optional database###line 42:
    sage: [k.disc() for k in J.unramified_outside([2],2)] # requires optional database
    NameError: name 'J' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/number_fields.rst", line 50:
    sage: [k.disc() for k in J.ramified_at([3,5],3)] # requires optional database
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        [k.disc() for k in J.ramified_at([Integer(3),Integer(5)],Integer(3))] # requires optional database###line 50:
    sage: [k.disc() for k in J.ramified_at([3,5],3)] # requires optional database
    NameError: name 'J' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/number_fields.rst", line 63:
    sage: J.ramified_at(101)                     # requires optional database
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[2]>", line 1, in <module>
        J.ramified_at(Integer(101))                     # requires optional database###line 63:
    sage: J.ramified_at(101)                     # requires optional database
    NameError: name 'J' is not defined
**********************************************************************
4 items had failures:
   1 of   3 in __main__.example_1
   1 of   3 in __main__.example_2
   1 of   6 in __main__.example_3
   1 of   3 in __main__.example_4
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3
```



---

Comment by jhpalmieri created at 2009-06-16 19:13:35

I put in some `.. link` directives so that "J" would remain defined from one set of examples to the next.  I also had to reorder a list.


---

Attachment


---

Comment by wdj created at 2009-06-16 23:12:01

Patch applies fine to 4.0.2.rc1 and passes sage -tp 1
 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds sage -docbuild
 constructions html (resp., pdf) went fine.


---

Comment by rlm created at 2009-06-24 10:00:21

Resolution: fixed
