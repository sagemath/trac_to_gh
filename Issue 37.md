# Issue 37: preparser doesn't parse hex input:

archive/issues_000037.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: 0x5\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     ZZ(0)x5\n           ^\nSyntaxError: invalid syntax\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/37\n\n",
    "created_at": "2006-09-12T23:30:00Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "preparser doesn't parse hex input:",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/37",
    "user": "was"
}
```
Assignee: somebody


```
sage: 0x5
------------------------------------------------------------
   File "<ipython console>", line 1
     ZZ(0)x5
           ^
SyntaxError: invalid syntax
```



Issue created by migration from https://trac.sagemath.org/ticket/37





---

archive/issue_comments_000234.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2006-09-12T23:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/37",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/37#issuecomment-234",
    "user": "was"
}
```

Changing priority from major to minor.



---

archive/issue_comments_000235.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2006-09-12T23:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/37",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/37#issuecomment-235",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_000236.json:
```json
{
    "body": "This is still a problem with Sage 2.8.2.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-22T19:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/37",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/37#issuecomment-236",
    "user": "mabshoff"
}
```

This is still a problem with Sage 2.8.2.

Cheers,

Michael



---

archive/issue_comments_000237.json:
```json
{
    "body": "The behaviour has changes (this is 2.10.2):\n\n```\nsage: 0x10\n16\n\nsage: 0xA\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     Integer(0x)A\n                ^\n<type 'exceptions.SyntaxError'>: invalid syntax\n\nsage: 0xa\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     Integer(0x)a\n                ^\n<type 'exceptions.SyntaxError'>: invalid syntax\n```\n",
    "created_at": "2008-02-27T00:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/37",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/37#issuecomment-237",
    "user": "malb"
}
```

The behaviour has changes (this is 2.10.2):

```
sage: 0x10
16

sage: 0xA
------------------------------------------------------------
   File "<ipython console>", line 1
     Integer(0x)A
                ^
<type 'exceptions.SyntaxError'>: invalid syntax

sage: 0xa
------------------------------------------------------------
   File "<ipython console>", line 1
     Integer(0x)a
                ^
<type 'exceptions.SyntaxError'>: invalid syntax
```




---

archive/issue_comments_000238.json:
```json
{
    "body": "Note: #2144 is (a) a dupe of this, and (b) actually doesn't fix the problem.",
    "created_at": "2008-02-28T04:58:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/37",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/37#issuecomment-238",
    "user": "was"
}
```

Note: #2144 is (a) a dupe of this, and (b) actually doesn't fix the problem.



---

archive/issue_comments_000239.json:
```json
{
    "body": "Attachment [sage-37.patch](tarball://root/attachments/some-uuid/ticket37/sage-37.patch) by was created at 2008-02-28 05:07:11",
    "created_at": "2008-02-28T05:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/37",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/37#issuecomment-239",
    "user": "was"
}
```

Attachment [sage-37.patch](tarball://root/attachments/some-uuid/ticket37/sage-37.patch) by was created at 2008-02-28 05:07:11



---

archive/issue_comments_000240.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2008-02-28T05:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/37",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/37#issuecomment-240",
    "user": "was"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_000241.json:
```json
{
    "body": "Doctests look good, commit.",
    "created_at": "2008-02-28T06:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/37",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/37#issuecomment-241",
    "user": "ncalexan"
}
```

Doctests look good, commit.



---

archive/issue_comments_000242.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T06:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/37",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/37#issuecomment-242",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc0



---

archive/issue_comments_000243.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T06:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/37",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/37#issuecomment-243",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_000244.json:
```json
{
    "body": "Nick beat me too it, but I think it looks good too.",
    "created_at": "2008-02-28T08:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/37",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/37#issuecomment-244",
    "user": "robertwb"
}
```

Nick beat me too it, but I think it looks good too.
