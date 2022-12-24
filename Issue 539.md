# Issue 539: Integer.__int__

archive/issues_000539.json:
```json
{
    "body": "Assignee: somebody\n\nThe `Integer.__int__` method was recently changed to use the new `mpz_get_pyintlong` function. This had to be disabled for 2.8.3 because of strange problems on 64-bit architectures, relating we think somehow to the resolution of #411. Figure out what was going wrong and re-enable that functionality (since `mpz_get_pyintlong` is faster than going via a python long every time).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/539\n\n",
    "created_at": "2007-08-31T01:24:26Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "Integer.__int__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/539",
    "user": "dmharvey"
}
```
Assignee: somebody

The `Integer.__int__` method was recently changed to use the new `mpz_get_pyintlong` function. This had to be disabled for 2.8.3 because of strange problems on 64-bit architectures, relating we think somehow to the resolution of #411. Figure out what was going wrong and re-enable that functionality (since `mpz_get_pyintlong` is faster than going via a python long every time).


Issue created by migration from https://trac.sagemath.org/ticket/539





---

archive/issue_comments_002744.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T03:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/539#issuecomment-2744",
    "user": "was"
}
```

Resolution: fixed
