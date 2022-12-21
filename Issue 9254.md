# Issue 9254: A collection of little improvements to BSD.py

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2010-06-17 18:28:22

Assignee: cremona

These are some of the things I did while working on my thesis.

Depends on #9253, which depends on #9247. Still needs work, since there is now the following error, which is very mysterious to me:


```
sage -t  "devel/sage-main/sage/schemes/elliptic_curves/BSD.py"
**********************************************************************
File "/Users/rlmill/sage-4.4.4.alpha0/devel/sage-main/sage/schemes/elliptic_curves/BSD.py", line 371:
    sage: E.prove_BSD(verbosity=2)
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.4.4.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[21]>", line 1, in <module>
        E.prove_BSD(verbosity=Integer(2))###line 371:
    sage: E.prove_BSD(verbosity=2)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/BSD.py", line 538, in prove_BSD
        I = BSD.curve.heegner_index(D)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/heegner.py", line 6464, in heegner_index
        reg = F.regulator(descent_second_limit=descent_second_limit, verbose=verbose_mwrank)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 2095, in regulator
        G = self.gens(proof=proof, use_database=use_database, descent_second_limit=descent_second_limit, verbose=verbose)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 1934, in gens
        G = C.gens()
      File "/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/libs/mwrank/interface.py", line 595, in gens
        return eval(preparse(self.__two_descent_data().getbasis().replace(":",",")))
    RuntimeError
**********************************************************************
```



---

Comment by rlm created at 2010-06-17 18:29:50

Also, this should be specifically tested on something like `t2` before it gets merged to make sure the timing issues are still fixed.


---

Comment by rlm created at 2010-06-17 18:30:08

Changing status from new to needs_work.


---

Comment by rlm created at 2010-07-18 06:32:58

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-07-18 08:11:36

See also #9535


---

Comment by was created at 2010-07-21 15:59:53

On t2:


```
sage -t  "devel/sage-main/sage/schemes/elliptic_curves/BSD.py"
         [225.4 s]
```


Oh yeah.


---

Comment by was created at 2010-07-21 15:59:53

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-08 08:45:45

I get a long doctest failure on t2 and sage.math:

```python
sage -t -long "devel/sage/sage/schemes/elliptic_curves/BSD.py"
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2-fin/devel/sage/sage/schemes/elliptic_curves/BSD.py", line 383:
    sage: E.prove_BSD(verbosity=2)               # long time
Expected:
    p = 2: True by 2-descent...
    True for p not in {2, 3} by Kolyvagin....
    ALERT: p = 3 left in Kolyvagin bound
        0 <= ord_p(#Sha) <= 2
        ord_p(#Sha_an) = 2
    Remaining primes:
    p = 3: irreducible, surjective, non-split multiplicative
        (0 <= ord_p <= 2)
    [3]
Got:
    p = 2: True by 2-descent
    True for p not in {2, 3} by Kolyvagin.
    Remaining primes:
    p = 3: irreducible, surjective, non-split multiplicative
        (0 <= ord_p <= 2)
        ord_p(#Sha_an) = 2
    [3]
**********************************************************************
1 items had failures:
   1 of  36 in __main__.example_6
***Test Failed*** 1 failures.
```

I'm using 4.5.2 + #9476 + #9247 + #9253 + #9254.  The failure first appears with this ticket.


---

Comment by mpatel created at 2010-08-08 08:45:45

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by rlm created at 2010-08-09 05:52:20

Updated patch fixes the long doctest failure.


---

Comment by rlm created at 2010-08-09 05:52:20

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-08-09 08:50:46

The test now passes on t2 and sage.math.  I'm not a subject expect, but since there are no new technical changes to review, I'm changing the status back to "positive."


---

Comment by mpatel created at 2010-08-09 08:50:46

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-09 09:50:39

Resolution: fixed
