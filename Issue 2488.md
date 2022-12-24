# Issue 2488: unused/broken hanke and pari pxy files

archive/issues_002488.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis file does not compile with cython currently but is in the tree. It is currently disabled in setup.py and should be removed or fixed. This is a significant priority as it makes the development of efficient(parallel) build systems problematic and wastes space, especially for files which have not been touched in ages. Code that does not build should not be in the main repository. \n\n```\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n290 problem.\n\"\"\"\n\n\n\ninclude 'interrupt.pxi'\n^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/libs/hanke/hanke.pyx:17:0: 'interrupt.pxi' not found\n\n\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o hanke.c hanke.pyx\n```\n\n\n```\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n                ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/libs/pari/test.pxd:5:17: Special methods must be declared with 'def', not 'cdef'\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/libs/pari/test.pyx:3:0: 'interrupt.pxi' not found\n\n\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o test.c test.pyx\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2488\n\n",
    "created_at": "2008-03-12T09:34:44Z",
    "labels": [
        "interfaces",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "unused/broken hanke and pari pxy files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2488",
    "user": "@garyfurnish"
}
```
Assignee: @williamstein

This file does not compile with cython currently but is in the tree. It is currently disabled in setup.py and should be removed or fixed. This is a significant priority as it makes the development of efficient(parallel) build systems problematic and wastes space, especially for files which have not been touched in ages. Code that does not build should not be in the main repository. 

```
Error converting Pyrex file to C:
------------------------------------------------------------
...
290 problem.
"""



include 'interrupt.pxi'
^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/libs/hanke/hanke.pyx:17:0: 'interrupt.pxi' not found


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o hanke.c hanke.pyx
```


```
Error converting Pyrex file to C:
------------------------------------------------------------
...
                ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/libs/pari/test.pxd:5:17: Special methods must be declared with 'def', not 'cdef'

Error converting Pyrex file to C:
------------------------------------------------------------
...
^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/libs/pari/test.pyx:3:0: 'interrupt.pxi' not found


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o test.c test.pyx
```


Issue created by migration from https://trac.sagemath.org/ticket/2488





---

archive/issue_comments_016861.json:
```json
{
    "body": "Changing assignee from @williamstein to @garyfurnish.",
    "created_at": "2008-03-13T02:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2488#issuecomment-16861",
    "user": "@garyfurnish"
}
```

Changing assignee from @williamstein to @garyfurnish.



---

archive/issue_comments_016862.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-13T02:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2488#issuecomment-16862",
    "user": "@garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016863.json:
```json
{
    "body": "This is not ready",
    "created_at": "2008-03-13T02:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2488#issuecomment-16863",
    "user": "@garyfurnish"
}
```

This is not ready



---

archive/issue_comments_016864.json:
```json
{
    "body": "Attachment [trac_2488.patch](tarball://root/attachments/some-uuid/ticket2488/trac_2488.patch) by @garyfurnish created at 2008-03-13 02:06:05",
    "created_at": "2008-03-13T02:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2488#issuecomment-16864",
    "user": "@garyfurnish"
}
```

Attachment [trac_2488.patch](tarball://root/attachments/some-uuid/ticket2488/trac_2488.patch) by @garyfurnish created at 2008-03-13 02:06:05



---

archive/issue_comments_016865.json:
```json
{
    "body": "This is now ready for a review.",
    "created_at": "2008-03-13T02:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2488#issuecomment-16865",
    "user": "@garyfurnish"
}
```

This is now ready for a review.



---

archive/issue_comments_016866.json:
```json
{
    "body": "`sage -ba` and a `-testall -long` works after applying this patch. I would suggest contacting the authors of the various files we remove \"just in case\".\n\nCheers,\n\nMichael",
    "created_at": "2008-03-13T07:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2488#issuecomment-16866",
    "user": "mabshoff"
}
```

`sage -ba` and a `-testall -long` works after applying this patch. I would suggest contacting the authors of the various files we remove "just in case".

Cheers,

Michael



---

archive/issue_comments_016867.json:
```json
{
    "body": "Hanke's code has never worked, so it's safe to remove. He can add it back if he can get it to work.  It's a substantial amount of code, but it shouldn't be in sage until it works and has somebody who will maintain it. \n\nThe other pari code -- test.pyx, e.g., was something I wrote and can safely be deleted.",
    "created_at": "2008-03-13T17:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2488#issuecomment-16867",
    "user": "@williamstein"
}
```

Hanke's code has never worked, so it's safe to remove. He can add it back if he can get it to work.  It's a substantial amount of code, but it shouldn't be in sage until it works and has somebody who will maintain it. 

The other pari code -- test.pyx, e.g., was something I wrote and can safely be deleted.



---

archive/issue_comments_016868.json:
```json
{
    "body": "\n```\n[23:00] <mabshoff> wstein: you are fine with the code removal by gfurnish?\n[23:00] <mabshoff> Then I will apply those patches now. \n[23:00] <wstein> yes\n```\n",
    "created_at": "2008-03-14T22:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2488#issuecomment-16868",
    "user": "mabshoff"
}
```


```
[23:00] <mabshoff> wstein: you are fine with the code removal by gfurnish?
[23:00] <mabshoff> Then I will apply those patches now. 
[23:00] <wstein> yes
```




---

archive/issue_comments_016869.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T22:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2488#issuecomment-16869",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016870.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T22:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2488#issuecomment-16870",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
