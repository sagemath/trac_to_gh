# Issue 1223: doctest timeouts in sage/plot/plot.py on slow systems

archive/issues_001223.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn my trusty OSX 10.4 PPC 1.4GHz iBook I get the following timeout:\n\n```\nmichael-abshoffs-ibook-g4:~/Desktop/sage-2.8.13.rc0 mabshoff$ ./sage -\nt  devel/sage-main/sage/plot/plot.py\nsage -t  devel/sage-main/sage/plot/plot.py                  *** ***\nError: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [269.9 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n        sage -t  devel/sage-main/sage/plot/plot.py\nTotal time for all tests: 269.9 seconds\n```\n\nI have seen similar issues on slower Linux boxen, so maybe we should raise the timeout value.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1223\n\n",
    "created_at": "2007-11-20T22:53:11Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "doctest timeouts in sage/plot/plot.py on slow systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1223",
    "user": "mabshoff"
}
```
Assignee: mabshoff

On my trusty OSX 10.4 PPC 1.4GHz iBook I get the following timeout:

```
michael-abshoffs-ibook-g4:~/Desktop/sage-2.8.13.rc0 mabshoff$ ./sage -
t  devel/sage-main/sage/plot/plot.py
sage -t  devel/sage-main/sage/plot/plot.py                  *** ***
Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [269.9 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:

        sage -t  devel/sage-main/sage/plot/plot.py
Total time for all tests: 269.9 seconds
```

I have seen similar issues on slower Linux boxen, so maybe we should raise the timeout value.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1223





---

archive/issue_comments_007616.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-20T22:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1223#issuecomment-7616",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007617.json:
```json
{
    "body": "Attachment [trac1223.patch](tarball://root/attachments/some-uuid/ticket1223/trac1223.patch) by was created at 2007-11-21 13:18:36\n\nthis optimizes the plot doctests some",
    "created_at": "2007-11-21T13:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1223#issuecomment-7617",
    "user": "was"
}
```

Attachment [trac1223.patch](tarball://root/attachments/some-uuid/ticket1223/trac1223.patch) by was created at 2007-11-21 13:18:36

this optimizes the plot doctests some



---

archive/issue_comments_007618.json:
```json
{
    "body": "trac1223.patch has been applied and doctesting plot.py drops from 51 seconds on sage.math to 35 seconds.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-21T13:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1223#issuecomment-7618",
    "user": "mabshoff"
}
```

trac1223.patch has been applied and doctesting plot.py drops from 51 seconds on sage.math to 35 seconds.

Cheers,

Michael



---

archive/issue_comments_007619.json:
```json
{
    "body": "Attachment [trac1223b.patch](tarball://root/attachments/some-uuid/ticket1223/trac1223b.patch) by was created at 2007-11-21 13:33:17\n\nspeed ups for graph generators and database doctests",
    "created_at": "2007-11-21T13:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1223#issuecomment-7619",
    "user": "was"
}
```

Attachment [trac1223b.patch](tarball://root/attachments/some-uuid/ticket1223/trac1223b.patch) by was created at 2007-11-21 13:33:17

speed ups for graph generators and database doctests



---

archive/issue_comments_007620.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-21T13:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1223#issuecomment-7620",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007621.json:
```json
{
    "body": "Merged in 2.8.13.rc2.",
    "created_at": "2007-11-21T13:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1223#issuecomment-7621",
    "user": "mabshoff"
}
```

Merged in 2.8.13.rc2.
