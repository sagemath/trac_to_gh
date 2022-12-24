# Issue 9944: partial_fraction_decomposition broken for FpT elements

archive/issues_009944.json:
```json
{
    "body": "Assignee: AlexGhitza\n\n\n```\n> sage: R.<x> = GF(3)[]\n> sage: q = (x+1)/(x^3+x+1)\n> sage: q.partial_fraction_decomposition()\n```\n\n\nSee http://groups.google.com/group/sage-support/browse_thread/thread/5423a314227309b3#\n\nIssue created by migration from https://trac.sagemath.org/ticket/9945\n\n",
    "created_at": "2010-09-18T23:41:19Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "partial_fraction_decomposition broken for FpT elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9944",
    "user": "robertwb"
}
```
Assignee: AlexGhitza


```
> sage: R.<x> = GF(3)[]
> sage: q = (x+1)/(x^3+x+1)
> sage: q.partial_fraction_decomposition()
```


See http://groups.google.com/group/sage-support/browse_thread/thread/5423a314227309b3#

Issue created by migration from https://trac.sagemath.org/ticket/9945





---

archive/issue_comments_099133.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-19T00:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99133",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099134.json:
```json
{
    "body": "Attachment [9945-part-frac-FpT.patch](tarball://root/attachments/some-uuid/ticket9945/9945-part-frac-FpT.patch) by robertwb created at 2010-09-19 00:11:51",
    "created_at": "2010-09-19T00:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99134",
    "user": "robertwb"
}
```

Attachment [9945-part-frac-FpT.patch](tarball://root/attachments/some-uuid/ticket9945/9945-part-frac-FpT.patch) by robertwb created at 2010-09-19 00:11:51



---

archive/issue_comments_099135.json:
```json
{
    "body": "Two small comments: in line 115 of sage/categories/quotient_fields.py, \"in-exact\" should be\n\"inexact\". Also I don't understand \"what side effects would this have this be bad?\" on line 166.\n\nPaul",
    "created_at": "2010-09-19T19:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99135",
    "user": "zimmerma"
}
```

Two small comments: in line 115 of sage/categories/quotient_fields.py, "in-exact" should be
"inexact". Also I don't understand "what side effects would this have this be bad?" on line 166.

Paul



---

archive/issue_comments_099136.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-19T19:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99136",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099137.json:
```json
{
    "body": "in addition, 2 doctests fail (with 4.5.3):\n\n```\nThe following tests failed:\n\n        sage -t  devel/sage-9945/sage/rings/ring.pyx # 2 doctests failed\n----------------------------------------------------------------------\nTimings have been updated.\nTotal time for all tests: 5056.9 seconds\n```\n\nPaul",
    "created_at": "2010-09-19T21:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99137",
    "user": "zimmerma"
}
```

in addition, 2 doctests fail (with 4.5.3):

```
The following tests failed:

        sage -t  devel/sage-9945/sage/rings/ring.pyx # 2 doctests failed
----------------------------------------------------------------------
Timings have been updated.
Total time for all tests: 5056.9 seconds
```

Paul



---

archive/issue_comments_099138.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-21T06:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99138",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099139.json:
```json
{
    "body": "Attachment [9945-referee-fixes.patch](tarball://root/attachments/some-uuid/ticket9945/9945-referee-fixes.patch) by robertwb created at 2010-09-21 06:27:34\n\nI was just moving code, but it doesn't hurt to clean it up as I do so (and I was the original author, so the criticism is just :) I removed the TODO, I was thinking about changing the factor command to group \"equal\" roots but that would be too invasive of a change to consider right now.",
    "created_at": "2010-09-21T06:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99139",
    "user": "robertwb"
}
```

Attachment [9945-referee-fixes.patch](tarball://root/attachments/some-uuid/ticket9945/9945-referee-fixes.patch) by robertwb created at 2010-09-21 06:27:34

I was just moving code, but it doesn't hurt to clean it up as I do so (and I was the original author, so the criticism is just :) I removed the TODO, I was thinking about changing the factor command to group "equal" roots but that would be too invasive of a change to consider right now.



---

archive/issue_comments_099140.json:
```json
{
    "body": "Robert, sorry the original patch fails to apply to 4.6.alpha1:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nLoading Sage library. Current Mercurial branch is: 9945\nsage: hg_sage.import_patch(\"/tmp/9945-part-frac-FpT.patch\")\ncd \"/tmp/sage-4.6.alpha1/devel/sage\" && hg status\ncd \"/tmp/sage-4.6.alpha1/devel/sage\" && hg status\ncd \"/tmp/sage-4.6.alpha1/devel/sage\" && hg import   \"/tmp/9945-part-frac-FpT.patch\"\napplying /tmp/9945-part-frac-FpT.patch\npatching file sage/rings/fraction_field_element.pyx\nHunk #3 FAILED at 282\n1 out of 4 hunks FAILED -- saving rejects to file sage/rings/fraction_field_element.pyx.rej\nabort: patch failed to apply\n```\n\nPlease could you rebase it?\n| Sage Version 4.6.alpha1, Release Date: 2010-09-18                  |\n| Type notebook() for the GUI, and license() for information.        |\nPaul",
    "created_at": "2010-09-21T07:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99140",
    "user": "zimmerma"
}
```

Robert, sorry the original patch fails to apply to 4.6.alpha1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: 9945
sage: hg_sage.import_patch("/tmp/9945-part-frac-FpT.patch")
cd "/tmp/sage-4.6.alpha1/devel/sage" && hg status
cd "/tmp/sage-4.6.alpha1/devel/sage" && hg status
cd "/tmp/sage-4.6.alpha1/devel/sage" && hg import   "/tmp/9945-part-frac-FpT.patch"
applying /tmp/9945-part-frac-FpT.patch
patching file sage/rings/fraction_field_element.pyx
Hunk #3 FAILED at 282
1 out of 4 hunks FAILED -- saving rejects to file sage/rings/fraction_field_element.pyx.rej
abort: patch failed to apply
```

Please could you rebase it?
| Sage Version 4.6.alpha1, Release Date: 2010-09-18                  |
| Type notebook() for the GUI, and license() for information.        |
Paul



---

archive/issue_comments_099141.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-21T07:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99141",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099142.json:
```json
{
    "body": "Attachment [9945-rebased.patch](tarball://root/attachments/some-uuid/ticket9945/9945-rebased.patch) by robertwb created at 2010-09-22 03:46:00\n\napply only this patch",
    "created_at": "2010-09-22T03:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99142",
    "user": "robertwb"
}
```

Attachment [9945-rebased.patch](tarball://root/attachments/some-uuid/ticket9945/9945-rebased.patch) by robertwb created at 2010-09-22 03:46:00

apply only this patch



---

archive/issue_comments_099143.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-22T03:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99143",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099144.json:
```json
{
    "body": "The rebased patch works ok with 4.6.alpha1.",
    "created_at": "2010-09-22T10:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99144",
    "user": "zimmerma"
}
```

The rebased patch works ok with 4.6.alpha1.



---

archive/issue_comments_099145.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T10:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99145",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099146.json:
```json
{
    "body": "Rebased against #8334 which should be in 4.6.alpha2.  Apply only this patch.",
    "created_at": "2010-09-29T09:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99146",
    "user": "mpatel"
}
```

Rebased against #8334 which should be in 4.6.alpha2.  Apply only this patch.



---

archive/issue_comments_099147.json:
```json
{
    "body": "Attachment [9945-rebased.2.patch](tarball://root/attachments/some-uuid/ticket9945/9945-rebased.2.patch) by mpatel created at 2010-09-29 09:22:46\n\nI've attached a patch rebased for the queue in [merger-4.6.alpha2](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2).",
    "created_at": "2010-09-29T09:22:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99147",
    "user": "mpatel"
}
```

Attachment [9945-rebased.2.patch](tarball://root/attachments/some-uuid/ticket9945/9945-rebased.2.patch) by mpatel created at 2010-09-29 09:22:46

I've attached a patch rebased for the queue in [merger-4.6.alpha2](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2).



---

archive/issue_comments_099148.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T10:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9944#issuecomment-99148",
    "user": "mpatel"
}
```

Resolution: fixed
