# Issue 4067: [with patch, needs review] hmm.pyx and ghmm.pyx valgrind issues

archive/issues_004067.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is a broken out patch from #3984. It does not fix the doctest, but numerous issues valgrind picks up. Someone needs to remember that C strings are NULL terminated :)\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4067\n\n",
    "created_at": "2008-09-05T10:10:37Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] hmm.pyx and ghmm.pyx valgrind issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4067",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This is a broken out patch from #3984. It does not fix the doctest, but numerous issues valgrind picks up. Someone needs to remember that C strings are NULL terminated :)

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4067





---

archive/issue_comments_029351.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-05T10:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4067#issuecomment-29351",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029352.json:
```json
{
    "body": "Attachment\n\nPatch looks good, I only read it though.",
    "created_at": "2008-09-05T10:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4067#issuecomment-29352",
    "user": "malb"
}
```

Attachment

Patch looks good, I only read it though.



---

archive/issue_comments_029353.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-05T11:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4067#issuecomment-29353",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc0



---

archive/issue_comments_029354.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-05T11:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4067#issuecomment-29354",
    "user": "mabshoff"
}
```

Resolution: fixed
