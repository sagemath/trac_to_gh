# Issue 5097: doctest failures in 3.3.alpha2 due to lack of #optional tag

archive/issues_005097.json:
```json
{
    "body": "Assignee: @aghitza\n\nSeveral doctests in interfaces/octave.py and interfaces/maple.py should be marked optional but aren't.  Trivial patch coming up.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5097\n\n",
    "created_at": "2009-01-25T08:20:07Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "doctest failures in 3.3.alpha2 due to lack of #optional tag",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5097",
    "user": "@aghitza"
}
```
Assignee: @aghitza

Several doctests in interfaces/octave.py and interfaces/maple.py should be marked optional but aren't.  Trivial patch coming up.


Issue created by migration from https://trac.sagemath.org/ticket/5097





---

archive/issue_comments_038879.json:
```json
{
    "body": "Thanks for the fixes, but they all should read\n\n```\n# optional -- requires Octave \n```\n\nor whatever system is required. I will fix the patch if no one beats me to it.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T14:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5097#issuecomment-38879",
    "user": "mabshoff"
}
```

Thanks for the fixes, but they all should read

```
# optional -- requires Octave 
```

or whatever system is required. I will fix the patch if no one beats me to it.

Cheers,

Michael



---

archive/issue_comments_038880.json:
```json
{
    "body": "Attachment [trac_5097.patch](tarball://root/attachments/some-uuid/ticket5097/trac_5097.patch) by @aghitza created at 2009-01-25 16:53:18",
    "created_at": "2009-01-25T16:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5097#issuecomment-38880",
    "user": "@aghitza"
}
```

Attachment [trac_5097.patch](tarball://root/attachments/some-uuid/ticket5097/trac_5097.patch) by @aghitza created at 2009-01-25 16:53:18



---

archive/issue_comments_038881.json:
```json
{
    "body": "Done.",
    "created_at": "2009-01-25T16:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5097#issuecomment-38881",
    "user": "@aghitza"
}
```

Done.



---

archive/issue_comments_038882.json:
```json
{
    "body": "Positive review. I changed some of the doctests tags to be more consitent, but now the doctests without maple and octave pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T21:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5097#issuecomment-38882",
    "user": "mabshoff"
}
```

Positive review. I changed some of the doctests tags to be more consitent, but now the doctests without maple and octave pass.

Cheers,

Michael



---

archive/issue_comments_038883.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3",
    "created_at": "2009-01-25T21:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5097#issuecomment-38883",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3



---

archive/issue_comments_038884.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-25T21:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5097#issuecomment-38884",
    "user": "mabshoff"
}
```

Resolution: fixed
