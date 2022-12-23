# Issue 6327: optional doctest failure -- failure using pari C library

Issue created by migration from https://trac.sagemath.org/ticket/6327

Original creator: was

Original creation time: 2009-06-16 15:04:26

Assignee: tbd

What's up with this?


```
sage -t -long --optional devel/sage/sage/libs/pari/gen.pyx
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/libs/pari/gen.pyx", line 5801:
    sage: e.ellpow([0,0], I+1) # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_177[4]>", line 1, in <module>
        e.ellpow([Integer(0),Integer(0)], I+Integer(1)) # optional###line 5801:
    sage: e.ellpow([0,0], I+1) # optional
      File "gen.pyx", line 9170, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44129)
        raise PariError, errno
    PariError: sorry, (15)
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_177
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wst
```



---

Comment by jdemeyer created at 2010-08-01 16:05:44

Changing component from optional packages to packages.


---

Comment by jdemeyer created at 2010-08-01 16:05:44

It means that complex multiplication for elliptic curves is not implemented in PARI/GP.  Like "it would be nice if this would work, but it doesn't".  Not sure what the correct keyword is for that :-)


---

Comment by jdemeyer created at 2010-09-16 21:07:21

Changing keywords from "" to "pari cm curve ellpow".


---

Comment by jdemeyer created at 2010-09-16 21:07:21

Changing component from packages to doctest.


---

Comment by jdemeyer created at 2010-09-16 21:07:21

Changing assignee from tbd to mvngu.


---

Comment by jdemeyer created at 2010-09-17 07:30:51

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-09-17 07:34:34

Changing keywords from "pari cm curve ellpow" to "pari ellpow complex multiplication elliptic curve".


---

Attachment


---

Comment by jdemeyer created at 2010-09-19 11:53:38

Changing component from doctest to elliptic curves.


---

Comment by davidloeffler created at 2010-09-23 12:35:36

Looks good and all doctests pass. See #9977 for a follow-up ticket. (I wonder who will get to open the golden ticket #10000?)


---

Comment by davidloeffler created at 2010-09-23 12:35:36

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-09-23 14:58:37

Replying to [comment:7 davidloeffler]:
> Looks good and all doctests pass. See #9977 for a follow-up ticket. (I wonder who will get to open the golden ticket #10000?)

Thanks for the review and I completely agree with the follow-up ticket.


---

Comment by mpatel created at 2010-09-29 04:24:51

Resolution: fixed
