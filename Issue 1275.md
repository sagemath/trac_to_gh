# Issue 1275: [with bundle] implementation of QQbar

Issue created by migration from https://trac.sagemath.org/ticket/1275

Original creator: cwitty

Original creation time: 2007-11-25 22:50:06

Assignee: cwitty

The attached qqbar.hg bundle provides an implementation of QQbar (the algebraic closure of the rationals), with an embedding into CC.  (The embedding is built-in, so there's no version without the embedding.)

testall passes on both 32-bit and 64-bit x86 Linux.

The bundle requires the new MPFI spkg from #1268, and the patches from #1270 and #1273.

The bundle contains two patches.  The first has all the actual functionality; the second only handles the file rename from algebraic_real.py to qqbar.py.  I'm going to also attach a copy of this first patch, for review purposes; but it should not be applied separately--apply the bundle instead.


---

Attachment


---

Comment by was created at 2007-11-27 14:05:34

I just read through this code.  
   * the code all looks good to me
   * there is some useful documentation
   * the doctest coverage of new functions isn't 100%, but the important functions have tests; more test should be added
   * I cannot apply the hg bundle: {{{
sage: hg_sage.pull()
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg pull -u http://www.sagemath.org/hg/sage-main
pulling from http://www.sagemath.org/hg/sage-main
searching for changes
no changes found
If it says use 'hg merge' above, then you should
type hg_sage.merge().
sage: hg_sage.heads()
cd "/Users/was/s/devel/sage" && hg head 
changeset:   7420:b06f58879bb3
tag:         tip
parent:      7419:dc8dedef562f
parent:      7405:ce4aa966e4c1
user:        William Stein <wstein`@`gmail.com>
date:        Tue Nov 27 05:59:30 2007 -0800
summary:     merge

sage: hg_sage.apply('qqbar.hg')
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg status
Unbundling bundle /Users/was/Downloads/qqbar.hg
If you get an error 'abort: unknown parent'
this usually means either you need to do:
       hg_sage.pull()
or you're applying this patch to the wrong repository.
cd "/Users/was/s/devel/sage" && hg unbundle -u "/Users/was/Downloads/qqbar.hg"
adding changesets
transaction abort!
rollback completed
abort: unknown parent 40eaefca4b52!
}}}
   * I can't apply the plain text patch cleanly either: {{{
sage: hg_sage.apply('7427-for-review.patch')
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg import   "/Users/was/Downloads/7427-for-review.patch"
applying /Users/was/Downloads/7427-for-review.patch
patching file sage/rings/complex_field.py
Hunk #1 FAILED at 25
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/complex_field.py.rej
abort: patch failed to apply
}}}


---

Comment by was created at 2007-11-27 14:06:25

I just read through this code.  
   * the code all looks good to me
   * there is some useful documentation
   * the doctest coverage of new functions isn't 100%, but the important functions have tests; more test should be added
   * I cannot apply the hg bundle: 

```
sage: hg_sage.pull()
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg pull -u http://www.sagemath.org/hg/sage-main
pulling from http://www.sagemath.org/hg/sage-main
searching for changes
no changes found
If it says use 'hg merge' above, then you should
type hg_sage.merge().
sage: hg_sage.heads()
cd "/Users/was/s/devel/sage" && hg head 
changeset:   7420:b06f58879bb3
tag:         tip
parent:      7419:dc8dedef562f
parent:      7405:ce4aa966e4c1
user:        William Stein <wstein@gmail.com>
date:        Tue Nov 27 05:59:30 2007 -0800
summary:     merge

sage: hg_sage.apply('qqbar.hg')
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg status
Unbundling bundle /Users/was/Downloads/qqbar.hg
If you get an error 'abort: unknown parent'
this usually means either you need to do:
       hg_sage.pull()
or you're applying this patch to the wrong repository.
cd "/Users/was/s/devel/sage" && hg unbundle -u "/Users/was/Downloads/qqbar.hg"
adding changesets
transaction abort!
rollback completed
abort: unknown parent 40eaefca4b52!
```

   * I can't apply the plain text patch cleanly either: 

```
sage: hg_sage.apply('7427-for-review.patch')
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg import   "/Users/was/Downloads/7427-for-review.patch"
applying /Users/was/Downloads/7427-for-review.patch
patching file sage/rings/complex_field.py
Hunk #1 FAILED at 25
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/complex_field.py.rej
abort: patch failed to apply
```



---

Attachment


---

Comment by cwitty created at 2007-11-30 03:20:51

OK, I tried to be excessively clever with Mercurial here, and it backfired.  The patch qqbar.hg evidently only works if you start with the exact same version of Sage that I started with, then apply patches from #1270 and #1273 on that version, then apply qqbar.hg.

I've attached qqbar-full.hg, which is a single bundle containing #1270+#1273+qqbar.hg; you should be able to apply this on any sufficiently new version of Sage, instead of requiring the exact same version I had.


---

Comment by robertwb created at 2007-12-01 02:27:03

I have been testing/playing with this and read much of the code and it looks very nice. Thanks! 

One thing that looked really out of place to me was the handling of the golden ratio constant. I'm attaching a patch that I would like you to consider as an alternative way of doing it.


---

Attachment


---

Comment by mabshoff created at 2007-12-01 11:04:37

I merged qqbar-full.hg, but I am waiting for comment on qqbar-sqrt-golden.patch submitted by Robert. 

Excellent!

Cheers,

Michael


---

Comment by cwitty created at 2007-12-01 16:07:53

Robert, my golden ratio code has the "advantage" that computations like `AA(golden_ratio)^2 - AA(golden_ratio)` are exact:

```
sage: phi = AA( (1+AA(5).sqrt()) / 2) 
sage: phi^2 - phi
[0.99999999999999988 .. 1.0000000000000003]
sage: phi = AA(golden_ratio)
sage: phi^2 - phi
1
```


If you don't think that's useful, then I'm happy to switch the implementation.

I'm puzzled by your new chunk in .argument(); as far as I can tell, it should be redundant.  (Did you upgrade to the MPFI spkg in #1268 before applying #1270?  That version fixes some bugs that cause problems in .argument().  Note that if you apply #1270 and rebuild, then upgrade #1268, it has no effect; if you did things in that order, you would also need to touch mpfi.pxi, like it says in the description for #1268.)

Also, sqrt() needs a scary warning about branch cuts, along the lines of the warning in argument().  (Now that I look, I see that `__pow__()` is also missing such a warning.)

Thanks for the review!


---

Comment by robertwb created at 2007-12-01 21:07:29

I wasn't able to install the MPFI spkg, hence the new chunk in argument. If that makes it redundant, than we don't need it. In fact, I thought this is why you did golden_ration the way you did ('cause without the argument "fix" the imaginary part was not exactly 0). 

I agree both sqrt() and `__pow__()` should refer to the warning and docstring of argument(). 

Here is a question. In your way, in your original version, if you do 


```
sage: phi = AA(golden_ratio)
sage: (phi - 1/2)^2
```


is the answer exact? 

In any case, this should definitely get included and we can deal with this issue later.


---

Comment by mabshoff created at 2007-12-02 05:39:09

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 05:39:09

Merged in 2.8.15.alpha2.


---

Comment by cwitty created at 2007-12-02 05:40:11

The two main parts of Robert's patch/comment have been split out as #1363 and #1365, and the actual implementation of qqbar was applied in 2.8.15.alpha0.
