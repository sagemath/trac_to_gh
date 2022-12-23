# Issue 8749: BSD: doctest failures on solaris (t2)

Issue created by migration from https://trac.sagemath.org/ticket/8749

Original creator: jhpalmieri

Original creation time: 2010-04-23 05:15:26

Assignee: cremona

CC:  robertwb rlm

With Sage 4.4.alpha2, I see the following:

```
File "/home/palmieri/t2/sage-4.4.alpha2/devel/sage-main/sage/schemes/elliptic_curves/BSD.py", line\
 304:
    sage: EllipticCurve('11a').prove_BSD(verbosity=2)
Expected:
    p = 2: True by 2-descent
    True for p not in {2, 5} by Kolyvagin.
    True for p=5 by Mazur
    []
Got:
    p = 2: True by 2-descent
    Timeout stopped Heegner index computation...
    Proceeding to use heegner_index_bound instead.
    True for p not in {2, 5} by Kolyvagin.
    True for p=5 by Mazur
    []
**********************************************************************
File "/home/palmieri/t2/sage-4.4.alpha2/devel/sage-main/sage/schemes/elliptic_curves/BSD.py", line\
 377:
    sage: E.prove_BSD(verbosity=2)               # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/palmieri/t2/sage-4.4.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/palmieri/t2/sage-4.4.alpha2/local/bin/sagedoctest.py", line 38, in run_one_examp\
le
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/palmieri/t2/sage-4.4.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_exam\
ple
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[22]>", line 1, in <module>
        E.prove_BSD(verbosity=Integer(2))               # long time###line 377:
    sage: E.prove_BSD(verbosity=2)               # long time
      File "/home/palmieri/t2/sage-4.4.alpha2/local/lib/python/site-packages/sage/schemes/elliptic\
_curves/BSD.py", line 761, in prove_BSD
        raise RuntimeError("p = %d: ord_p_bound == %d, but sha_an.ord(p) == %d. This appears to be\
 a counterexample to BSD, but is more likely a bug."%(p,ord_p_bound,BSD.sha_an.ord(p)))
    RuntimeError: p = 3: ord_p_bound == 1, but sha_an.ord(p) == 2. This appears to be a counterexa\
mple to BSD, but is more likely a bug.
**********************************************************************
1 items had failures:
   2 of  35 in __main__.example_6
***Test Failed*** 2 failures.
```

The first is a timeout issue of some sort, and perhaps could be fixed by putting in some dots `...` in case the timeout message appears.  (I've also seen more failures of this type from the same file, so ellipses in several places might be needed.  Test on t2 several times to see.)

I have no idea about the second issue.  Presumably it's not a counterexample to BSD.


---

Comment by jhpalmieri created at 2010-04-23 17:24:27

Replying to [ticket:8749 jhpalmieri]:
> (I've also seen more failures of this type from the same file, so ellipses in several places might be needed.  Test on t2 several times to see.)

More specifically, I just saw this on lines 304, 310, 336, and 418.


---

Attachment


---

Comment by rlm created at 2010-04-30 01:44:55

Changing status from new to needs_review.


---

Comment by was created at 2010-05-01 06:09:38

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-05-01 06:13:59

Resolution: fixed


---

Comment by was created at 2010-05-01 18:43:43

It turns out this patch works on t2, but fails on *everything* else... due to misuse of ...
The attached patch fixes this by removing a newline in each ...'d test.


---

Attachment

Second patch looks good: positive review.


---

Comment by drkirkby created at 2010-06-03 12:41:26

I don't think this is fixed properly - or if it was, a very similar error is now occurring on the same doctest. See  #9127 

Dave
