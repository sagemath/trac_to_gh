# Issue 6080: Add utility methods to Integer (needed for mpmath)

archive/issues_006080.json:
```json
{
    "body": "Assignee: somebody\n\nPatch adds sqrtrem (I only found an existing isqrt) and a method to count trailing zero bits, both of which are needed to make mpmath on top of sage.Integer reasonably fast.\n\nThe value of (0).trailing_zero_bits() (as well as the name of the method) could be adjusted.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6080\n\n",
    "created_at": "2009-05-19T03:35:31Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Add utility methods to Integer (needed for mpmath)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6080",
    "user": "fredrik.johansson"
}
```
Assignee: somebody

Patch adds sqrtrem (I only found an existing isqrt) and a method to count trailing zero bits, both of which are needed to make mpmath on top of sage.Integer reasonably fast.

The value of (0).trailing_zero_bits() (as well as the name of the method) could be adjusted.

Issue created by migration from https://trac.sagemath.org/ticket/6080





---

archive/issue_comments_048396.json:
```json
{
    "body": "Attachment [intutils.patch](tarball://root/attachments/some-uuid/ticket6080/intutils.patch) by mvngu created at 2009-05-19 03:56:34",
    "created_at": "2009-05-19T03:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6080#issuecomment-48396",
    "user": "mvngu"
}
```

Attachment [intutils.patch](tarball://root/attachments/some-uuid/ticket6080/intutils.patch) by mvngu created at 2009-05-19 03:56:34



---

archive/issue_comments_048397.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-05-19T04:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6080#issuecomment-48397",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_048398.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T20:37:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6080#issuecomment-48398",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_048399.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T20:37:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6080#issuecomment-48399",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael
