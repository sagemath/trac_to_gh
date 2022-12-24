# Issue 1275: [with bundle] implementation of QQbar

archive/issues_001275.json:
```json
{
    "body": "Assignee: cwitty\n\nThe attached qqbar.hg bundle provides an implementation of QQbar (the algebraic closure of the rationals), with an embedding into CC.  (The embedding is built-in, so there's no version without the embedding.)\n\ntestall passes on both 32-bit and 64-bit x86 Linux.\n\nThe bundle requires the new MPFI spkg from #1268, and the patches from #1270 and #1273.\n\nThe bundle contains two patches.  The first has all the actual functionality; the second only handles the file rename from algebraic_real.py to qqbar.py.  I'm going to also attach a copy of this first patch, for review purposes; but it should not be applied separately--apply the bundle instead.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1275\n\n",
    "created_at": "2007-11-25T22:50:06Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with bundle] implementation of QQbar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1275",
    "user": "cwitty"
}
```
Assignee: cwitty

The attached qqbar.hg bundle provides an implementation of QQbar (the algebraic closure of the rationals), with an embedding into CC.  (The embedding is built-in, so there's no version without the embedding.)

testall passes on both 32-bit and 64-bit x86 Linux.

The bundle requires the new MPFI spkg from #1268, and the patches from #1270 and #1273.

The bundle contains two patches.  The first has all the actual functionality; the second only handles the file rename from algebraic_real.py to qqbar.py.  I'm going to also attach a copy of this first patch, for review purposes; but it should not be applied separately--apply the bundle instead.

Issue created by migration from https://trac.sagemath.org/ticket/1275





---

archive/issue_comments_007981.json:
```json
{
    "body": "Attachment [7427-for-review.patch](tarball://root/attachments/some-uuid/ticket1275/7427-for-review.patch) by cwitty created at 2007-11-25 22:51:06",
    "created_at": "2007-11-25T22:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7981",
    "user": "cwitty"
}
```

Attachment [7427-for-review.patch](tarball://root/attachments/some-uuid/ticket1275/7427-for-review.patch) by cwitty created at 2007-11-25 22:51:06



---

archive/issue_comments_007982.json:
```json
{
    "body": "I just read through this code.  \n* the code all looks good to me\n* there is some useful documentation\n* the doctest coverage of new functions isn't 100%, but the important functions have tests; more test should be added\n* I cannot apply the hg bundle: {{{\nsage: hg_sage.pull()\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg pull -u http://www.sagemath.org/hg/sage-main\npulling from http://www.sagemath.org/hg/sage-main\nsearching for changes\nno changes found\nIf it says use 'hg merge' above, then you should\ntype hg_sage.merge().\nsage: hg_sage.heads()\ncd \"/Users/was/s/devel/sage\" && hg head \nchangeset:   7420:b06f58879bb3\ntag:         tip\nparent:      7419:dc8dedef562f\nparent:      7405:ce4aa966e4c1\nuser:        William Stein <wstein`@`gmail.com>\ndate:        Tue Nov 27 05:59:30 2007 -0800\nsummary:     merge\n\nsage: hg_sage.apply('qqbar.hg')\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg status\nUnbundling bundle /Users/was/Downloads/qqbar.hg\nIf you get an error 'abort: unknown parent'\nthis usually means either you need to do:\n       hg_sage.pull()\nor you're applying this patch to the wrong repository.\ncd \"/Users/was/s/devel/sage\" && hg unbundle -u \"/Users/was/Downloads/qqbar.hg\"\nadding changesets\ntransaction abort!\nrollback completed\nabort: unknown parent 40eaefca4b52!\n}}}\n* I can't apply the plain text patch cleanly either: {{{\nsage: hg_sage.apply('7427-for-review.patch')\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg import   \"/Users/was/Downloads/7427-for-review.patch\"\napplying /Users/was/Downloads/7427-for-review.patch\npatching file sage/rings/complex_field.py\nHunk #1 FAILED at 25\n1 out of 2 hunks FAILED -- saving rejects to file sage/rings/complex_field.py.rej\nabort: patch failed to apply\n}}}",
    "created_at": "2007-11-27T14:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7982",
    "user": "was"
}
```

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

archive/issue_comments_007983.json:
```json
{
    "body": "I just read through this code.  \n* the code all looks good to me\n* there is some useful documentation\n* the doctest coverage of new functions isn't 100%, but the important functions have tests; more test should be added\n* I cannot apply the hg bundle: \n\n```\nsage: hg_sage.pull()\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg pull -u http://www.sagemath.org/hg/sage-main\npulling from http://www.sagemath.org/hg/sage-main\nsearching for changes\nno changes found\nIf it says use 'hg merge' above, then you should\ntype hg_sage.merge().\nsage: hg_sage.heads()\ncd \"/Users/was/s/devel/sage\" && hg head \nchangeset:   7420:b06f58879bb3\ntag:         tip\nparent:      7419:dc8dedef562f\nparent:      7405:ce4aa966e4c1\nuser:        William Stein <wstein@gmail.com>\ndate:        Tue Nov 27 05:59:30 2007 -0800\nsummary:     merge\n\nsage: hg_sage.apply('qqbar.hg')\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg status\nUnbundling bundle /Users/was/Downloads/qqbar.hg\nIf you get an error 'abort: unknown parent'\nthis usually means either you need to do:\n       hg_sage.pull()\nor you're applying this patch to the wrong repository.\ncd \"/Users/was/s/devel/sage\" && hg unbundle -u \"/Users/was/Downloads/qqbar.hg\"\nadding changesets\ntransaction abort!\nrollback completed\nabort: unknown parent 40eaefca4b52!\n```\n\n* I can't apply the plain text patch cleanly either: \n\n```\nsage: hg_sage.apply('7427-for-review.patch')\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg import   \"/Users/was/Downloads/7427-for-review.patch\"\napplying /Users/was/Downloads/7427-for-review.patch\npatching file sage/rings/complex_field.py\nHunk #1 FAILED at 25\n1 out of 2 hunks FAILED -- saving rejects to file sage/rings/complex_field.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2007-11-27T14:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7983",
    "user": "was"
}
```

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

archive/issue_comments_007984.json:
```json
{
    "body": "Attachment [qqbar-full.hg](tarball://root/attachments/some-uuid/ticket1275/qqbar-full.hg) by cwitty created at 2007-11-30 03:14:42",
    "created_at": "2007-11-30T03:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7984",
    "user": "cwitty"
}
```

Attachment [qqbar-full.hg](tarball://root/attachments/some-uuid/ticket1275/qqbar-full.hg) by cwitty created at 2007-11-30 03:14:42



---

archive/issue_comments_007985.json:
```json
{
    "body": "OK, I tried to be excessively clever with Mercurial here, and it backfired.  The patch qqbar.hg evidently only works if you start with the exact same version of Sage that I started with, then apply patches from #1270 and #1273 on that version, then apply qqbar.hg.\n\nI've attached qqbar-full.hg, which is a single bundle containing #1270+#1273+qqbar.hg; you should be able to apply this on any sufficiently new version of Sage, instead of requiring the exact same version I had.",
    "created_at": "2007-11-30T03:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7985",
    "user": "cwitty"
}
```

OK, I tried to be excessively clever with Mercurial here, and it backfired.  The patch qqbar.hg evidently only works if you start with the exact same version of Sage that I started with, then apply patches from #1270 and #1273 on that version, then apply qqbar.hg.

I've attached qqbar-full.hg, which is a single bundle containing #1270+#1273+qqbar.hg; you should be able to apply this on any sufficiently new version of Sage, instead of requiring the exact same version I had.



---

archive/issue_comments_007986.json:
```json
{
    "body": "I have been testing/playing with this and read much of the code and it looks very nice. Thanks! \n\nOne thing that looked really out of place to me was the handling of the golden ratio constant. I'm attaching a patch that I would like you to consider as an alternative way of doing it.",
    "created_at": "2007-12-01T02:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7986",
    "user": "robertwb"
}
```

I have been testing/playing with this and read much of the code and it looks very nice. Thanks! 

One thing that looked really out of place to me was the handling of the golden ratio constant. I'm attaching a patch that I would like you to consider as an alternative way of doing it.



---

archive/issue_comments_007987.json:
```json
{
    "body": "Attachment [qqbar-sqrt-golden.patch](tarball://root/attachments/some-uuid/ticket1275/qqbar-sqrt-golden.patch) by robertwb created at 2007-12-01 02:27:29",
    "created_at": "2007-12-01T02:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7987",
    "user": "robertwb"
}
```

Attachment [qqbar-sqrt-golden.patch](tarball://root/attachments/some-uuid/ticket1275/qqbar-sqrt-golden.patch) by robertwb created at 2007-12-01 02:27:29



---

archive/issue_comments_007988.json:
```json
{
    "body": "I merged qqbar-full.hg, but I am waiting for comment on qqbar-sqrt-golden.patch submitted by Robert. \n\nExcellent!\n\nCheers,\n\nMichael",
    "created_at": "2007-12-01T11:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7988",
    "user": "mabshoff"
}
```

I merged qqbar-full.hg, but I am waiting for comment on qqbar-sqrt-golden.patch submitted by Robert. 

Excellent!

Cheers,

Michael



---

archive/issue_comments_007989.json:
```json
{
    "body": "Robert, my golden ratio code has the \"advantage\" that computations like `AA(golden_ratio)^2 - AA(golden_ratio)` are exact:\n\n```\nsage: phi = AA( (1+AA(5).sqrt()) / 2) \nsage: phi^2 - phi\n[0.99999999999999988 .. 1.0000000000000003]\nsage: phi = AA(golden_ratio)\nsage: phi^2 - phi\n1\n```\n\n\nIf you don't think that's useful, then I'm happy to switch the implementation.\n\nI'm puzzled by your new chunk in .argument(); as far as I can tell, it should be redundant.  (Did you upgrade to the MPFI spkg in #1268 before applying #1270?  That version fixes some bugs that cause problems in .argument().  Note that if you apply #1270 and rebuild, then upgrade #1268, it has no effect; if you did things in that order, you would also need to touch mpfi.pxi, like it says in the description for #1268.)\n\nAlso, sqrt() needs a scary warning about branch cuts, along the lines of the warning in argument().  (Now that I look, I see that `__pow__()` is also missing such a warning.)\n\nThanks for the review!",
    "created_at": "2007-12-01T16:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7989",
    "user": "cwitty"
}
```

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

archive/issue_comments_007990.json:
```json
{
    "body": "I wasn't able to install the MPFI spkg, hence the new chunk in argument. If that makes it redundant, than we don't need it. In fact, I thought this is why you did golden_ration the way you did ('cause without the argument \"fix\" the imaginary part was not exactly 0). \n\nI agree both sqrt() and `__pow__()` should refer to the warning and docstring of argument(). \n\nHere is a question. In your way, in your original version, if you do \n\n\n```\nsage: phi = AA(golden_ratio)\nsage: (phi - 1/2)^2\n```\n\n\nis the answer exact? \n\nIn any case, this should definitely get included and we can deal with this issue later.",
    "created_at": "2007-12-01T21:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7990",
    "user": "robertwb"
}
```

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

archive/issue_comments_007991.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T05:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7991",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007992.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-02T05:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7992",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha2.



---

archive/issue_comments_007993.json:
```json
{
    "body": "The two main parts of Robert's patch/comment have been split out as #1363 and #1365, and the actual implementation of qqbar was applied in 2.8.15.alpha0.",
    "created_at": "2007-12-02T05:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1275#issuecomment-7993",
    "user": "cwitty"
}
```

The two main parts of Robert's patch/comment have been split out as #1363 and #1365, and the actual implementation of qqbar was applied in 2.8.15.alpha0.
