# Issue 1651: bug in decode

archive/issues_001651.json:
```json
{
    "body": "Assignee: @wdjoyner\n\nReported by Harald Schilly:\n\nHere what I've tried (documentation does it a bit more \"difficult\",\nbut should be the same -- at least I hope so)\nhttp://www.sagemath.org/doc/html/const/node37.html\n\nC = HammingCode(2,GF(5))\nv = matrix(GF(5),[This is the Trac macro *1,0,0,2,1,0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,0,0,2,1,0-macro))\nC.decode(v)\n\nworks (at least no errors), but\n\nv = vector(GF(5),[1,0,0,2,1,0])\nC.decode(v)\n\nsays:\n\nTypeError: Gap produced error output\nPermutation: <expr> must be a positive integer (not a integer)\nexecuting $sage333:=(1, 0, 0, 2, 1, 0);;\n\nI can see the different braces in the output, but internally a 1xn/nx1\nmatrix should handled in some way the same as a vector.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1651\n\n",
    "created_at": "2008-01-01T14:46:56Z",
    "labels": [
        "component: coding theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "bug in decode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1651",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @wdjoyner

Reported by Harald Schilly:

Here what I've tried (documentation does it a bit more "difficult",
but should be the same -- at least I hope so)
http://www.sagemath.org/doc/html/const/node37.html

C = HammingCode(2,GF(5))
v = matrix(GF(5),[This is the Trac macro *1,0,0,2,1,0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,0,0,2,1,0-macro))
C.decode(v)

works (at least no errors), but

v = vector(GF(5),[1,0,0,2,1,0])
C.decode(v)

says:

TypeError: Gap produced error output
Permutation: <expr> must be a positive integer (not a integer)
executing $sage333:=(1, 0, 0, 2, 1, 0);;

I can see the different braces in the output, but internally a 1xn/nx1
matrix should handled in some way the same as a vector.


Issue created by migration from https://trac.sagemath.org/ticket/1651





---

archive/issue_comments_010477.json:
```json
{
    "body": "I fixed this bug. The patch is at\nhttp://sage.math.washington.edu/home/wdj/patches/linear-codes20071210.hg\nIt passes sage -t.",
    "created_at": "2008-01-02T17:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10477",
    "user": "https://github.com/wdjoyner"
}
```

I fixed this bug. The patch is at
http://sage.math.washington.edu/home/wdj/patches/linear-codes20071210.hg
It passes sage -t.



---

archive/issue_comments_010478.json:
```json
{
    "body": "patch for bug fix of decode in linear_code.py",
    "created_at": "2008-01-02T17:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10478",
    "user": "https://github.com/wdjoyner"
}
```

patch for bug fix of decode in linear_code.py



---

archive/issue_comments_010479.json:
```json
{
    "body": "Attachment [linear_code20080102.hg](tarball://root/attachments/some-uuid/ticket1651/linear_code20080102.hg) by @mwhansen created at 2008-01-13 13:44:40",
    "created_at": "2008-01-13T13:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10479",
    "user": "https://github.com/mwhansen"
}
```

Attachment [linear_code20080102.hg](tarball://root/attachments/some-uuid/ticket1651/linear_code20080102.hg) by @mwhansen created at 2008-01-13 13:44:40



---

archive/issue_comments_010480.json:
```json
{
    "body": "Attachment [1651-doctest.patch](tarball://root/attachments/some-uuid/ticket1651/1651-doctest.patch) by @mwhansen created at 2008-01-15 06:41:55",
    "created_at": "2008-01-15T06:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10480",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1651-doctest.patch](tarball://root/attachments/some-uuid/ticket1651/1651-doctest.patch) by @mwhansen created at 2008-01-15 06:41:55



---

archive/issue_comments_010481.json:
```json
{
    "body": "Seems reasonable, I say apply.  The formatting on the 1651-doctest patch is not the best, and I don't think the docstring to decode() is clear about what the acceptable inputs are.",
    "created_at": "2008-01-22T18:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10481",
    "user": "https://github.com/ncalexan"
}
```

Seems reasonable, I say apply.  The formatting on the 1651-doctest patch is not the best, and I don't think the docstring to decode() is clear about what the acceptable inputs are.



---

archive/issue_comments_010482.json:
```json
{
    "body": "Attachment [linear_code20080127.hg](tarball://root/attachments/some-uuid/ticket1651/linear_code20080127.hg) by @wdjoyner created at 2008-01-27 17:07:45\n\nI added an attachment which includes (1) my fix of the H Schilly bug, (2) M Hansen's docstring addition (reformatted, as the referee suggested), (3) an additional doctest (as suggested by the referee).",
    "created_at": "2008-01-27T17:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10482",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [linear_code20080127.hg](tarball://root/attachments/some-uuid/ticket1651/linear_code20080127.hg) by @wdjoyner created at 2008-01-27 17:07:45

I added an attachment which includes (1) my fix of the H Schilly bug, (2) M Hansen's docstring addition (reformatted, as the referee suggested), (3) an additional doctest (as suggested by the referee).



---

archive/issue_comments_010483.json:
```json
{
    "body": "Could we get somebody to review this updated patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-02T03:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10483",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Could we get somebody to review this updated patch?

Cheers,

Michael



---

archive/issue_comments_010484.json:
```json
{
    "body": "Thumbs up from me!",
    "created_at": "2008-02-16T17:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10484",
    "user": "https://github.com/ncalexan"
}
```

Thumbs up from me!



---

archive/issue_comments_010485.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-16T17:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10485",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010486.json:
```json
{
    "body": "Merged linear_code20080127.hg in Sage 2.10.2.alpha0",
    "created_at": "2008-02-16T17:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10486",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged linear_code20080127.hg in Sage 2.10.2.alpha0



---

archive/issue_events_004082.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-16T17:25:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1651#event-4082"
}
```



---

archive/issue_comments_010487.json:
```json
{
    "body": "Arrg, it was actually merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-16T18:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10487",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Arrg, it was actually merged in Sage 2.10.2.alpha1
