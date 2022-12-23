# Issue 8453: Update PARI to 2.3.5

Issue created by migration from https://trac.sagemath.org/ticket/8453

Original creator: mhansen

Original creation time: 2010-03-06 06:21:58

Assignee: tbd

CC:  cremona

There is an spkg at http://sage.math.washington.edu/home/mhansen/pari-2.3.5.spkg


---

Attachment


---

Comment by mhansen created at 2010-03-06 06:23:08

Changing status from new to needs_review.


---

Comment by cremona created at 2010-03-06 11:53:05

Mike, I will give this a try.  Unfortunately I have not been able to build 4.3.3 on my 64-bit machine (it builds but thousands of tests fail) so I'll be limited to testing on a 32-bit.

Can we try to collect from other tickets problems which have been attributed to bugs in the pari library, to see if this upgrade fixes them?  If so, there ought tobe appropriate doctests to prove it, and cross-referencing the other tickets, which might therefore be closed.


---

Comment by cremona created at 2010-03-06 13:46:13

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-03-06 13:46:13

Successfully installed the new spkg and patch on 4.3.4.alpha0 on a 32-bit ubuntu machine.  Tested all library (-long) and found a few failures which should be easy to fix (especially the last one!):

```
sage -t -long sage/functions/transcendental.py
**********************************************************************
File "/home/john/sage-4.3.4.alpha0/devel/sage-pari/sage/functions/transcendental.py", line 78:
    sage: w = exponential_integral_1(2,4); w
Expected:
    [0.048900510708061118, 0.003779352409848905, 0.00036008245216265542, 3.7665622843921715e-05] 
Got:
    [0.048900510708061118, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843924751e-05]
```


```
**********************************************************************
File "/home/john/sage-4.3.4.alpha0/devel/sage-pari/sage/functions/special.py", line 1456:
    sage: exp_int(6)
Expected:
    doctest:...: DeprecationWarning: The method expint() is deprecated. Use -Ei(-x) or exponential_integral_1(x) as needed instead.
    0.000360082452162655
Got:
    doctest:1: DeprecationWarning: The method expint() is deprecated. Use -Ei(-x) or exponential_integral_1(x) as needed instead.
    0.000360082452162659
```


```
**********************************************************************
File "/home/john/sage-4.3.4.alpha0/devel/sage-pari/sage/libs/pari/gen.pyx", line 7848:
    sage: E.ellwp(1, flag=2)
Expected:
    [14.2992028590818 + 1.140149682 E-18*I, 50.0619300880073 + 1.040834085 E-17*I] 
Got:
    [14.2992028590818 + 0.E-18*I, 50.0619300880073 - 3.469446952 E-18*I]
```


```
**********************************************************************
File "/home/john/sage-4.3.4.alpha0/devel/sage-pari/sage/interfaces/gp.py", line 476:
    sage: gp.version()
Expected:
    ((2, 3, 3), 'GP/PARI CALCULATOR Version 2.3.3 (released)')
Got:
    ((2, 3, 5), 'GP/PARI CALCULATOR Version 2.3.5 (released)')
```



---

Attachment

apply over previous patch


---

Comment by davidloeffler created at 2010-03-11 19:55:11

I have added a second patch which changes the doctests mentioned above. They should now pass on both 64-bit and 32-bit (the latter using the output John got above). I've also put in a doctest to confirm that #8415 is fixed. 

John, can you double-check that it now works on 32-bit? I've marked it as "needs review" for now, but if that passes, I think we can give it a positive review (and mark #8415 as fixed as well). Sadly, #7736 is still broken.

David


---

Comment by davidloeffler created at 2010-03-11 19:55:11

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-03-11 20:13:41

Replying to [comment:4 davidloeffler]:
> I have added a second patch which changes the doctests mentioned above. They should now pass on both 64-bit and 32-bit (the latter using the output John got above). I've also put in a doctest to confirm that #8415 is fixed. 

Excellent

> 
> John, can you double-check that it now works on 32-bit? I've marked it as "needs review" for now, but if that passes, I think we can give it a positive review (and mark #8415 as fixed as well). Sadly, #7736 is still broken.

OK, testing now....

> 
> David


---

Comment by cremona created at 2010-03-11 21:07:35

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-03-11 21:07:35

All pass on 32-bit.


---

Comment by davidloeffler created at 2010-03-18 17:54:25

FWIW: I've just checked and it *does* build and run OK on Solaris, by the way. I haven't done a full doctest run because that would take a looong time; but I tested a selection of relevant files including sage/rings/number_field, sage/functions/transcendental and sage/libs/pari/gen and they all seem to pass.


---

Comment by was created at 2010-04-28 19:32:51

Resolution: fixed


---

Comment by mvngu created at 2010-04-29 06:13:28

Since Pari is now upgraded to 2.3.5, we no longer need ticket #7979 for patching Pari 2.3.3. That ticket concerns the case where Pari 2.3.3 sometimes ignores the build option "--graphic=none". However, the file `config/get_fltk` in Pari 2.3.5 has the same logic as in Pari 2.3.3 so it's possible that Pari 2.3.5 also ignores the build option "--graphic=none". If that issue comes up, open another ticket to patch Pari 2.3.5 for Sage.
