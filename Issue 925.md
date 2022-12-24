# Issue 925: valgrind options to sage (sage -valgrind, sage -callgrind, etc.) should be more customizable

archive/issues_000925.json:
```json
{
    "body": "Assignee: mabshoff\n\nCurrently, running `sage -valgrind` or `sage -callgrind` uses a hardcoded set of command-line arguments (in local/bin/sage-valgrind and local/bin/sage-callgrind respectively).  There should be some way to change the arguments.\n\nIssue created by migration from https://trac.sagemath.org/ticket/925\n\n",
    "created_at": "2007-10-19T06:35:35Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "valgrind options to sage (sage -valgrind, sage -callgrind, etc.) should be more customizable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/925",
    "user": "cwitty"
}
```
Assignee: mabshoff

Currently, running `sage -valgrind` or `sage -callgrind` uses a hardcoded set of command-line arguments (in local/bin/sage-valgrind and local/bin/sage-callgrind respectively).  There should be some way to change the arguments.

Issue created by migration from https://trac.sagemath.org/ticket/925





---

archive/issue_comments_005668.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-19T06:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/925#issuecomment-5668",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005669.json:
```json
{
    "body": "A suggested fix for this is to check if some environment variable\n\n```\nSAGE_VALGRIND_OPTIONS\n```\n\nand use the content of that if it is defined. I plan to work on this during Bug Day 4.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-19T06:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/925#issuecomment-5669",
    "user": "mabshoff"
}
```

A suggested fix for this is to check if some environment variable

```
SAGE_VALGRIND_OPTIONS
```

and use the content of that if it is defined. I plan to work on this during Bug Day 4.

Cheers,

Michael



---

archive/issue_comments_005670.json:
```json
{
    "body": "Attachment [trac_925.patch](tarball://root/attachments/some-uuid/ticket925/trac_925.patch) by mabshoff created at 2008-09-15 11:26:07",
    "created_at": "2008-09-15T11:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/925#issuecomment-5670",
    "user": "mabshoff"
}
```

Attachment [trac_925.patch](tarball://root/attachments/some-uuid/ticket925/trac_925.patch) by mabshoff created at 2008-09-15 11:26:07



---

archive/issue_comments_005671.json:
```json
{
    "body": "I have not tested that this works, but I have been discussing with mabshoff as he has tested. Looks good to me.",
    "created_at": "2008-09-15T11:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/925#issuecomment-5671",
    "user": "@rlmill"
}
```

I have not tested that this works, but I have been discussing with mabshoff as he has tested. Looks good to me.



---

archive/issue_comments_005672.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-15T11:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/925#issuecomment-5672",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_005673.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc4",
    "created_at": "2008-09-15T11:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/925#issuecomment-5673",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc4
