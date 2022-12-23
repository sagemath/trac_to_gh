# Issue 7652: Adds Linear Programming to the Constructions document

Issue created by migration from https://trac.sagemath.org/ticket/7652

Original creator: ncohen

Original creation time: 2009-12-10 14:54:54

Assignee: mvngu

CC:  mvngu

Following Minh's idea from #6765, here is the first version of this document.

This patch documents the small improvement from #7637 (which is hence needed by the docstrings)


---

Comment by wdj created at 2009-12-10 20:49:25

I have not applied this but only read the patch file.

Comments on the English grammar:


```
10	A linear program is the sum of two information : 
```

should read

```
10	A linear program consists of the following two pieces of information : 
```

I'm not an expert on complexity theory, but I think

```
29	is usually `NP`-Complete (= it can take exponential time, according to a  
30	widely-spread belief that `P\neq NP`) 
```

is not precisely correct as stated it it? Perhaps better would be


```
29	is usually `NP`-Complete (if `P\neq NP` then there is not polynomial time 30      algorithm solving a general MILP problem) 
```


Sorry, I don't understand this beginning of a sentence:

```
82	Can be written (quite naturally, I hope !) this way :: 
```



---

Comment by mvngu created at 2009-12-11 13:58:27

Changing status from new to needs_review.


---

Attachment

I have attached a reviewer patch `trac_7652-reviewer.patch` that includes the following changes:

 * some typo fixes
 * proper ReST formatting

Once my patch is given some thumbs up, then patches should be applied in this order:

 1. `trac_7652.patch`
 1. `trac_7652-reviewer.patch`


---

Comment by mvngu created at 2009-12-12 01:16:25

reviewer patch


---

Attachment

New reviewer patch attached, which needs some reviewing. Note that the patch `trac_7652.patch` results in the following doctest failures:

```
[mvngu@sage sage-4.3.alpha1-7652-linear]$ ./sage -t -long devel/sage-main/doc/en/constructions/linear_programming.rst 
sage -t -long "devel/sage-main/doc/en/constructions/linear_programming.rst"
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/devel/sage-main/doc/en/constructions/linear_programming.rst", line 112:
    sage: p.set_objective( p["first unique variable"] + B[2] + p[-3] )
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[4]>", line 1, in <module>
        p.set_objective( p["first unique variable"] + B[Integer(2)] + p[-Integer(3)] )###line 112:
    sage: p.set_objective( p["first unique variable"] + B[2] + p[-3] )
    AttributeError: MixedIntegerLinearProgram instance has no attribute '__getitem__'
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/devel/sage-main/doc/en/constructions/linear_programming.rst", line 134:
    sage: print x_sol
Expected:
    {1: 0.83333333333333337, 2: 0.0}
Got:
    {1: None, 2: None}
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_2
   1 of   9 in __main__.example_3
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_linear_programming.py
	 [2.1 s]
exit code: 1024
```

My reviewer patch resolves the second failure, but I'm unable to resolve the first one. Help wanted.


---

Comment by ncohen created at 2009-12-12 09:16:45

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-12-12 09:16:45

Even when you think there is an error somewhere, your patches are perfect Minh !!! This example failed because of the patch #7637 mentioned in the description of the TRAC ticket, which is a small and recent improvement made for Martin Albrecht who needed something of the kind :-)

Once this patch is applied, yours is too, and there is no error in the docstrings, with or without the -optional flag... Positive review ! Thank you for your help again ! :-)

Nathann


---

Comment by mhansen created at 2009-12-14 16:08:06

Resolution: fixed
