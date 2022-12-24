# Issue 9554: Doctest failure in SageNB's sageinspect.py with #8988

archive/issues_009554.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  davidloeffler novoselt vbraun timdumol\n\nThis happens with the patches at #8988, which I've merged in the forthcoming 4.5.2.alpha0:\n\n```\n$ ./sage -t -long  local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py\nsage -t -long \"local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.1-rm/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py\", line 997:\n    sage: sage_getvariablename(A)\nExpected:\n    ['A', 'B']\nGot:\n    ['B', 'A']\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_22\n***Test Failed*** 1 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9554\n\n",
    "created_at": "2010-07-20T08:55:02Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "title": "Doctest failure in SageNB's sageinspect.py with #8988",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9554",
    "user": "mpatel"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/9554





---

archive/issue_comments_092087.json:
```json
{
    "body": "Can you double-check that you applied `trac_8988-sageinspect_doctest_fix.patch` from #8988? That patch was supposed to fix precisely this issue. In fact, there are 3 patches in #8988, see http://trac.sagemath.org/sage_trac/ticket/8988#comment:42",
    "created_at": "2010-07-20T13:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92087",
    "user": "vbraun"
}
```

Can you double-check that you applied `trac_8988-sageinspect_doctest_fix.patch` from #8988? That patch was supposed to fix precisely this issue. In fact, there are 3 patches in #8988, see http://trac.sagemath.org/sage_trac/ticket/8988#comment:42



---

archive/issue_comments_092088.json:
```json
{
    "body": "I've applied the 3 patches mentioned in #8988 [comment:ticket:8988:42 comment 42].  The failure above is in the *notebook's* `sageinspect.py` file, which is very similar to the Sage library's version.\n\nOf course, we should try to reconcile the two files, to the extent it's permitted by SageNB's status as an independent project.  I believe we've been updating them together when one changes, in order to keep both current.",
    "created_at": "2010-07-21T00:30:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92088",
    "user": "mpatel"
}
```

I've applied the 3 patches mentioned in #8988 [comment:ticket:8988:42 comment 42].  The failure above is in the *notebook's* `sageinspect.py` file, which is very similar to the Sage library's version.

Of course, we should try to reconcile the two files, to the extent it's permitted by SageNB's status as an independent project.  I believe we've been updating them together when one changes, in order to keep both current.



---

archive/issue_comments_092089.json:
```json
{
    "body": "I can make the SageNB patch a bit later this week and try to ensure it's merged into 4.5.2.alphaX.",
    "created_at": "2010-07-21T00:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92089",
    "user": "mpatel"
}
```

I can make the SageNB patch a bit later this week and try to ensure it's merged into 4.5.2.alphaX.



---

archive/issue_comments_092090.json:
```json
{
    "body": "Attachment [trac_9554-fix_order_of_var_names-SageNB-repo.patch](tarball://root/attachments/some-uuid/ticket9554/trac_9554-fix_order_of_var_names-SageNB-repo.patch) by leif created at 2010-07-22 15:40:42\n\nSageNB repo patch - logically same as http://trac.sagemath.org/sage_trac/attachment/ticket/8988/trac_8988-sageinspect_doctest_fix.patch",
    "created_at": "2010-07-22T15:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92090",
    "user": "leif"
}
```

Attachment [trac_9554-fix_order_of_var_names-SageNB-repo.patch](tarball://root/attachments/some-uuid/ticket9554/trac_9554-fix_order_of_var_names-SageNB-repo.patch) by leif created at 2010-07-22 15:40:42

SageNB repo patch - logically same as http://trac.sagemath.org/sage_trac/attachment/ticket/8988/trac_8988-sageinspect_doctest_fix.patch



---

archive/issue_comments_092091.json:
```json
{
    "body": "Please excuse if my upload violates any rules regarding Sage-SageNB collaboration...\n\nThe patch is almost the same as the one to the Sage library here: http://trac.sagemath.org/sage_trac/attachment/ticket/8988/trac_8988-sageinspect_doctest_fix.patch\n\nI've built a SageNB 0.8.1.p1 spkg, installed it on 4.5.2.alpha0, and `./sage -t -long -sagenb` passed all tests.\n\n(I'm not going to upload the patched spkg though, it's almost 19MB. So if appropriate, someone else has to provide it on sage.math.)\n\n-Leif",
    "created_at": "2010-07-22T15:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92091",
    "user": "leif"
}
```

Please excuse if my upload violates any rules regarding Sage-SageNB collaboration...

The patch is almost the same as the one to the Sage library here: http://trac.sagemath.org/sage_trac/attachment/ticket/8988/trac_8988-sageinspect_doctest_fix.patch

I've built a SageNB 0.8.1.p1 spkg, installed it on 4.5.2.alpha0, and `./sage -t -long -sagenb` passed all tests.

(I'm not going to upload the patched spkg though, it's almost 19MB. So if appropriate, someone else has to provide it on sage.math.)

-Leif



---

archive/issue_comments_092092.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-22T15:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92092",
    "user": "leif"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092093.json:
```json
{
    "body": "P.S.:\n\n```sh\nleif@portland:~/Sage/spkgs/sagenb-0.8.1.p1/src/sagenb$ hg status\n? sagenb/sagenb.po\n```\n\n(This is of course in vanilla 0.8.1, too.)",
    "created_at": "2010-07-22T16:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92093",
    "user": "leif"
}
```

P.S.:

```sh
leif@portland:~/Sage/spkgs/sagenb-0.8.1.p1/src/sagenb$ hg status
? sagenb/sagenb.po
```

(This is of course in vanilla 0.8.1, too.)



---

archive/issue_comments_092094.json:
```json
{
    "body": "Replying to [comment:1 vbraun]:\n> Can you double-check that you applied `trac_8988-sageinspect_doctest_fix.patch` from #8988? That patch was supposed to fix precisely this issue. In fact, there are 3 patches in #8988, see http://trac.sagemath.org/sage_trac/ticket/8988#comment:42\n\nAll three patches were merged in 4.5.2.alpha0 -- changesets 14652-4.",
    "created_at": "2010-07-23T02:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92094",
    "user": "ddrake"
}
```

Replying to [comment:1 vbraun]:
> Can you double-check that you applied `trac_8988-sageinspect_doctest_fix.patch` from #8988? That patch was supposed to fix precisely this issue. In fact, there are 3 patches in #8988, see http://trac.sagemath.org/sage_trac/ticket/8988#comment:42

All three patches were merged in 4.5.2.alpha0 -- changesets 14652-4.



---

archive/issue_comments_092095.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T04:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92095",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092096.json:
```json
{
    "body": "Yes, as mpatel already pointed out, the problematic doctest is in `sagenb/misc/sageinspect.py` and not in `sage/misc/sageinspect.py` (sage**nb** vs. sage). The latter is fixed by the patch in #8988, and the former is fixed by leif's `trac_9554-fix_order_of_var_names-SageNB-repo.patch`. Both patches make identical changes to code that is duplicated in the notebook spkg. \n\nSince the patch is clearly the right thing to do I'll give it a positive review. Whoever does the next SageNB release, please add this patch. The tracker bug for SageNB 0.8.2 is #9572 where this patch is already listed.",
    "created_at": "2010-07-23T04:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92096",
    "user": "vbraun"
}
```

Yes, as mpatel already pointed out, the problematic doctest is in `sagenb/misc/sageinspect.py` and not in `sage/misc/sageinspect.py` (sage**nb** vs. sage). The latter is fixed by the patch in #8988, and the former is fixed by leif's `trac_9554-fix_order_of_var_names-SageNB-repo.patch`. Both patches make identical changes to code that is duplicated in the notebook spkg. 

Since the patch is clearly the right thing to do I'll give it a positive review. Whoever does the next SageNB release, please add this patch. The tracker bug for SageNB 0.8.2 is #9572 where this patch is already listed.



---

archive/issue_comments_092097.json:
```json
{
    "body": "Replying to [comment:5 leif]:\n> P.S.:\n> {{{\n> #!sh\n> leif`@`portland:~/Sage/spkgs/sagenb-0.8.1.p1/src/sagenb$ hg status\n> ? sagenb/sagenb.po\n> }}}\n> (This is of course in vanilla 0.8.1, too.)\n\nThis is now #9580.",
    "created_at": "2010-07-23T06:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92097",
    "user": "mpatel"
}
```

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

archive/issue_comments_092098.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-23T07:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92098",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_092099.json:
```json
{
    "body": "I've merged the patch into SageNB 0.8.2, which awaits review at #9572.",
    "created_at": "2010-07-23T07:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92099",
    "user": "mpatel"
}
```

I've merged the patch into SageNB 0.8.2, which awaits review at #9572.



---

archive/issue_comments_092100.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n> (I'm not going to upload the patched spkg though, it's almost 19MB. So if appropriate, someone else has to provide it on sage.math.)\n\nDo you have a Sage cluster (i.e., sage.math, boxen.math, etc.) account?  If not, William Stein can make one for you.",
    "created_at": "2010-07-23T07:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9554#issuecomment-92100",
    "user": "mpatel"
}
```

Replying to [comment:4 leif]:
> (I'm not going to upload the patched spkg though, it's almost 19MB. So if appropriate, someone else has to provide it on sage.math.)

Do you have a Sage cluster (i.e., sage.math, boxen.math, etc.) account?  If not, William Stein can make one for you.
