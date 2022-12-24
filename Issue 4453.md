# Issue 4453: elliptic curves -- heegner_index command gives nonsense when rank > 1

archive/issues_004453.json:
```json
{
    "body": "Assignee: was\n\nFor any elliptic curve over QQ of rank >= 2 the heegner_index command must always give 0 as output.   So the following 1 at the end is just wrong.\n\n\n```\nsage: E = EllipticCurve('389a')\nsage: D = E.heegner_discriminants_list(1)[0]\nsage: D\n-7\nsage: E.heegner_index(D)\n1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4453\n\n",
    "created_at": "2008-11-06T14:47:03Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.5",
    "title": "elliptic curves -- heegner_index command gives nonsense when rank > 1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4453",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/4453





---

archive/issue_comments_032824.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32824",
    "user": "davidloeffler"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_032825.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-20T19:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32825",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_032826.json:
```json
{
    "body": "Remove assignee davidloeffler.",
    "created_at": "2009-10-09T09:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32826",
    "user": "davidloeffler"
}
```

Remove assignee davidloeffler.



---

archive/issue_comments_032827.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T04:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32827",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_032828.json:
```json
{
    "body": "Depends on #6616?",
    "created_at": "2010-01-20T10:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32828",
    "user": "robertwb"
}
```

Depends on #6616?



---

archive/issue_comments_032829.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T17:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32829",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032830.json:
```json
{
    "body": "Positive review: looks good (apart from a docstring typo \"We higher rank examples\") and applies fine to 4.3.1, tests pass and docs build & look good.\n\nI added a new patch which changes the above to \"Some higher rank examples\" with no further changes.",
    "created_at": "2010-01-31T17:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32830",
    "user": "cremona"
}
```

Positive review: looks good (apart from a docstring typo "We higher rank examples") and applies fine to 4.3.1, tests pass and docs build & look good.

I added a new patch which changes the above to "Some higher rank examples" with no further changes.



---

archive/issue_comments_032831.json:
```json
{
    "body": "I get two hunk failures when applying [trac_4453.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4453/trac_4453.2.patch) on top of Sage 4.3.3.alpha0:\n\n```\n[mvngu@sage sage-main]$ pwd\n/dev/shm/mvngu/sage-4.3.3.alpha0/devel/sage-main\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4453/trac_4453.2.patch && hg qpush\nadding trac_4453.2.patch to series file\napplying trac_4453.2.patch\npatching file sage/schemes/elliptic_curves/heegner.py\nHunk #3 FAILED at 6350\nHunk #4 succeeded at 6370 with fuzz 2 (offset -12 lines).\nHunk #5 FAILED at 6430\n2 out of 5 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/heegner.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_4453.2.patch\n```\n\nThe attachment [trac_4453.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4453/trac_4453.2.patch) needs rebase against Sage 4.3.3.alpha0.",
    "created_at": "2010-02-13T05:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32831",
    "user": "mvngu"
}
```

I get two hunk failures when applying [trac_4453.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4453/trac_4453.2.patch) on top of Sage 4.3.3.alpha0:

```
[mvngu@sage sage-main]$ pwd
/dev/shm/mvngu/sage-4.3.3.alpha0/devel/sage-main
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4453/trac_4453.2.patch && hg qpush
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

archive/issue_comments_032832.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-13T05:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32832",
    "user": "mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_032833.json:
```json
{
    "body": "Attachment [trac_4453-rebased.patch](tarball://root/attachments/some-uuid/ticket4453/trac_4453-rebased.patch) by robertwb created at 2010-07-29 06:02:03",
    "created_at": "2010-07-29T06:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32833",
    "user": "robertwb"
}
```

Attachment [trac_4453-rebased.patch](tarball://root/attachments/some-uuid/ticket4453/trac_4453-rebased.patch) by robertwb created at 2010-07-29 06:02:03



---

archive/issue_comments_032834.json:
```json
{
    "body": "Rebased, I also fixed a small error when check_rank=False.",
    "created_at": "2010-07-29T06:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32834",
    "user": "robertwb"
}
```

Rebased, I also fixed a small error when check_rank=False.



---

archive/issue_comments_032835.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-07-29T06:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32835",
    "user": "robertwb"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_032836.json:
```json
{
    "body": "With the forthcoming 4.5.2 (4.5.2.rc0 + #9226) and the rebased patch, I get a doctest failure:\n\n```python\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/heegner.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/devel/sage/sage/schemes/elliptic_curves/heegner.py\", line 6465:\n    sage: E.heegner_index(-8, descent_second_limit=16)\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_229[14]>\", line 1, in <module>\n        E.heegner_index(-Integer(8), descent_second_limit=Integer(16))###line 6465: \n    sage: E.heegner_index(-8, descent_second_limit=16)\n      File \"/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/lib/python/site-packages/sage/schemes/elliptic_curves/heegner.py\", line 6485, in heegner_index\n        if check_rank and self.rank() >= 2:\n      File \"/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 1741, in rank\n        raise RuntimeError, 'Rank not provably correct.'\n    RuntimeError: Rank not provably correct.\n**********************************************************************\n1 items had failures:\n   1 of  21 in __main__.example_229\n***Test Failed*** 1 failures.\n```\n",
    "created_at": "2010-08-07T09:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32836",
    "user": "mpatel"
}
```

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

archive/issue_comments_032837.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-07T09:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32837",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_032838.json:
```json
{
    "body": "Replying to [comment:8 mpatel]:\n> With the forthcoming 4.5.2 (4.5.2.rc0 + #9226) and the rebased patch, I get a doctest failure:\n\nThat should be \"4.5.2 (4.5.2.rc1 + #9226)\".",
    "created_at": "2010-08-07T10:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32838",
    "user": "mpatel"
}
```

Replying to [comment:8 mpatel]:
> With the forthcoming 4.5.2 (4.5.2.rc0 + #9226) and the rebased patch, I get a doctest failure:

That should be "4.5.2 (4.5.2.rc1 + #9226)".



---

archive/issue_comments_032839.json:
```json
{
    "body": "this patch still applies fine to 4.7.1, and the new examples in the patch seem to work.\nHowever the description says that the following should give 0 and not `+Infinity`:\n\n```\nsage: E = EllipticCurve('389a')\nsage: E.heegner_index(-7)\n+Infinity\n```\n\nIs the description wrong?\n\nPaul",
    "created_at": "2011-09-15T16:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32839",
    "user": "zimmerma"
}
```

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

archive/issue_comments_032840.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-09-15T16:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32840",
    "user": "zimmerma"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_032841.json:
```json
{
    "body": "The description is wrong, the Heegner point is torsion for rank >= 2 curves, hence its index in the full group is infinite.",
    "created_at": "2011-09-15T23:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32841",
    "user": "robertwb"
}
```

The description is wrong, the Heegner point is torsion for rank >= 2 curves, hence its index in the full group is infinite.



---

archive/issue_comments_032842.json:
```json
{
    "body": "thanks Robert. Is the new description ok? I put back as \"needs review\" to check if the doctests\npass.\n\nPaul",
    "created_at": "2011-09-16T06:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32842",
    "user": "zimmerma"
}
```

thanks Robert. Is the new description ok? I put back as "needs review" to check if the doctests
pass.

Paul



---

archive/issue_comments_032843.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-09-16T06:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32843",
    "user": "zimmerma"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_032844.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-09-16T09:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32844",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_032845.json:
```json
{
    "body": "the failure mentioned in comment [comment:8] is still there:\n\n```\nsage: E = EllipticCurve([0, 0, 1, -34874, -2506691])\nsage: E.heegner_index(-8, descent_second_limit=16)\n...\nRuntimeError: Rank not provably correct.\n```\n\nthus this ticket needs work.\n\nPaul",
    "created_at": "2011-09-16T09:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32845",
    "user": "zimmerma"
}
```

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

archive/issue_comments_032846.json:
```json
{
    "body": "Attachment [4453-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket4453/4453-doctest-fix.patch) by robertwb created at 2012-10-24 07:22:12\n\nApply trac_4453-rebased.patch, 4453-doctest-fix.patch",
    "created_at": "2012-10-24T07:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32846",
    "user": "robertwb"
}
```

Attachment [4453-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket4453/4453-doctest-fix.patch) by robertwb created at 2012-10-24 07:22:12

Apply trac_4453-rebased.patch, 4453-doctest-fix.patch



---

archive/issue_comments_032847.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-10-24T07:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32847",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_032848.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-10-24T07:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32848",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032849.json:
```json
{
    "body": "Robert, I find it strange that you give a positive review to your own patch...\n\nPaul",
    "created_at": "2012-10-24T07:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32849",
    "user": "zimmerma"
}
```

Robert, I find it strange that you give a positive review to your own patch...

Paul



---

archive/issue_comments_032850.json:
```json
{
    "body": "I was giving a positive review to the original patch; I suppose someone should review my 1-line doctest fix as well.",
    "created_at": "2012-10-24T07:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32850",
    "user": "robertwb"
}
```

I was giving a positive review to the original patch; I suppose someone should review my 1-line doctest fix as well.



---

archive/issue_comments_032851.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-10-24T07:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32851",
    "user": "robertwb"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_032852.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-10-24T07:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32852",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_032853.json:
```json
{
    "body": "I'll check Robert's one-liner but not this week.",
    "created_at": "2012-10-24T08:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32853",
    "user": "cremona"
}
```

I'll check Robert's one-liner but not this week.



---

archive/issue_comments_032854.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-10-24T09:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32854",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032855.json:
```json
{
    "body": "Rob's patch looks fine to me, and patchbot's happy with it, so let's get this in.",
    "created_at": "2012-10-24T09:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32855",
    "user": "davidloeffler"
}
```

Rob's patch looks fine to me, and patchbot's happy with it, so let's get this in.



---

archive/issue_comments_032856.json:
```json
{
    "body": "Please specify which patch(es) to apply.",
    "created_at": "2012-10-30T16:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32856",
    "user": "jdemeyer"
}
```

Please specify which patch(es) to apply.



---

archive/issue_comments_032857.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2012-10-30T16:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32857",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_032858.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-10-30T17:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32858",
    "user": "robertwb"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_032859.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-10-30T17:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32859",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032860.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-11-01T12:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32860",
    "user": "jdemeyer"
}
```

Resolution: fixed
