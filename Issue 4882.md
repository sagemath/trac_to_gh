# Issue 4882: ./sage -t sage/sage/rings/polynomial/multi_polynomial_ideal.py M2 failure

Issue created by migration from https://trac.sagemath.org/ticket/4882

Original creator: jsp

Original creation time: 2008-12-26 17:39:31

Assignee: tbd

On Fedora 9, 32 bits:


```
sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 58:
    sage: S.<a,b> = R.quotient((x^2 + y^2, 17))
Expected:
    verbose 0 ... Warning: falling back to very slow toy implementation.
Got nothing
**********************************************************************
1 items had failures:
   1 of  47 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/jaap/downloads/sage-3.2.2/tmp/.doctest_multi_polynomial_ideal.py
	 [44.6 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
Total time for all tests: 44.6 seconds

```



Jaap


---

Comment by mabshoff created at 2008-12-26 17:49:42

Changing assignee from tbd to mabshoff.


---

Comment by mabshoff created at 2008-12-26 17:49:42

Changing component from algebra to doctest.


---

Comment by mabshoff created at 2008-12-26 17:49:42

Changing status from new to assigned.


---

Attachment


---

Comment by jsp created at 2008-12-26 18:55:17

After the patch:



```
sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 65:
    sage: a^2 + b^2 == 0
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[16]>", line 1, in <module>
        a**Integer(2) + b**Integer(2) == Integer(0)###line 65:
    sage: a^2 + b^2 == 0
    NameError: name 'a' is not defined
**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 67:
    sage: a^3 - b^2
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[17]>", line 1, in <module>
        a**Integer(3) - b**Integer(2)###line 67:
    sage: a^3 - b^2
    NameError: name 'a' is not defined
**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 69:
    sage: (a+b)^17
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[18]>", line 1, in <module>
        (a+b)**Integer(17)###line 69:
    sage: (a+b)^17
    NameError: name 'a' is not defined
**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 71:
    sage: S(17) == 0
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[19]>", line 1, in <module>
        S(Integer(17)) == Integer(0)###line 71:
    sage: S(17) == 0
    NameError: name 'S' is not defined
**********************************************************************
1 items had failures:
   4 of  45 in __main__.example_0
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/jaap/downloads/sage-3.2.2/tmp/.doctest_multi_polynomial_ideal.py
	 [12.6 s]
exit code: 1024
 

```


Needs work

Jaap


---

Comment by mabshoff created at 2008-12-26 19:13:25

Oops, my bad, A patch on top of that is coming up once sage.math is running again.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-12-26 22:27:36

Jaap,

a second patch to be applied on top of the other patch is up and should fix the issues. It even passes doctests now on my test box ;)

Cheers,

Michael


---

Comment by jsp created at 2008-12-26 22:39:49

Now:

```
sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
	 [39.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 39.8 seconds

```


Cheers,

Jaap


---

Comment by mabshoff created at 2008-12-26 22:45:45

Merged both patches in Sage 3.2.3.final


---

Comment by mabshoff created at 2008-12-26 22:45:45

Resolution: fixed
