# Issue 4453: elliptic curves -- heegner_index command gives nonsense when rank > 1

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-11-06 14:47:03

Assignee: was

For any elliptic curve over QQ of rank >= 2 the heegner_index command must always give 0 as output.   So the following 1 at the end is just wrong.


```
sage: E = EllipticCurve('389a')
sage: D = E.heegner_discriminants_list(1)[0]
sage: D
-7
sage: E.heegner_index(D)
1
```



---

Comment by davidloeffler created at 2009-07-20 19:49:42

Changing component from number theory to elliptic curves.


---

Comment by davidloeffler created at 2009-07-20 19:49:42

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-10-09 09:14:05

Remove assignee davidloeffler.


---

Comment by was created at 2010-01-18 04:35:21

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-01-20 10:18:55

Depends on #6616?


---

Comment by cremona created at 2010-01-31 17:31:36

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-01-31 17:31:36

Positive review: looks good (apart from a docstring typo "We higher rank examples") and applies fine to 4.3.1, tests pass and docs build & look good.

I added a new patch which changes the above to "Some higher rank examples" with no further changes.


---

Comment by mvngu created at 2010-02-13 05:59:54

I get two hunk failures when applying [trac_4453.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4453/trac_4453.2.patch) on top of Sage 4.3.3.alpha0:

```
[mvngu`@`sage sage-main]$ pwd
/dev/shm/mvngu/sage-4.3.3.alpha0/devel/sage-main
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4453/trac_4453.2.patch && hg qpush
adding trac_4453.2.patch to series file
applying trac_4453.2.patch
patching file sage/schemes/elliptic_curves/heegner.py
Hunk #3 FAILED at 6350
Hunk #4 succeeded at 6370 with fuzz 2 (offset -12 lines).
Hunk #5 FAILED at 6430
2 out of 5 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/heegner.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_4453.2.patch
```

The attachment [trac_4453.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4453/trac_4453.2.patch) needs rebase against Sage 4.3.3.alpha0.


---

Comment by mvngu created at 2010-02-13 05:59:54

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by robertwb created at 2010-07-29 06:03:24

Rebased, I also fixed a small error when check_rank=False.


---

Comment by robertwb created at 2010-07-29 06:03:24

Changing status from needs_work to positive_review.


---

Comment by mpatel created at 2010-08-07 09:58:31

With the forthcoming 4.5.2 (4.5.2.rc0 + #9226) and the rebased patch, I get a doctest failure:

```python
sage -t -long "devel/sage/sage/schemes/elliptic_curves/heegner.py"
**********************************************************************
File "/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 6465:
    sage: E.heegner_index(-8, descent_second_limit=16)
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_229[14]>", line 1, in <module>
        E.heegner_index(-Integer(8), descent_second_limit=Integer(16))###line 6465: 
    sage: E.heegner_index(-8, descent_second_limit=16)
      File "/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/lib/python/site-packages/sage/schemes/elliptic_curves/heegner.py", line 6485, in heegner_index
        if check_rank and self.rank() >= 2:
      File "/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 1741, in rank
        raise RuntimeError, 'Rank not provably correct.'
    RuntimeError: Rank not provably correct.
**********************************************************************
1 items had failures:
   1 of  21 in __main__.example_229
***Test Failed*** 1 failures.
```



---

Comment by mpatel created at 2010-08-07 09:58:31

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-08-07 10:00:11

Replying to [comment:8 mpatel]:
> With the forthcoming 4.5.2 (4.5.2.rc0 + #9226) and the rebased patch, I get a doctest failure:

That should be "4.5.2 (4.5.2.rc1 + #9226)".


---

Comment by zimmerma created at 2011-09-15 16:06:01

this patch still applies fine to 4.7.1, and the new examples in the patch seem to work.
However the description says that the following should give 0 and not `+Infinity`:

```
sage: E = EllipticCurve('389a')
sage: E.heegner_index(-7)
+Infinity
```

Is the description wrong?

Paul


---

Comment by zimmerma created at 2011-09-15 16:06:01

Changing status from needs_work to needs_info.


---

Comment by robertwb created at 2011-09-15 23:25:22

The description is wrong, the Heegner point is torsion for rank >= 2 curves, hence its index in the full group is infinite.


---

Comment by zimmerma created at 2011-09-16 06:26:01

thanks Robert. Is the new description ok? I put back as "needs review" to check if the doctests
pass.

Paul


---

Comment by zimmerma created at 2011-09-16 06:26:01

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2011-09-16 09:06:57

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2011-09-16 09:06:57

the failure mentioned in comment [comment:8] is still there:

```
sage: E = EllipticCurve([0, 0, 1, -34874, -2506691])
sage: E.heegner_index(-8, descent_second_limit=16)
...
RuntimeError: Rank not provably correct.
```

thus this ticket needs work.

Paul


---

Attachment

Apply trac_4453-rebased.patch, 4453-doctest-fix.patch


---

Comment by robertwb created at 2012-10-24 07:22:12

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2012-10-24 07:23:16

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2012-10-24 07:27:15

Robert, I find it strange that you give a positive review to your own patch...

Paul


---

Comment by robertwb created at 2012-10-24 07:30:59

I was giving a positive review to the original patch; I suppose someone should review my 1-line doctest fix as well.


---

Comment by robertwb created at 2012-10-24 07:30:59

Changing status from positive_review to needs_work.


---

Comment by robertwb created at 2012-10-24 07:31:06

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2012-10-24 08:31:23

I'll check Robert's one-liner but not this week.


---

Comment by davidloeffler created at 2012-10-24 09:12:39

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2012-10-24 09:12:39

Rob's patch looks fine to me, and patchbot's happy with it, so let's get this in.


---

Comment by jdemeyer created at 2012-10-30 16:10:18

Please specify which patch(es) to apply.


---

Comment by jdemeyer created at 2012-10-30 16:10:18

Changing status from positive_review to needs_info.


---

Comment by robertwb created at 2012-10-30 17:27:52

Changing status from needs_info to needs_review.


---

Comment by robertwb created at 2012-10-30 17:28:06

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-11-01 12:01:54

Resolution: fixed
