# Issue 5493: [with patch, needs review]

archive/issues_005493.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: sphinx, crypto\n\nThe attached patch makes the Sphinx output for `mq.SR` look much nicer.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5493\n\n",
    "created_at": "2009-03-11T23:03:38Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5493",
    "user": "@malb"
}
```
Assignee: @malb

Keywords: sphinx, crypto

The attached patch makes the Sphinx output for `mq.SR` look much nicer.

Issue created by migration from https://trac.sagemath.org/ticket/5493





---

archive/issue_comments_042666.json:
```json
{
    "body": "Attachment [sr_sphinx.patch](tarball://root/attachments/some-uuid/ticket5493/sr_sphinx.patch) by @malb created at 2009-03-11 23:03:54\n\nyay, my first sphinx patch",
    "created_at": "2009-03-11T23:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5493#issuecomment-42666",
    "user": "@malb"
}
```

Attachment [sr_sphinx.patch](tarball://root/attachments/some-uuid/ticket5493/sr_sphinx.patch) by @malb created at 2009-03-11 23:03:54

yay, my first sphinx patch



---

archive/issue_comments_042667.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch **sr_sphinx.patch** applied fine against Sage version 3.4. All tests passed, even with the `-long` option. The reference manual (which the patch touches) builds OK and looks rather prettier, which is what Martin wants :-)  Positive review.\n\n\n\nNote that while reviewing this ticket, I also noticed some further enhancements that can be done to `sr.py`. But these are addressed in ticket #5527.",
    "created_at": "2009-03-16T07:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5493#issuecomment-42667",
    "user": "mvngu"
}
```

REFEREE REPORT



The patch **sr_sphinx.patch** applied fine against Sage version 3.4. All tests passed, even with the `-long` option. The reference manual (which the patch touches) builds OK and looks rather prettier, which is what Martin wants :-)  Positive review.



Note that while reviewing this ticket, I also noticed some further enhancements that can be done to `sr.py`. But these are addressed in ticket #5527.



---

archive/issue_comments_042668.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-20T20:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5493#issuecomment-42668",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_042669.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-20T20:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5493#issuecomment-42669",
    "user": "mabshoff"
}
```

Resolution: fixed
