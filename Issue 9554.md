# Issue 9554: Doctest failure in SageNB's sageinspect.py with #8988

Issue created by migration from https://trac.sagemath.org/ticket/9554

Original creator: mpatel

Original creation time: 2010-07-20 08:55:02

Assignee: jason, was

CC:  davidloeffler novoselt vbraun timdumol

This happens with the patches at #8988, which I've merged in the forthcoming 4.5.2.alpha0:

```
$ ./sage -t -long  local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py
sage -t -long "local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py"
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.1-rm/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py", line 997:
    sage: sage_getvariablename(A)
Expected:
    ['A', 'B']
Got:
    ['B', 'A']
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_22
***Test Failed*** 1 failures.
```



---

Comment by vbraun created at 2010-07-20 13:28:45

Can you double-check that you applied `trac_8988-sageinspect_doctest_fix.patch` from #8988? That patch was supposed to fix precisely this issue. In fact, there are 3 patches in #8988, see http://trac.sagemath.org/sage_trac/ticket/8988#comment:42


---

Comment by mpatel created at 2010-07-21 00:30:43

I've applied the 3 patches mentioned in #8988 [comment:ticket:8988:42 comment 42].  The failure above is in the _notebook's_ `sageinspect.py` file, which is very similar to the Sage library's version.

Of course, we should try to reconcile the two files, to the extent it's permitted by SageNB's status as an independent project.  I believe we've been updating them together when one changes, in order to keep both current.


---

Comment by mpatel created at 2010-07-21 00:32:39

I can make the SageNB patch a bit later this week and try to ensure it's merged into 4.5.2.alphaX.


---

Attachment

SageNB repo patch - logically same as http://trac.sagemath.org/sage_trac/attachment/ticket/8988/trac_8988-sageinspect_doctest_fix.patch


---

Comment by leif created at 2010-07-22 15:49:45

Please excuse if my upload violates any rules regarding Sage-SageNB collaboration...

The patch is almost the same as the one to the Sage library here: http://trac.sagemath.org/sage_trac/attachment/ticket/8988/trac_8988-sageinspect_doctest_fix.patch

I've built a SageNB 0.8.1.p1 spkg, installed it on 4.5.2.alpha0, and `./sage -t -long -sagenb` passed all tests.

(I'm not going to upload the patched spkg though, it's almost 19MB. So if appropriate, someone else has to provide it on sage.math.)

-Leif


---

Comment by leif created at 2010-07-22 15:49:45

Changing status from new to needs_review.


---

Comment by leif created at 2010-07-22 16:07:54

P.S.:

```sh
leif@portland:~/Sage/spkgs/sagenb-0.8.1.p1/src/sagenb$ hg status
? sagenb/sagenb.po
```

(This is of course in vanilla 0.8.1, too.)


---

Comment by ddrake created at 2010-07-23 02:26:49

Replying to [comment:1 vbraun]:
> Can you double-check that you applied `trac_8988-sageinspect_doctest_fix.patch` from #8988? That patch was supposed to fix precisely this issue. In fact, there are 3 patches in #8988, see http://trac.sagemath.org/sage_trac/ticket/8988#comment:42

All three patches were merged in 4.5.2.alpha0 -- changesets 14652-4.


---

Comment by vbraun created at 2010-07-23 04:49:30

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2010-07-23 04:49:30

Yes, as mpatel already pointed out, the problematic doctest is in `sagenb/misc/sageinspect.py` and not in `sage/misc/sageinspect.py` (sage*nb* vs. sage). The latter is fixed by the patch in #8988, and the former is fixed by leif's `trac_9554-fix_order_of_var_names-SageNB-repo.patch`. Both patches make identical changes to code that is duplicated in the notebook spkg. 

Since the patch is clearly the right thing to do I'll give it a positive review. Whoever does the next SageNB release, please add this patch. The tracker bug for SageNB 0.8.2 is #9572 where this patch is already listed.


---

Comment by mpatel created at 2010-07-23 06:28:59

Replying to [comment:5 leif]:
> P.S.:
> {{{
> #!sh
> leif`@`portland:~/Sage/spkgs/sagenb-0.8.1.p1/src/sagenb$ hg status
> ? sagenb/sagenb.po
> }}}
> (This is of course in vanilla 0.8.1, too.)

This is now #9580.


---

Comment by mpatel created at 2010-07-23 07:19:29

Resolution: fixed


---

Comment by mpatel created at 2010-07-23 07:19:29

I've merged the patch into SageNB 0.8.2, which awaits review at #9572.


---

Comment by mpatel created at 2010-07-23 07:22:07

Replying to [comment:4 leif]:
> (I'm not going to upload the patched spkg though, it's almost 19MB. So if appropriate, someone else has to provide it on sage.math.)

Do you have a Sage cluster (i.e., sage.math, boxen.math, etc.) account?  If not, William Stein can make one for you.
