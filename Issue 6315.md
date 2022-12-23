# Issue 6315: optional doctest failure -- caused by mistakes in lectures on number theory rst book

Issue created by migration from https://trac.sagemath.org/ticket/6315

Original creator: was

Original creation time: 2009-06-16 14:44:11

Assignee: tbd


```
sage -t -long --optional devel/sage/doc/en/bordeaux_2008/birds_other.rst
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/bordeaux_2008/birds_other.rst", line 243:
    sage: magma.eval(s)     #optional - magma
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[12]>", line 1, in <module>
        magma.eval(s)     #optional - magma###line 243:
    sage: magma.eval(s)     #optional - magma
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 471, in eval
        raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    RuntimeError: Error evaluating Magma code.
    IN:time v := [_sage_[3] * _sage_[4] for _ in [1..10^5]];
    OUT:
    >> time v := [_sage_[3] * _sage_[4] for _ in [1..10^5]];
                                        ^
    User error: bad syntax
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/bordeaux_2008/birds_other.rst", line 265:
    sage: magma.eval(s) #optional - magma
Expected:
    'Time: 1.480'
Got:
    'Time: 0.210'
**********************************************************************
2 items had failures:
   1 of  14 in __main__.example_6
   1 of   9 in __main__.example_7
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_birds_other.py
```



---

Attachment


---

Comment by mariah created at 2011-05-25 17:33:58

[attachment:trac_6315.patch] fixes the "bad syntax" error.  However I do not know what to do about the difference between the Expected time and the Got time.  Timings will be dependent on the computer system.  With the patch, I currently get:


```
eno% ./sage -t -long --optional devel/sage/doc/en/bordeaux_2008/birds_other.rst
sage -t -long --optional "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
**********************************************************************
File "/home/mariah/sage/sage-4.7.rc4-x86_64-Linux-core2-fc-work-magma/devel/sage/doc/en/bordeaux_2008/birds_other.rst", line 244:
    sage: magma.eval(s)     #optional - magma
Expected:
    'Time: 17.120'
Got:
    'Time: 3.560'
**********************************************************************
File "/home/mariah/sage/sage-4.7.rc4-x86_64-Linux-core2-fc-work-magma/devel/sage/doc/en/bordeaux_2008/birds_other.rst", line 266:
    sage: magma.eval(s) #optional - magma
Expected:
    'Time: 1.480'
Got:
    'Time: 0.200'
**********************************************************************
2 items had failures:
```


William - what do you want done?


---

Comment by mariah created at 2011-05-25 17:33:58

Changing status from new to needs_info.


---

Comment by mstreng created at 2011-06-29 14:37:27

Replying to [comment:1 mariah]:
> [...] I do not know what to do about the difference between the Expected time and the Got time.  Timings will be dependent on the computer system.


Why not just append "`, random output`" to "`#optional - magma`"? That way, the output is ignored, just like the timings in this rst file that don't use magma.

Are the authors of the book aware of this error?


---

Attachment

Replying to [comment:2 mstreng]:
> Are the authors of the book aware of this error?

The authors "= me" is aware now.  I've posted a part2 patch that puts ...'s in for the timings, explains that the doctest is showing the reader *how* to compare timings with Magma (which is good to know how to do easily), and remarks that in fact the timings may change over time.


---

Comment by was created at 2011-08-23 08:10:37

Changing status from needs_info to needs_review.


---

Comment by mstreng created at 2011-08-23 08:29:20

Changing status from needs_review to positive_review.


---

Comment by was created at 2011-08-24 23:46:04

Changing keywords from "" to "sd32".


---

Comment by leif created at 2011-09-12 19:41:56

Resolution: fixed
