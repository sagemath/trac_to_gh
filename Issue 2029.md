# Issue 2029: adjust TIMEOUT for long and valgrinded doctests

archive/issues_002029.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.10.1.rc4$ ./sage -t -valgrind -long devel/sage/sage/calculus/calculus.py\nsage -t -valgrind -long devel/sage-main/sage/calculus/calculus.py\nRaising timeout to 1800 seconds due to '-long' option\n\nRaising timeout to 1048576 seconds due to valgrind\n```\n\n\nPatch coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2029\n\n",
    "created_at": "2008-02-02T04:30:56Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "adjust TIMEOUT for long and valgrinded doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2029",
    "user": "mabshoff"
}
```
Assignee: failure


```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.10.1.rc4$ ./sage -t -valgrind -long devel/sage/sage/calculus/calculus.py
sage -t -valgrind -long devel/sage-main/sage/calculus/calculus.py
Raising timeout to 1800 seconds due to '-long' option

Raising timeout to 1048576 seconds due to valgrind
```


Patch coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2029





---

archive/issue_comments_013130.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-02T04:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2029#issuecomment-13130",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013131.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-02-02T04:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2029#issuecomment-13131",
    "user": "mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_013132.json:
```json
{
    "body": "Attachment\n\nPatch applies cleanly. \nTested that -long, -valgrind work as advertised.",
    "created_at": "2008-02-02T04:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2029#issuecomment-13132",
    "user": "jkantor"
}
```

Attachment

Patch applies cleanly. 
Tested that -long, -valgrind work as advertised.



---

archive/issue_comments_013133.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-02T05:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2029#issuecomment-13133",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013134.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc5",
    "created_at": "2008-02-02T05:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2029#issuecomment-13134",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc5



---

archive/issue_comments_013135.json:
```json
{
    "body": "another positive review.",
    "created_at": "2008-02-02T08:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2029#issuecomment-13135",
    "user": "was"
}
```

another positive review.
