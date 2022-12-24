# Issue 1384: 2.8.15.rc0: fix numerical doctest fallout on PCC

archive/issues_001384.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere are various doctest failures related to numerical noise and different order of result on PPC for\n\ndevel/sage-main/sage/rings/polynomial/complex_roots.py\ndevel/sage-main/sage/rings/polynomial/polynomial_element.pyx\ndevel/sage-main/sage/rings/qqbar.py\n\nPatch coming shortly.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1384\n\n",
    "created_at": "2007-12-03T19:10:19Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "title": "2.8.15.rc0: fix numerical doctest fallout on PCC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1384",
    "user": "mabshoff"
}
```
Assignee: mabshoff

There are various doctest failures related to numerical noise and different order of result on PPC for

devel/sage-main/sage/rings/polynomial/complex_roots.py
devel/sage-main/sage/rings/polynomial/polynomial_element.pyx
devel/sage-main/sage/rings/qqbar.py

Patch coming shortly.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1384





---

archive/issue_comments_008882.json:
```json
{
    "body": "Attachment [Sage-2.8.15.rc1-fix-numerical-noise-OSX-PPC.patch](tarball://root/attachments/some-uuid/ticket1384/Sage-2.8.15.rc1-fix-numerical-noise-OSX-PPC.patch) by mabshoff created at 2007-12-03 19:20:10",
    "created_at": "2007-12-03T19:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1384#issuecomment-8882",
    "user": "mabshoff"
}
```

Attachment [Sage-2.8.15.rc1-fix-numerical-noise-OSX-PPC.patch](tarball://root/attachments/some-uuid/ticket1384/Sage-2.8.15.rc1-fix-numerical-noise-OSX-PPC.patch) by mabshoff created at 2007-12-03 19:20:10



---

archive/issue_comments_008883.json:
```json
{
    "body": "I needed another minimal fix for x86-64 Linux, but this is now in.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-03T19:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1384#issuecomment-8883",
    "user": "mabshoff"
}
```

I needed another minimal fix for x86-64 Linux, but this is now in.

Cheers,

Michael



---

archive/issue_comments_008884.json:
```json
{
    "body": "Merged in 2.8.15.rc1.",
    "created_at": "2007-12-03T19:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1384#issuecomment-8884",
    "user": "mabshoff"
}
```

Merged in 2.8.15.rc1.



---

archive/issue_comments_008885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-03T19:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1384#issuecomment-8885",
    "user": "mabshoff"
}
```

Resolution: fixed
