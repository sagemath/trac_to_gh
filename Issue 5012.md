# Issue 5012: Solaris 10/x86: Numerical noise in sage/rings/qqbar.py

archive/issues_005012.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  cwitty\n\nHere we go:\n\n```\n[4:36pm] mabs: cwitty: I have another interesting bug for you:\n[4:36pm] mabs: File \"/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-fulvia/devel/sage/sage/rings/qqbar.py\", line 3826:\n[4:36pm] mabs:     sage: cp.complex_roots(30, 1)\n[4:36pm] mabs: Expected:\n[4:36pm] mabs:     [1.189207115002721?,\n[4:36pm] mabs:     -1.189207115002721?,\n[4:36pm] mabs:     1.189207115002721?*I,\n[4:36pm] mabs:     -1.189207115002721?*I]\n[4:36pm] mabs: Got:\n[4:36pm] mabs:     [1.189207115002721?, -1.189207115002722?, 1.189207115002721?*I, -1.189207115002721?*I]\n[4:37pm] mabs: Notice that the second and third entries are different?\n[4:37pm] mabs: Ehh, the second only\n[4:38pm] cwitty: Yes.  It's probably not a bug; complex_roots doesn't guarantee to find the tightest possible \ninterval, and it depends on ATLAS which doesn't guarantee identical results.\n[4:38pm] mabs: ok\n[4:38pm] mabs: Should I use \"...\" then?\n[4:38pm] cwitty: Yes.\n```\n\n\nPatch coming up. Credit is shared with cwitty.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5012\n\n",
    "created_at": "2009-01-18T06:50:40Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Solaris 10/x86: Numerical noise in sage/rings/qqbar.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5012",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  cwitty

Here we go:

```
[4:36pm] mabs: cwitty: I have another interesting bug for you:
[4:36pm] mabs: File "/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-fulvia/devel/sage/sage/rings/qqbar.py", line 3826:
[4:36pm] mabs:     sage: cp.complex_roots(30, 1)
[4:36pm] mabs: Expected:
[4:36pm] mabs:     [1.189207115002721?,
[4:36pm] mabs:     -1.189207115002721?,
[4:36pm] mabs:     1.189207115002721?*I,
[4:36pm] mabs:     -1.189207115002721?*I]
[4:36pm] mabs: Got:
[4:36pm] mabs:     [1.189207115002721?, -1.189207115002722?, 1.189207115002721?*I, -1.189207115002721?*I]
[4:37pm] mabs: Notice that the second and third entries are different?
[4:37pm] mabs: Ehh, the second only
[4:38pm] cwitty: Yes.  It's probably not a bug; complex_roots doesn't guarantee to find the tightest possible 
interval, and it depends on ATLAS which doesn't guarantee identical results.
[4:38pm] mabs: ok
[4:38pm] mabs: Should I use "..." then?
[4:38pm] cwitty: Yes.
```


Patch coming up. Credit is shared with cwitty.

Issue created by migration from https://trac.sagemath.org/ticket/5012





---

archive/issue_comments_038200.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-18T06:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5012#issuecomment-38200",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038201.json:
```json
{
    "body": "Attachment [trac_5012_qqbar_numerical_noise.patch](tarball://root/attachments/some-uuid/ticket5012/trac_5012_qqbar_numerical_noise.patch) by craigcitro created at 2009-01-18 12:38:11\n\nPatch looks pretty good, with one exception: guaranteed is misspelled in the patch. Once that is fixed, this looks good.",
    "created_at": "2009-01-18T12:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5012#issuecomment-38201",
    "user": "craigcitro"
}
```

Attachment [trac_5012_qqbar_numerical_noise.patch](tarball://root/attachments/some-uuid/ticket5012/trac_5012_qqbar_numerical_noise.patch) by craigcitro created at 2009-01-18 12:38:11

Patch looks pretty good, with one exception: guaranteed is misspelled in the patch. Once that is fixed, this looks good.



---

archive/issue_comments_038202.json:
```json
{
    "body": "I fixed the spelling issue in the patch I applied.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-18T14:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5012#issuecomment-38202",
    "user": "mabshoff"
}
```

I fixed the spelling issue in the patch I applied.

Cheers,

Michael



---

archive/issue_comments_038203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T14:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5012#issuecomment-38203",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038204.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-18T14:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5012#issuecomment-38204",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0
