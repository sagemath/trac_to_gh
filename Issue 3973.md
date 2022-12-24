# Issue 3973: [with patch, needs review] short_weierstrass_model in characteristic 2 and 3

archive/issues_003973.json:
```json
{
    "body": "Assignee: was\n\nCC:  cremona\n\nthis is to correct a small thing in short_weierstrass_model. It used to return an error in characteristic 3 for each curve, even if the curve was given in short weierstrass form.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3973\n\n",
    "created_at": "2008-08-28T11:51:02Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] short_weierstrass_model in characteristic 2 and 3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3973",
    "user": "wuthrich"
}
```
Assignee: was

CC:  cremona

this is to correct a small thing in short_weierstrass_model. It used to return an error in characteristic 3 for each curve, even if the curve was given in short weierstrass form.

Issue created by migration from https://trac.sagemath.org/ticket/3973





---

archive/issue_comments_028545.json:
```json
{
    "body": "Attachment [sage_trac3973.patch](tarball://root/attachments/some-uuid/ticket3973/sage_trac3973.patch) by wuthrich created at 2008-08-28 11:56:33\n\ncorrecting the behaviour of short_weierstrass_model in characteristic 3",
    "created_at": "2008-08-28T11:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3973#issuecomment-28545",
    "user": "wuthrich"
}
```

Attachment [sage_trac3973.patch](tarball://root/attachments/some-uuid/ticket3973/sage_trac3973.patch) by wuthrich created at 2008-08-28 11:56:33

correcting the behaviour of short_weierstrass_model in characteristic 3



---

archive/issue_comments_028546.json:
```json
{
    "body": "Chris,\n\nplease assign a milestone to all tickets you open. Usually the next release is the one that should be selected.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-28T12:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3973#issuecomment-28546",
    "user": "mabshoff"
}
```

Chris,

please assign a milestone to all tickets you open. Usually the next release is the one that should be selected.

Cheers,

Michael



---

archive/issue_comments_028547.json:
```json
{
    "body": "One small comment on the patch: Please escape the hash in the docstring since otherwise TeX will be unhappy when building the documentation:\n\n```\nThis used to be different see trac #3973\n```\n\n\nJohn: I assume this patch is right up your alley.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-28T12:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3973#issuecomment-28547",
    "user": "mabshoff"
}
```

One small comment on the patch: Please escape the hash in the docstring since otherwise TeX will be unhappy when building the documentation:

```
This used to be different see trac #3973
```


John: I assume this patch is right up your alley.

Cheers,

Michael



---

archive/issue_comments_028548.json:
```json
{
    "body": "Attachment [sage_trac3973a.patch](tarball://root/attachments/some-uuid/ticket3973/sage_trac3973a.patch) by cremona created at 2008-08-28 13:36:25",
    "created_at": "2008-08-28T13:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3973#issuecomment-28548",
    "user": "cremona"
}
```

Attachment [sage_trac3973a.patch](tarball://root/attachments/some-uuid/ticket3973/sage_trac3973a.patch) by cremona created at 2008-08-28 13:36:25



---

archive/issue_comments_028549.json:
```json
{
    "body": "Looks good to me -- Chris had already pointed out to me this missing case (in code I wrote).\n\nI fixed the hash, and also made a couple of small other changes to the docstring which makes it clearer (I hope).  \n\nApplies cleanly to 3.1.1, and all doctests in elliptic_curves pass.  I think this (both patches) can be merged.",
    "created_at": "2008-08-28T13:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3973#issuecomment-28549",
    "user": "cremona"
}
```

Looks good to me -- Chris had already pointed out to me this missing case (in code I wrote).

I fixed the hash, and also made a couple of small other changes to the docstring which makes it clearer (I hope).  

Applies cleanly to 3.1.1, and all doctests in elliptic_curves pass.  I think this (both patches) can be merged.



---

archive/issue_comments_028550.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-28T20:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3973#issuecomment-28550",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028551.json:
```json
{
    "body": "Merged both patches in Sage 3.1.2.alpha2",
    "created_at": "2008-08-28T20:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3973#issuecomment-28551",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.1.2.alpha2
