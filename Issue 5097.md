# Issue 5097: doctest failures in 3.3.alpha2 due to lack of #optional tag

archive/issues_005097.json:
```json
{
    "body": "Assignee: @aghitza\n\nSeveral doctests in interfaces/octave.py and interfaces/maple.py should be marked optional but aren't.  Trivial patch coming up.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5097\n\n",
    "created_at": "2009-01-25T08:20:07Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "doctest failures in 3.3.alpha2 due to lack of #optional tag",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5097",
    "user": "https://github.com/aghitza"
}
```
Assignee: @aghitza

Several doctests in interfaces/octave.py and interfaces/maple.py should be marked optional but aren't.  Trivial patch coming up.


Issue created by migration from https://trac.sagemath.org/ticket/5097





---

archive/issue_comments_038805.json:
```json
{
    "body": "Thanks for the fixes, but they all should read\n\n```\n# optional -- requires Octave \n```\nor whatever system is required. I will fix the patch if no one beats me to it.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T14:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5097#issuecomment-38805",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_038806.json:
```json
{
    "body": "Attachment [trac_5097.patch](tarball://root/attachments/some-uuid/ticket5097/trac_5097.patch) by @aghitza created at 2009-01-25 16:53:18",
    "created_at": "2009-01-25T16:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5097#issuecomment-38806",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5097.patch](tarball://root/attachments/some-uuid/ticket5097/trac_5097.patch) by @aghitza created at 2009-01-25 16:53:18



---

archive/issue_comments_038807.json:
```json
{
    "body": "Done.",
    "created_at": "2009-01-25T16:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5097#issuecomment-38807",
    "user": "https://github.com/aghitza"
}
```

Done.



---

archive/issue_comments_038808.json:
```json
{
    "body": "Positive review. I changed some of the doctests tags to be more consitent, but now the doctests without maple and octave pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T21:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5097#issuecomment-38808",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. I changed some of the doctests tags to be more consitent, but now the doctests without maple and octave pass.

Cheers,

Michael



---

archive/issue_events_011769.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-25T21:03:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5097#event-11769"
}
```



---

archive/issue_comments_038809.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3",
    "created_at": "2009-01-25T21:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5097#issuecomment-38809",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3



---

archive/issue_comments_038810.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-25T21:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5097#issuecomment-38810",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
