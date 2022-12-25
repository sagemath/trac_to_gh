# Issue 4453: elliptic curves -- heegner_index command gives nonsense when rank > 1

archive/issues_004453.json:
```json
{
    "body": "Assignee: @williamstein\n\nFor any elliptic curve over QQ of rank >= 2 the heegner_index command must always give 0 as output.   So the following 1 at the end is just wrong.\n\n\n```\nsage: E = EllipticCurve('389a')\nsage: D = E.heegner_discriminants_list(1)[0]\nsage: D\n-7\nsage: E.heegner_index(D)\n1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4453\n\n",
    "created_at": "2008-11-06T14:47:03Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.5",
    "title": "elliptic curves -- heegner_index command gives nonsense when rank > 1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4453",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

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

archive/issue_comments_032761.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32761",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_032762.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T19:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32762",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_032763.json:
```json
{
    "body": "Remove assignee @loefflerd.",
    "created_at": "2009-10-09T09:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32763",
    "user": "https://github.com/loefflerd"
}
```

Remove assignee @loefflerd.



---

archive/issue_comments_032764.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T04:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32764",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_032765.json:
```json
{
    "body": "Depends on #6616?",
    "created_at": "2010-01-20T10:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32765",
    "user": "https://github.com/robertwb"
}
```

Depends on #6616?



---

archive/issue_comments_032766.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T17:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32766",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032767.json:
```json
{
    "body": "Positive review: looks good (apart from a docstring typo \"We higher rank examples\") and applies fine to 4.3.1, tests pass and docs build & look good.\n\nI added a new patch which changes the above to \"Some higher rank examples\" with no further changes.",
    "created_at": "2010-01-31T17:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32767",
    "user": "https://github.com/JohnCremona"
}
```

Positive review: looks good (apart from a docstring typo "We higher rank examples") and applies fine to 4.3.1, tests pass and docs build & look good.

I added a new patch which changes the above to "Some higher rank examples" with no further changes.



---

archive/issue_comments_032768.json:
```json
{
    "body": "I get two hunk failures when applying [trac_4453.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4453/trac_4453.2.patch) on top of Sage 4.3.3.alpha0:\n\n```\n[mvngu@sage sage-main]$ pwd\n/dev/shm/mvngu/sage-4.3.3.alpha0/devel/sage-main\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4453/trac_4453.2.patch && hg qpush\nadding trac_4453.2.patch to series file\napplying trac_4453.2.patch\npatching file sage/schemes/elliptic_curves/heegner.py\nHunk #3 FAILED at 6350\nHunk #4 succeeded at 6370 with fuzz 2 (offset -12 lines).\nHunk #5 FAILED at 6430\n2 out of 5 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/heegner.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_4453.2.patch\n```\n\nThe attachment [trac_4453.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4453/trac_4453.2.patch) needs rebase against Sage 4.3.3.alpha0.",
    "created_at": "2010-02-13T05:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32768",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
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

archive/issue_comments_032769.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-13T05:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32769",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_032770.json:
```json
{
    "body": "Attachment [trac_4453-rebased.patch](tarball://root/attachments/some-uuid/ticket4453/trac_4453-rebased.patch) by @robertwb created at 2010-07-29 06:02:03",
    "created_at": "2010-07-29T06:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32770",
    "user": "https://github.com/robertwb"
}
```

Attachment [trac_4453-rebased.patch](tarball://root/attachments/some-uuid/ticket4453/trac_4453-rebased.patch) by @robertwb created at 2010-07-29 06:02:03



---

archive/issue_comments_032771.json:
```json
{
    "body": "Rebased, I also fixed a small error when check_rank=False.",
    "created_at": "2010-07-29T06:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32771",
    "user": "https://github.com/robertwb"
}
```

Rebased, I also fixed a small error when check_rank=False.



---

archive/issue_comments_032772.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-07-29T06:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32772",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_032773.json:
```json
{
    "body": "With the forthcoming 4.5.2 (4.5.2.rc0 + #9226) and the rebased patch, I get a doctest failure:\n\n```python\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/heegner.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/devel/sage/sage/schemes/elliptic_curves/heegner.py\", line 6465:\n    sage: E.heegner_index(-8, descent_second_limit=16)\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_229[14]>\", line 1, in <module>\n        E.heegner_index(-Integer(8), descent_second_limit=Integer(16))###line 6465: \n    sage: E.heegner_index(-8, descent_second_limit=16)\n      File \"/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/lib/python/site-packages/sage/schemes/elliptic_curves/heegner.py\", line 6485, in heegner_index\n        if check_rank and self.rank() >= 2:\n      File \"/mnt/usb1/scratch/mpatel/apps/sage-4.5.2/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 1741, in rank\n        raise RuntimeError, 'Rank not provably correct.'\n    RuntimeError: Rank not provably correct.\n**********************************************************************\n1 items had failures:\n   1 of  21 in __main__.example_229\n***Test Failed*** 1 failures.\n```\n",
    "created_at": "2010-08-07T09:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32773",
    "user": "https://github.com/qed777"
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

archive/issue_events_010050.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-07T09:58:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4453#event-10050"
}
```



---

archive/issue_comments_032774.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-07T09:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32774",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_032775.json:
```json
{
    "body": "Replying to [comment:8 mpatel]:\n> With the forthcoming 4.5.2 (4.5.2.rc0 + #9226) and the rebased patch, I get a doctest failure:\n\nThat should be \"4.5.2 (4.5.2.rc1 + #9226)\".",
    "created_at": "2010-08-07T10:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32775",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:8 mpatel]:
> With the forthcoming 4.5.2 (4.5.2.rc0 + #9226) and the rebased patch, I get a doctest failure:

That should be "4.5.2 (4.5.2.rc1 + #9226)".



---

archive/issue_comments_032776.json:
```json
{
    "body": "this patch still applies fine to 4.7.1, and the new examples in the patch seem to work.\nHowever the description says that the following should give 0 and not `+Infinity`:\n\n```\nsage: E = EllipticCurve('389a')\nsage: E.heegner_index(-7)\n+Infinity\n```\n\nIs the description wrong?\n\nPaul",
    "created_at": "2011-09-15T16:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32776",
    "user": "https://github.com/zimmermann6"
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

archive/issue_comments_032777.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-09-15T16:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32777",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_032778.json:
```json
{
    "body": "The description is wrong, the Heegner point is torsion for rank >= 2 curves, hence its index in the full group is infinite.",
    "created_at": "2011-09-15T23:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32778",
    "user": "https://github.com/robertwb"
}
```

The description is wrong, the Heegner point is torsion for rank >= 2 curves, hence its index in the full group is infinite.



---

archive/issue_comments_032779.json:
```json
{
    "body": "thanks Robert. Is the new description ok? I put back as \"needs review\" to check if the doctests\npass.\n\nPaul",
    "created_at": "2011-09-16T06:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32779",
    "user": "https://github.com/zimmermann6"
}
```

thanks Robert. Is the new description ok? I put back as "needs review" to check if the doctests
pass.

Paul



---

archive/issue_comments_032780.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-09-16T06:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32780",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_032781.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-09-16T09:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32781",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_032782.json:
```json
{
    "body": "the failure mentioned in comment [comment:8] is still there:\n\n```\nsage: E = EllipticCurve([0, 0, 1, -34874, -2506691])\nsage: E.heegner_index(-8, descent_second_limit=16)\n...\nRuntimeError: Rank not provably correct.\n```\n\nthus this ticket needs work.\n\nPaul",
    "created_at": "2011-09-16T09:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32782",
    "user": "https://github.com/zimmermann6"
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

archive/issue_comments_032783.json:
```json
{
    "body": "Attachment [4453-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket4453/4453-doctest-fix.patch) by @robertwb created at 2012-10-24 07:22:12\n\nApply trac_4453-rebased.patch, 4453-doctest-fix.patch",
    "created_at": "2012-10-24T07:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32783",
    "user": "https://github.com/robertwb"
}
```

Attachment [4453-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket4453/4453-doctest-fix.patch) by @robertwb created at 2012-10-24 07:22:12

Apply trac_4453-rebased.patch, 4453-doctest-fix.patch



---

archive/issue_comments_032784.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-10-24T07:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32784",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_032785.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-10-24T07:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32785",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032786.json:
```json
{
    "body": "Robert, I find it strange that you give a positive review to your own patch...\n\nPaul",
    "created_at": "2012-10-24T07:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32786",
    "user": "https://github.com/zimmermann6"
}
```

Robert, I find it strange that you give a positive review to your own patch...

Paul



---

archive/issue_comments_032787.json:
```json
{
    "body": "I was giving a positive review to the original patch; I suppose someone should review my 1-line doctest fix as well.",
    "created_at": "2012-10-24T07:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32787",
    "user": "https://github.com/robertwb"
}
```

I was giving a positive review to the original patch; I suppose someone should review my 1-line doctest fix as well.



---

archive/issue_comments_032788.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-10-24T07:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32788",
    "user": "https://github.com/robertwb"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_032789.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-10-24T07:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32789",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_032790.json:
```json
{
    "body": "I'll check Robert's one-liner but not this week.",
    "created_at": "2012-10-24T08:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32790",
    "user": "https://github.com/JohnCremona"
}
```

I'll check Robert's one-liner but not this week.



---

archive/issue_comments_032791.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-10-24T09:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32791",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032792.json:
```json
{
    "body": "Rob's patch looks fine to me, and patchbot's happy with it, so let's get this in.",
    "created_at": "2012-10-24T09:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32792",
    "user": "https://github.com/loefflerd"
}
```

Rob's patch looks fine to me, and patchbot's happy with it, so let's get this in.



---

archive/issue_events_010051.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-10-29T21:29:25Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4453#event-10051"
}
```



---

archive/issue_events_010052.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-10-29T21:29:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "milestone": "sage-5.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4453#event-10052"
}
```



---

archive/issue_comments_032793.json:
```json
{
    "body": "Please specify which patch(es) to apply.",
    "created_at": "2012-10-30T16:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32793",
    "user": "https://github.com/jdemeyer"
}
```

Please specify which patch(es) to apply.



---

archive/issue_comments_032794.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2012-10-30T16:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32794",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_032795.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-10-30T17:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32795",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_032796.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-10-30T17:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32796",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032797.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-11-01T12:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4453#issuecomment-32797",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_010053.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-11-01T12:01:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4453",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4453#event-10053"
}
```
